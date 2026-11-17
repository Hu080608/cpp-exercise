/* C++ 在线编译运行
 * 主通道：Judge0 CE（公共 CORS API）
 * 备用通道：Wandbox（公共 CORS API）
 * 任一服务繁忙/不可用时自动切换，不需要自建后端。
 */
(function () {
  'use strict';
  const JUDGE0_URL = 'https://ce.judge0.com/submissions?base64_encoded=false&wait=true';
  const JUDGE0_LANG_ID = 105; // C++ (GCC 14.1.0)
  const WANDBOX_URL = 'https://wandbox.org/api/compile.json';
  const WANDBOX_COMPILER = 'gcc-head';
  const DEFAULT_TIMEOUT = 40000;
  let preferredProvider = null;

  class ProviderError extends Error {
    constructor(message, provider) { super(message); this.name = 'ProviderError'; this.provider = provider; }
  }

  function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

  function normalizeOutput(s) {
    return String(s == null ? '' : s).replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n').map(line => line.replace(/[ \t]+$/g, '')).join('\n').replace(/\n+$/g, '');
  }

  function friendlyError(msg) {
    const text = String(msg || '');
    const hints = [];
    if (/expected ['‘’]?;|expected ';'/.test(text)) hints.push('可能少写了分号；检查报错行及上一行的末尾。');
    if (/was not declared in this scope|undeclared/.test(text)) hints.push('使用了未声明/拼错的变量或函数；检查大小写、作用域与头文件。');
    if (/no matching function|invalid conversion|cannot convert/.test(text)) hints.push('参数或赋值类型不匹配，检查函数签名与变量类型。');
    if (/expected primary-expression|expected expression/.test(text)) hints.push('表达式不完整，检查括号、操作符两侧是否有操作数。');
    if (/redefinition|multiple definition/.test(text)) hints.push('同一作用域重复定义；检查是否重复包含了定义或函数体。');
    if (/No such file or directory/.test(text)) hints.push('头文件/源文件找不到，检查 #include 名称。');
    if (/expected unqualified-id/.test(text)) hints.push('可能是关键词被当作变量名，或括号配对错误。');
    if (/Segmentation fault|SIGSEGV|core dumped|Runtime Error/.test(text)) hints.push('程序运行时异常退出，常见原因有数组越界、空指针解引用、除以零或递归过深。');
    if (/warning:/.test(text)) hints.push('编译通过但有警告，建议逐条检查警告信息。');
    return hints.length ? '可能的排查方向：\n' + hints.map((h, i) => (i + 1) + '. ' + h).join('\n') : '';
  }

  function providerIssue(text) {
    return /OCI runtime error|crun:|Resource temporarily unavailable|Service Unavailable|Internal Server Error|maintenance|temporarily unavailable|too many requests|rate limit/i.test(String(text || ''));
  }

  async function fetchJson(url, options, timeoutMs) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs || DEFAULT_TIMEOUT);
    try {
      const res = await fetch(url, Object.assign({}, options, { signal: controller.signal }));
      if (!res.ok) throw new ProviderError('HTTP ' + res.status, options && options.provider);
      return await res.json();
    } finally { clearTimeout(timer); }
  }

  async function runJudge0(code, stdin, opts) {
    const started = performance.now();
    const data = await fetchJson(JUDGE0_URL, {
      provider: 'Judge0',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ language_id: JUDGE0_LANG_ID, source_code: String(code), stdin: String(stdin || '') })
    }, (opts && opts.timeout) || DEFAULT_TIMEOUT).catch(err => {
      throw new ProviderError(err && err.name === 'AbortError' ? 'Judge0 响应超时' : ('Judge0 连接失败：' + (err.message || '网络错误')), 'Judge0');
    });
    if (!data || !data.status) throw new ProviderError('Judge0 返回了无法解析的结果。', 'Judge0');
    const sid = Number(data.status.id || 0);
    if (sid === 1 || sid === 2) throw new ProviderError('Judge0 排队超时。', 'Judge0');
    if (sid === 13 || sid === 14) throw new ProviderError('Judge0 内部错误：' + (data.message || data.status.description), 'Judge0');
    const compileOutput = data.compile_output || '';
    const stderr = data.stderr || '';
    const message = data.message || '';
    if (providerIssue(compileOutput + '\n' + stderr + '\n' + message)) throw new ProviderError('Judge0 服务暂时繁忙。', 'Judge0');
    const compiled = sid !== 6;
    const accepted = sid === 3;
    const durationMs = Math.round(performance.now() - started);
    let error = '';
    if (!compiled) error = compileOutput || message || '编译失败。';
    else if (!accepted) {
      if (sid === 5) error = '运行超时：程序超过在线编译服务的时间限制。';
      else error = stderr || message || (data.status.description || '运行失败。');
    }
    return {
      ok: accepted,
      compiled,
      phase: compiled ? 'run' : 'compile',
      stdout: data.stdout || '',
      stderr: stderr,
      compilerOutput: '',
      compilerError: compileOutput,
      compileOutput: compileOutput,
      status: String(sid),
      statusDescription: data.status.description || '',
      signal: '',
      time: data.time || '',
      memory: data.memory || '',
      provider: 'judge0',
      providerLabel: 'Judge0 · GCC 14.1',
      durationMs,
      error,
      friendly: friendlyError(compileOutput || stderr || message)
    };
  }

  async function runWandbox(code, stdin, opts) {
    const started = performance.now();
    const data = await fetchJson(WANDBOX_URL, {
      provider: 'Wandbox',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        compiler: WANDBOX_COMPILER,
        code: String(code),
        stdin: String(stdin || ''),
        'compiler-option-raw': '-std=c++17',
        'runtime-option-raw': ''
      })
    }, (opts && opts.timeout) || DEFAULT_TIMEOUT).catch(err => {
      throw new ProviderError(err && err.name === 'AbortError' ? 'Wandbox 响应超时' : ('Wandbox 连接失败：' + (err.message || '网络错误')), 'Wandbox');
    });
    const compilerError = data.compiler_error || '';
    const compilerOutput = data.compiler_output || '';
    const status = String(data.status == null ? '' : data.status);
    if (providerIssue(compilerError + '\n' + compilerOutput)) throw new ProviderError('Wandbox 运行环境暂时不可用（OCI/crun 资源繁忙）。', 'Wandbox');
    if (!data || data.status == null) throw new ProviderError('Wandbox 返回了无法解析的结果。', 'Wandbox');
    const hasCompileError = status === '1' || /(^|\n).*error:/.test(compilerError);
    const compiled = !hasCompileError;
    const runtimeFailed = compiled && (status !== '0' || !!data.program_error || !!data.signal);
    let error = '';
    if (!compiled) error = compilerError || compilerOutput || '编译失败。';
    else if (runtimeFailed) error = data.program_error || ('程序异常终止：返回码/信号 ' + status + (data.signal ? ' (' + data.signal + ')' : '') + '。常见原因包括数组越界、空指针解引用、除以零或递归过深。');
    return {
      ok: compiled && !runtimeFailed,
      compiled,
      phase: compiled ? 'run' : 'compile',
      stdout: data.program_output || '',
      stderr: data.program_error || '',
      compilerOutput,
      compilerError,
      compileOutput: compilerError,
      status,
      statusDescription: runtimeFailed ? 'Runtime Error' : (compiled ? 'Accepted' : 'Compilation Error'),
      signal: data.signal || '',
      time: '',
      memory: '',
      provider: 'wandbox',
      providerLabel: 'Wandbox · GCC Head',
      durationMs: Math.round(performance.now() - started),
      error,
      friendly: friendlyError(compilerError || data.program_error || compilerOutput)
    };
  }

  async function runCpp(code, stdin, opts) {
    opts = opts || {};
    if (!code || !String(code).trim()) {
      return { ok: false, compiled: false, phase: 'input', error: '代码为空。', stdout: '', stderr: '', compilerOutput: '', compilerError: '', durationMs: 0 };
    }
    const providers = [
      { name: 'judge0', fn: runJudge0 },
      { name: 'wandbox', fn: runWandbox }
    ];
    providers.sort((a, b) => (a.name === preferredProvider ? -1 : b.name === preferredProvider ? 1 : 0));
    const failures = [];
    for (const provider of providers) {
      for (let attempt = 0; attempt < 2; attempt++) {
        try {
          const result = await provider.fn(code, stdin, { timeout: opts.timeout || DEFAULT_TIMEOUT });
          preferredProvider = provider.name;
          return result;
        } catch (err) {
          failures.push((err && err.message) || String(err));
          if (attempt === 0) await sleep(450);
        }
      }
    }
    const detail = failures.length ? failures[failures.length - 1] : '未知网络错误';
    return {
      ok: false, compiled: false, phase: 'service', durationMs: 0,
      stdout: '', stderr: '', compilerOutput: '', compilerError: '', error:
        '在线编译服务暂时繁忙，已自动切换备用通道并重试，但仍未成功。\n服务反馈：' + detail +
        '\n请稍等几十秒再试；刷题、知识点与本地记录不受影响。'
    };
  }

  function compareOutput(actual, expected) { return normalizeOutput(actual) === normalizeOutput(expected); }

  async function judgeTests(code, tests, onProgress) {
    const results = [];
    for (let i = 0; i < tests.length; i++) {
      const t = tests[i];
      if (onProgress) onProgress(i, tests.length, t);
      const r = await runCpp(code, t.input || '');
      const passed = r.compiled && !r.stderr && compareOutput(r.stdout, t.output);
      results.push({ index: i, input: t.input || '', expected: t.output, actual: r.stdout, stderr: r.stderr, passed, run: r, hidden: !!t.hidden });
      if (!r.compiled) break;
    }
    const allPassed = results.length === tests.length && results.every(r => r.passed);
    return { allPassed, results };
  }

  window.CppSandbox = { runCpp, judgeTests, compareOutput, normalizeOutput, friendlyError, JUDGE0_URL, WANDBOX_URL, JUDGE0_LANG_ID };
})();

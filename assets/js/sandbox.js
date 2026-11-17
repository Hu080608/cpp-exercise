/* C++ 在线编译运行 —— 通过 Wandbox 公共编译 API（CORS 可用，无需自建后端）
 * 所有编译/运行在远端隔离环境中完成；本站仅发送源码与 stdin。
 */
(function () {
  'use strict';
  const WANDBOX_URL = 'https://wandbox.org/api/compile.json';
  const COMPILER = 'gcc-head';
  const TIMEOUT_MS = 45000;

  function normalizeOutput(s) {
    return String(s == null ? '' : s).replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n').map(line => line.replace(/[ \t]+$/g, '')).join('\n').replace(/\n+$/g, '');
  }

  function friendlyError(msg) {
    const text = String(msg || '');
    const lines = text.split('\n').filter(Boolean);
    const hints = [];
    if (/expected ['‘’]?;|expected ';'/.test(text)) hints.push('可能少写了分号；检查报错行及上一行的末尾。');
    if (/was not declared in this scope|undeclared/.test(text)) hints.push('使用了未声明/拼错的变量或函数；检查大小写、作用域与头文件。');
    if (/no matching function|invalid conversion|cannot convert/.test(text)) hints.push('参数或赋值类型不匹配，检查函数签名与变量类型。');
    if (/expected primary-expression|expected expression/.test(text)) hints.push('表达式不完整，检查括号、操作符两侧是否有操作数。');
    if (/redefinition|multiple definition/.test(text)) hints.push('同一作用域重复定义；检查是否重复包含了定义或函数体。');
    if (/No such file or directory/.test(text)) hints.push('头文件/源文件找不到，检查 #include 名称。');
    if (/expected unqualified-id/.test(text)) hints.push('可能是关键词被当作变量名，或括号配对错误。');
    if (/warning:/.test(text)) hints.push('编译通过但有警告，建议逐条检查警告信息。');
    return hints.length ? '可能的排查方向：\n' + hints.map((h, i) => (i + 1) + '. ' + h).join('\n') : '';
  }

  async function runCpp(code, stdin, opts) {
    opts = opts || {};
    if (!code || !String(code).trim()) {
      return { ok: false, phase: 'input', error: '代码为空。', stdout: '', stderr: '', compilerOutput: '', compilerError: '', durationMs: 0 };
    }
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), opts.timeout || TIMEOUT_MS);
    const started = performance.now();
    try {
      const body = {
        compiler: COMPILER,
        code: String(code),
        stdin: String(stdin == null ? '' : stdin),
        'compiler-option-raw': '-std=c++17',
        'runtime-option-raw': ''
      };
      const res = await fetch(WANDBOX_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
        signal: controller.signal
      });
      clearTimeout(timer);
      const durationMs = Math.round(performance.now() - started);
      if (!res.ok) throw new Error('编译服务返回 HTTP ' + res.status + '。请稍后重试。');
      const data = await res.json();
      const compilerError = data.compiler_error || '';
      const compilerOutput = data.compiler_output || '';
      const status = String(data.status == null ? '' : data.status);
      const compiled = !compilerError && status !== '1';
      const result = {
        ok: compiled && !data.program_error && status !== '1',
        compiled,
        phase: compiled ? 'run' : 'compile',
        stdout: data.program_output || '',
        stderr: data.program_error || '',
        compilerOutput,
        compilerError,
        status,
        signal: data.signal || '',
        durationMs,
        friendly: friendlyError(compilerError || data.program_error || compilerOutput)
      };
      if (!compiled) result.error = compilerError || compilerOutput || '编译失败。';
      else if (data.program_error) result.error = data.program_error;
      return result;
    } catch (err) {
      clearTimeout(timer);
      const aborted = err && err.name === 'AbortError';
      return {
        ok: false, compiled: false, phase: 'network', durationMs: Math.round(performance.now() - started),
        stdout: '', stderr: '', compilerOutput: '', compilerError: '',
        error: aborted ? '编译服务响应超时（45 秒）。请检查网络，或稍后再试。' : ('无法连接在线编译服务：' + (err && err.message ? err.message : '网络错误') + '。需要联网才能编译运行 C++。')
      };
    }
  }

  function compareOutput(actual, expected) {
    return normalizeOutput(actual) === normalizeOutput(expected);
  }

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

  window.CppSandbox = { runCpp, judgeTests, compareOutput, normalizeOutput, friendlyError, WANDBOX_URL, COMPILER };
})();

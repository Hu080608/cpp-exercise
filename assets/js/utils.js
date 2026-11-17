/* 通用工具：DOM、图标、存储、答案判分、弹层 */
(function () {
  'use strict';
  const U = {};
  const LETTERS = ['A','B','C','D','E','F','G','H'];
  U.LETTERS = LETTERS;
  U.esc = function (s) {
    return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  };
  U.attr = U.esc;
  U.icon = function (name, cls) {
    const p = U.ICONS[name] || U.ICONS.spark;
    return '<svg class="' + (cls || '') + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + p + '</svg>';
  };
  U.ICONS = {
    home: '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h5.5v-6h3v6H19V9.5"/>',
    book: '<path d="M4 4.5h11a3 3 0 0 1 3 3V20a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M4 4.5V20"/>',
    chart: '<path d="M4 20V10"/><path d="M10 20V4"/><path d="M16 20v-7"/><path d="M22 20H2"/>',
    gear: '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.9.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.9 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1A1.7 1.7 0 0 0 4.6 9a1.7 1.7 0 0 0-.3-1.9l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.9.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.9-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.9V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    x: '<path d="M18 6 6 18"/><path d="M6 6l12 12"/>',
    arrow: '<path d="M9 6l6 6-6 6"/>',
    back: '<path d="M15 18l-6-6 6-6"/>',
    play: '<path d="m8 5 11 7-11 7z"/>',
    code: '<path d="m8 8-5 4 5 4"/><path d="m16 8 5 4-5 4"/><path d="m14 4-4 16"/>',
    terminal: '<path d="m5 7 5 5-5 5"/><path d="M13 17h6"/>',
    search: '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.4-3.4"/>',
    filter: '<path d="M3 5h18"/><path d="M6 12h12"/><path d="M10 19h4"/>',
    target: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/>',
    fire: '<path d="M12 22c4 0 7-2.7 7-6.6 0-3-1.7-4.8-3-6.4-1-1.3-1.8-2.6-1.8-4.4C10.6 6.2 8.4 9 8.4 11c-1-.5-1.7-1.4-1.9-2.6C5.5 10 5 12 5 14.4 5 19 8 22 12 22z"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    bulb: '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2v.1h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>',
    star: '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L3 9.6l6.2-.9z"/>',
    refresh: '<path d="M21 12a9 9 0 1 1-2.6-6.4"/><path d="M21 3v6h-6"/>',
    trash: '<path d="M4 7h16"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M6 7l1 13h10l1-13"/><path d="M9 7V4h6v3"/>',
    download: '<path d="M12 3v12"/><path d="m7 11 5 5 5-5"/><path d="M4 20h16"/>',
    upload: '<path d="M12 16V4"/><path d="m7 8 5-5 5 5"/><path d="M4 20h16"/>',
    grid: '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    layers: '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 12 9 5 9-5"/><path d="m3 16 9 5 9-5"/>',
    spark: '<path d="m12 3 1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16v4"/><path d="M17 18h4"/>',
    arrowUp: '<path d="M12 19V5"/><path d="m6 11 6-6 6 6"/>',
    award: '<circle cx="12" cy="8" r="5"/><path d="m8.5 12-1.5 9 5-3 5 3-1.5-9"/>',
    doc: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/>',
    keyboard: '<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M7 14h10"/>',
    menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
    clock2: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    eye: '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    lock: '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    trophy: '<path d="M8 21h8"/><path d="M12 17v4"/><path d="M7 4h10v4a5 5 0 0 1-10 0z"/><path d="M7 5H4v2a3 3 0 0 0 3 3"/><path d="M17 5h3v2a3 3 0 0 1-3 3"/>',
    brain: '<path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0 0 6v1a3 3 0 0 0 3 3h1V4z"/><path d="M15 21a3 3 0 0 0 3-3v-1a3 3 0 0 0 0-6V9a3 3 0 0 0-3-3h-1v15z"/>',
    link: '<path d="M10 13a5 5 0 0 0 7.5.5l2-2a5 5 0 0 0-7-7l-1.2 1.2"/><path d="M14 11a5 5 0 0 0-7.5-.5l-2 2a5 5 0 0 0 7 7l1.2-1.2"/>'
  };
  U.byId = id => document.getElementById(id);
  U.qs = (sel, root) => (root || document).querySelector(sel);
  U.qsa = (sel, root) => Array.from((root || document).querySelectorAll(sel));
  U.on = (el, ev, fn, opts) => el && el.addEventListener(ev, fn, opts);
  U.debounce = function (fn, wait) { let t; return function () { const a = arguments, c = this; clearTimeout(t); t = setTimeout(() => fn.apply(c, a), wait); }; };
  U.shuffle = function (arr) { const a = arr.slice(); for (let i=a.length-1;i>0;i--) { const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; };
  U.clamp = (n, a, b) => Math.max(a, Math.min(b, n));
  U.pct = (a, b) => b > 0 ? Math.round(a / b * 100) : 0;
  U.formatTime = function (sec) { sec = Math.max(0, Math.round(sec || 0)); const m = Math.floor(sec/60), s = sec%60; return (m ? m + ' 分 ' : '') + s + ' 秒'; };
  U.dateKey = function (d) { d = d || new Date(); const p = n => String(n).padStart(2,'0'); return d.getFullYear()+'-'+p(d.getMonth()+1)+'-'+p(d.getDate()); };
  U.shortDate = function (ts) { if (!ts) return ''; const d = new Date(ts); return (d.getMonth()+1)+'/'+d.getDate(); };
  U.relativeTime = function (ts) { if (!ts) return '—'; const diff = Date.now()-ts, min=60000, hour=3600000, day=86400000; if (diff<min) return '刚刚'; if (diff<hour) return Math.floor(diff/min)+' 分钟前'; if (diff<day) return Math.floor(diff/hour)+' 小时前'; if (diff<day*7) return Math.floor(diff/day)+' 天前'; return U.shortDate(ts); };
  U.toast = function (msg, kind) {
    let el = document.getElementById('toast');
    if (!el) { el = document.createElement('div'); el.id = 'toast'; el.setAttribute('role','status'); document.body.appendChild(el); }
    el.className = 'toast' + (kind ? ' ' + kind : '');
    el.textContent = msg; el.classList.add('show'); clearTimeout(U._toastTimer);
    U._toastTimer = setTimeout(() => el.classList.remove('show'), 2400);
  };
  U.modal = function (html, opts) {
    opts = opts || {};
    const wrap = document.createElement('div'); wrap.className = 'modal-backdrop'; wrap.setAttribute('role','dialog'); wrap.setAttribute('aria-modal','true');
    wrap.innerHTML = '<div class="modal"><div class="row" style="margin-bottom:12px"><div style="flex:1"></div><button class="icon-btn modal-close" aria-label="关闭">' + U.icon('x') + '</button></div>' + html + '</div>';
    document.body.appendChild(wrap);
    const close = () => { wrap.remove(); document.removeEventListener('keydown', onKey); };
    function onKey(e) { if (e.key === 'Escape') close(); }
    U.qs('.modal-close', wrap).addEventListener('click', close);
    wrap.addEventListener('click', e => { if (e.target === wrap) close(); });
    document.addEventListener('keydown', onKey);
    return { el: wrap, close };
  };
  U.confirm = function (title, message) {
    return new Promise(resolve => {
      const m = U.modal('<h2>' + U.esc(title) + '</h2><p class="lede" style="font-size:13.5px;margin:8px 0 20px">' + U.esc(message) + '</p><div class="row" style="justify-content:flex-end"><button class="btn btn-ghost" data-act="cancel">取消</button><button class="btn btn-primary" data-act="ok">确认</button></div>');
      m.el.querySelector('[data-act="cancel"]').onclick = () => { m.close(); resolve(false); };
      m.el.querySelector('[data-act="ok"]').onclick = () => { m.close(); resolve(true); };
    });
  };
  U.store = {
    get(key, fallback) { try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; } catch(e) { return fallback; } },
    set(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch(e) { return false; } },
    del(key) { try { localStorage.removeItem(key); } catch(e) {} }
  };
  window.CppU = U;
})();
/* 答案判分（填空做安全的等价归一化） */
(function (U) {
  'use strict';
  const FULL = { '＜':'<','＞':'>','（':'(','）':')','＝':'=','；':';','：':':','，':',','！':'!','＆':'&','｜':'|','＂':'"','＇':"'",'＋':'+','－':'-','＊':'*','／':'/','％':'%','＿':'_','｛':'{','｝':'}','［':'[','］':']','＃':'#','＠':'@','＾':'^','～':'~','＼':String.fromCharCode(92),'　':' ','“':'"','”':'"','‘':"'",'’':"'",'。':'.','、':',' };
  function halfWidth(s) { let out=''; for (const c of String(s)) out += (FULL[c] !== undefined ? FULL[c] : c); return out; }
  function splitTop(s, sep) {
    const parts=[]; let cur='', depth=0;
    for (let i=0;i<s.length;i++) {
      const c=s[i];
      if (c==='('||c==='[') { depth++; cur+=c; continue; }
      if (c===')'||c===']') { depth--; cur+=c; continue; }
      if (depth===0 && s.startsWith(sep,i)) { parts.push(cur); cur=''; i+=sep.length-1; continue; }
      cur+=c;
    }
    parts.push(cur); return parts;
  }
  function normalizeLogical(s) {
    // 仅对顶层 && / || 的操作数做排序；不展开括号，不改变语义。
    const ors = splitTop(s, '||');
    if (ors.length > 1) return ors.map(normalizeLogical).sort().join('||');
    const ands = splitTop(s, '&&');
    if (ands.length > 1) return ands.map(normalizeLogical).sort().join('&&');
    return s;
  }
  U.fillKey = function (s) {
    let t = halfWidth(s).replace(/\s+/g,'').replace(/[;；]+$/,'');
    if (!t) return '';
    t = t.replace(/std::/g,'');
    t = t.replace(/static_cast<double>\(([A-Za-z_][\w.\[\]]*)\)/g,'#dbl($1)');
    t = t.replace(/\(double\)([A-Za-z_][\w.\[\]]*)/g,'#dbl($1)');
    t = t.replace(/\bdouble\(([A-Za-z_][\w.\[\]]*)\)/g,'#dbl($1)');
    t = t.replace(/\b1\.0\*([A-Za-z_][\w.\[\]]*)/g,'#dbl($1)');
    t = t.replace(/([A-Za-z_][\w.\[\]]*)\*1\.0\b/g,'#dbl($1)');
    t = normalizeLogical(t);
    t = t.replace(/(\d+\.\d*?)0+(?=\D|$)/g,'$1').replace(/\.$/,'');
    return t;
  };
  U.grade = function (q, resp) {
    if (resp == null) return false;
    if (q.type === 'single' || q.type === 'code') return resp === q.answer;
    if (q.type === 'judge') return resp === q.answer;
    if (q.type === 'multiple') {
      if (!Array.isArray(resp) || !Array.isArray(q.answer) || resp.length !== q.answer.length) return false;
      const a = resp.slice().sort(), b = q.answer.slice().sort();
      return a.every((x,i)=>x===b[i]);
    }
    if (q.type === 'fill') {
      if (!Array.isArray(resp) || !Array.isArray(q.answer) || resp.length !== q.answer.length) return false;
      return q.answer.every((ans,i)=>{
        const got = U.fillKey(resp[i]);
        if (!got) return false;
        if (got === U.fillKey(ans)) return true;
        const alts = (q.alt && q.alt[i]) || [];
        return alts.some(a => U.fillKey(a) === got);
      });
    }
    return false;
  };
  U.answerText = function (q) {
    if (q.type === 'single' || q.type === 'code') return U.LETTERS[q.answer] + '. ' + ((q.options||[])[q.answer] || '');
    if (q.type === 'multiple') return (q.answer||[]).slice().sort().map(i => U.LETTERS[i] + '. ' + ((q.options||[])[i]||'')).join('；');
    if (q.type === 'judge') return q.answer ? '正确' : '错误';
    if (q.type === 'fill') return (q.answer||[]).map((a,i)=>'第 '+(i+1)+' 空：'+a).join('；');
    if (q.type === 'programming') return '通过全部测试用例';
    return '';
  };
})(window.CppU);
/* 编程题参考解展示：轻量 C++ 格式化 + 复制 */
(function (U) {
  'use strict';
  U.formatCpp = function (source) {
    const text = String(source == null ? '' : source).replace(/\r/g, '');
    let out = '', indent = 0, paren = 0, quote = null, escaped = false, needIndent = false;
    function newline() { out = out.replace(/[ \t]+$/,'') + '\n'; needIndent = true; }
    function emit(str) {
      if (needIndent) { out += '    '.repeat(Math.max(0, indent)); needIndent = false; }
      out += str;
    }
    function isBlockBrace(i) {
      let j = i - 1;
      while (j >= 0 && /\s/.test(text[j])) j--;
      const prev = j >= 0 ? text[j] : '';
      return prev !== '=' && prev !== ',' && prev !== '[' && prev !== '{';
    }
    for (let i = 0; i < text.length; i++) {
      const c = text[i];
      if (quote) {
        emit(c);
        if (escaped) escaped = false;
        else if (c === String.fromCharCode(92)) escaped = true;
        else if (c === quote) quote = null;
        continue;
      }
      if (c === '"' || c === "'") { quote = c; emit(c); continue; }
      if (c === '\n') { if (!out.endsWith('\n')) newline(); else needIndent = true; continue; }
      if (c === ' ' || c === '\t') {
        if (!needIndent && out && !out.endsWith(' ') && !out.endsWith('\n') && !'([{;,)}'.includes(out[out.length - 1])) emit(' ');
        continue;
      }
      if (c === '(') { paren++; emit(c); continue; }
      if (c === ')') { paren = Math.max(0, paren - 1); emit(c); continue; }
      if (c === ';' && paren === 0) { emit(';'); newline(); continue; }
      if (c === '{' && isBlockBrace(i)) {
        if (out && !out.endsWith(' ') && !out.endsWith('\n')) emit(' ');
        emit('{'); newline(); indent++; needIndent = true; continue;
      }
      if (c === '}') {
        if (!out.endsWith('\n')) newline();
        indent = Math.max(0, indent - 1);
        emit('}');
        let j = i + 1;
        while (j < text.length && text[j] === ' ') j++;
        if (text[j] === ';') { emit(';'); newline(); i = j; }
        else newline();
        continue;
      }
      emit(c);
    }
    return out.replace(/\n{3,}/g, '\n\n').trim() + '\n';
  };

  U.copyText = async function (text) {
    const value = String(text == null ? '' : text);
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(value);
      } else {
        const ta = document.createElement('textarea');
        ta.value = value;
        ta.style.cssText = 'position:fixed;left:-9999px;top:0;opacity:0';
        document.body.appendChild(ta);
        ta.focus(); ta.select();
        const ok = document.execCommand('copy');
        ta.remove();
        if (!ok) throw new Error('copy failed');
      }
      U.toast('✓ 参考解已复制', 'ok');
      return true;
    } catch (e) {
      U.toast('复制失败，请手动选中代码复制', 'bad');
      return false;
    }
  };
})(window.CppU);

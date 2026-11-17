/* C++ Lab — main app */
(function () {
  'use strict';
  const U = window.CppU;
  const SAND = window.CppSandbox;
  const KNOWLEDGE = window.CPP_KNOWLEDGE || [];
  const DOWNLOADS = window.CPP_DOWNLOADS || [];
  const STORE_KEY = 'cpplab.v2';
  const CHAPTER_TITLES = {
    1: { title: '程序和 C++ 基础', short: '程序基础', desc: '计算机组成、数制、程序设计语言与 C++ 词法', accent: 'green' },
    2: { title: '数据与表达式', short: '数据表达式', desc: '基本类型、常量变量、输入输出、运算与类型转换', accent: 'coral' },
    3: { title: '流程控制', short: '流程控制', desc: '顺序、选择、循环、转移语句与程序风格', accent: 'blue' },
    4: { title: '函数与过程抽象', short: '函数抽象', desc: '函数、作用域、递归、重载、Lambda 与动态内存', accent: 'gold' },
    5: { title: '复合数据类型', short: '复合数据', desc: '枚举、数组、字符串、结构体、指针、链表与引用', accent: 'green' }
  };
  const TYPE_LABEL = { single:'单选', multiple:'多选', judge:'判断', fill:'填空', code:'代码阅读', programming:'编程' };
  const DIFF_LABEL = { 1:'入门', 2:'简单', 3:'中等', 4:'困难' };
  const DIFF_CLASS = { 1:'ok', 2:'accent', 3:'gold', 4:'bad' };
  const TYPE_ICON = { single:'target', multiple:'layers', judge:'check', fill:'keyboard', code:'code', programming:'terminal' };

  let QUESTIONS = [], QID = {}, TOPICS = {}, MANIFEST = { count: 0 };
  let route = parseHash();
  let practiceFilter = { chapter:'all', topic:'all', type:'all', diff:'all', status:'all', q:'' };
  let pendingProgram = {};
  let currentQuestionStarted = Date.now();
  let currentQuestionId = null;

  const DEFAULT_STATE = {
    version: 2,
    records: {}, favorites: [], activity: {}, drafts: {},
    settings: { theme:'system', autoNext:false, showSource:true, motion:true, dailyGoal:20, lineWrap:false },
    session: null,
    lastPractice: null,
    createdAt: Date.now()
  };
  let state = loadState();
  function loadState() {
    const raw = U.store.get(STORE_KEY, null);
    if (!raw || typeof raw !== 'object') return JSON.parse(JSON.stringify(DEFAULT_STATE));
    const s = Object.assign({}, JSON.parse(JSON.stringify(DEFAULT_STATE)), raw);
    s.records = raw.records || {}; s.favorites = Array.isArray(raw.favorites) ? raw.favorites : [];
    s.activity = raw.activity || {}; s.drafts = raw.drafts || {};
    s.settings = Object.assign({}, DEFAULT_STATE.settings, raw.settings || {});
    return s;
  }
  let saveTimer = null;
  function save(now) {
    if (saveTimer) clearTimeout(saveTimer);
    const fn = () => { U.store.set(STORE_KEY, state); saveTimer = null; };
    if (now) fn(); else saveTimer = setTimeout(fn, 140);
  }
  function applyTheme() {
    const t = state.settings.theme || 'system';
    const dark = t === 'dark' || (t === 'system' && window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches);
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    document.documentElement.dataset.motion = state.settings.motion ? 'on' : 'off';
  }
  window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', applyTheme);

  function parseHash() {
    const raw = (location.hash || '#/home').replace(/^#\/?/, '').split('?')[0];
    const parts = raw.split('/').filter(Boolean);
    if (!parts.length) return { name:'home', params:{} };
    const name = parts[0];
    const params = {};
    if (name === 'chapter') params.ch = Number(parts[1]) || 1;
    if (name === 'topic') params.id = decodeURIComponent(parts[1] || '');
    if (name === 'sandbox') params.qid = parts[1] || '';
    return { name, params };
  }
  function go(path) { location.hash = path.startsWith('#') ? path : '#/' + path; }
  function navTo(name) { go(name); }
  function activeNav() {
    if (['home'].includes(route.name)) return 'home';
    if (['practice','chapter','topic','quiz'].includes(route.name)) return 'practice';
    if (['knowledge'].includes(route.name)) return 'knowledge';
    if (['stats'].includes(route.name)) return 'stats';
    if (['wrong','favorites'].includes(route.name)) return 'wrong';
    if (['sandbox'].includes(route.name)) return 'sandbox';
    if (['settings','docs'].includes(route.name)) return 'settings';
    return 'home';
  }
  function pageShell(content, opts) {
    opts = opts || {};
    const active = opts.active || activeNav();
    const navItems = [
      { key:'home', label:'首页', icon:'home' }, { key:'practice', label:'题库', icon:'book' },
      { key:'knowledge', label:'知识点', icon:'brain' }, { key:'stats', label:'统计', icon:'chart' },
      { key:'sandbox', label:'沙箱', icon:'terminal' }, { key:'wrong', label:'错题', icon:'fire' }
    ];
    const top = '<div class="shell topnav-inner"><a class="brand" href="#/home" aria-label="C++ Lab 首页"><span class="brand-mark">&lt;/&gt;</span><span><span class="brand-name">C++ Lab</span><span class="brand-sub">PROGRAMMING PRACTICE</span></span></a>' +
      '<nav class="nav-links" aria-label="主导航">' + navItems.map(n => '<a class="nav-link ' + (active===n.key?'active':'') + '" href="#/' + n.key + '">' + n.label + '</a>').join('') + '</nav>' +
      '<div class="nav-actions"><button class="icon-btn" data-action="open-search" title="搜索题目 (/)">' + U.icon('search') + '</button>' +
      '<button class="icon-btn" data-action="toggle-theme" title="切换主题">' + U.icon(state.settings.theme==='dark'?'bulb':'moon') + '</button>' +
      '<button class="icon-btn" data-nav="settings" data-action="open-settings" title="设置">' + U.icon('gear') + '</button></div></div>';
    const tab = '<nav class="mobile-tabbar" aria-label="移动端导航">' + navItems.map(n => '<button class="' + (active===n.key?'active':'') + '" data-action="tab" data-tab="' + n.key + '">' + U.icon(n.icon) + '<span>' + n.label + '</span></button>').join('') + '</nav>';
    return '<header class="topnav" id="topnav">' + top + '</header><main class="page fade-in" id="page">' + content + '</main>' + tab;
  }
  const ICON_MOON = '<path d="M20.5 14.2A8.5 8.5 0 0 1 9.8 3.5 8.5 8.5 0 1 0 20.5 14.2z"/>';
  U.ICONS.moon = ICON_MOON;
  function emptyState(icon, title, text, actionHtml) {
    return '<div class="empty"><div class="empty-ic">' + U.icon(icon) + '</div><h3>' + U.esc(title) + '</h3><p>' + U.esc(text) + '</p>' + (actionHtml || '') + '</div>';
  }
  function ringSvg(pct, label) {
    const r = 38, c = 2 * Math.PI * r, off = c * (1 - U.clamp(pct,0,100)/100);
    return '<div class="ring"><svg width="82" height="82" viewBox="0 0 88 88"><circle class="ring-bg" cx="44" cy="44" r="' + r + '"/><circle class="ring-fg" cx="44" cy="44" r="' + r + '" stroke-dasharray="' + c.toFixed(1) + '" stroke-dashoffset="' + off.toFixed(1) + '"/></svg><div class="ring-label"><b>' + Math.round(pct) + '%</b><span>' + U.esc(label||'已练') + '</span></div></div>';
  }
  function pctBar(a,b) { return '<div class="progress"><i style="width:' + U.pct(a,b) + '%"></i></div>'; }

  /* ---------- data / progress ---------- */
  async function loadData() {
    const base = new URL('./data/questions/', document.baseURI);
    const man = await fetch(new URL('manifest.json', base)).then(r => { if (!r.ok) throw new Error('manifest'); return r.json(); });
    MANIFEST = man;
    const lists = await Promise.all(man.chapters.map(ch => fetch(new URL('ch' + ch + '.json', base)).then(r => { if (!r.ok) throw new Error('chapter ' + ch); return r.json(); })));
    QUESTIONS = lists.flatMap(x => x.questions);
    QUESTIONS.forEach(q => { QID[q.id] = q; });
    KNOWLEDGE.forEach(k => {
      k.questions = QUESTIONS.filter(q => q.topicId === k.id);
      TOPICS[k.id] = k;
    });
  }
  function recOf(id) { return state.records[id] || null; }
  function isDone(id) { const r = recOf(id); return !!(r && r.attempts > 0); }
  function inWrongBook(id) { const r = recOf(id); return !!(r && r.wrong > 0 && (r.streak || 0) < 2); }
  function questionStatus(id) {
    const r = recOf(id);
    if (!r || !r.attempts) return { key:'new', label:'未做', cls:'' };
    if (r.streak >= 2) return { key:'mastered', label:'已掌握', cls:'ok' };
    if (r.lastOk) return { key:'learning', label:'待巩固', cls:'gold' };
    return { key:'wrong', label:'待复习', cls:'bad' };
  }
  function isFav(id) { return state.favorites.includes(id); }
  function globalStats() {
    let done = 0, mastered = 0, correct = 0, attempts = 0, wrong = 0, time = 0;
    QUESTIONS.forEach(q => {
      const r = recOf(q.id); if (!r) return;
      if (r.attempts > 0) { done++; attempts += r.attempts; correct += r.correct || 0; wrong += r.wrong || 0; time += r.timeMs || 0; if ((r.streak || 0) >= 2) mastered++; }
    });
    return { total: QUESTIONS.length, done, mastered, correct, attempts, wrong, time, accuracy: attempts ? U.pct(correct, attempts) : 0, wrongCount: QUESTIONS.filter(q => inWrongBook(q.id)).length };
  }
  function chapterStats(ch) {
    const qs = QUESTIONS.filter(q => q.chapter === ch);
    let done=0, ok=0, attempts=0, correct=0, time=0, mastered=0;
    qs.forEach(q => { const r=recOf(q.id); if (r && r.attempts) { done++; attempts+=r.attempts; correct+=r.correct||0; time+=r.timeMs||0; if ((r.streak||0)>=2) mastered++; if (r.lastOk) ok++; } });
    return { total:qs.length, done, ok, attempts, correct, time, mastered, accuracy:attempts?U.pct(correct,attempts):0 };
  }
  function topicStats(topicId) {
    const qs = QUESTIONS.filter(q => q.topicId === topicId);
    let done=0, attempts=0, correct=0, wrong=0;
    qs.forEach(q => { const r=recOf(q.id); if(r&&r.attempts){done++;attempts+=r.attempts;correct+=r.correct||0;wrong+=r.wrong||0;} });
    return { total:qs.length, done, attempts, correct, wrong, accuracy:attempts?U.pct(correct,attempts):0 };
  }
  function smartPool(n) {
    const newQs = QUESTIONS.filter(q => !isDone(q.id));
    const review = QUESTIONS.filter(q => inWrongBook(q.id));
    const weak = QUESTIONS.filter(q => { const r=recOf(q.id); return r && r.attempts && !r.lastOk; });
    const rest = QUESTIONS.filter(q => isDone(q.id) && !inWrongBook(q.id));
    const pool = [...U.shuffle(review), ...U.shuffle(newQs), ...U.shuffle(weak), ...U.shuffle(rest)];
    const out=[]; const seen=new Set();
    for (const q of pool) { if (!seen.has(q.id)) { out.push(q); seen.add(q.id); } if (out.length >= n) break; }
    return out;
  }
  function activitySeries(days) {
    const out = []; const now = new Date();
    for (let i=days-1;i>=0;i--) { const d=new Date(now); d.setDate(now.getDate()-i); const key=U.dateKey(d); out.push({ key, date:d, data:state.activity[key]||{answered:0,correct:0,seconds:0} }); }
    return out;
  }
  function streakDays() {
    let streak = 0; const d = new Date();
    for (;;) { const key=U.dateKey(d); if ((state.activity[key]?.answered||0)>0) { streak++; d.setDate(d.getDate()-1); } else break; }
    return streak;
  }
  function dailyProgress() { const a=state.activity[U.dateKey()]||{answered:0,correct:0,seconds:0}; return { ...a, goal:state.settings.dailyGoal||20 }; }
  function addActivity(ok, timeMs) {
    const key=U.dateKey(); const a=state.activity[key]||{answered:0,correct:0,seconds:0};
    a.answered++; if (ok) a.correct++; a.seconds += Math.round((timeMs||0)/1000); state.activity[key]=a;
  }
  function recordAttempt(q, ok, answer, elapsedMs) {
    const old = state.records[q.id] || { attempts:0, correct:0, wrong:0, streak:0, lastAt:0, lastOk:false, timeMs:0 };
    old.attempts++; old.correct = (old.correct||0) + (ok?1:0); old.wrong = (old.wrong||0) + (ok?0:1);
    old.streak = ok ? (old.streak||0)+1 : 0;
    old.lastOk = !!ok; old.lastAt = Date.now(); old.lastAnswer = answer; old.timeMs = (old.timeMs||0) + Math.max(0, elapsedMs||0);
    state.records[q.id] = old; addActivity(ok, elapsedMs); save();
  }
  function isAnswerCorrect(q, value) {
    if (value === undefined || value === null || value === '__revealed__') return false;
    if (q.type === 'programming') return true;
    return U.grade(q, value);
  }
  function updateLastPractice() {
    const s = state.session; if (!s) return;
    const answered = s.qids.filter(id => s.answers[id] !== undefined);
    let ok=0; answered.forEach(id => { if (isAnswerCorrect(QID[id], s.answers[id])) ok++; });
    state.lastPractice = { title:s.title, qids:s.qids.slice(), answered:answered.length, ok, startedAt:s.startedAt, at:Date.now() };
  }

  /* ---------- home ---------- */
  function quickCard(action, icon, title, sub) {
    return '<button class="quick-card" data-action="' + action + '"><div class="quick-icon">' + U.icon(icon) + '</div><div class="quick-title">' + U.esc(title) + '</div><div class="quick-sub">' + U.esc(sub) + '</div></button>';
  }
  function renderHome() {
    const g = globalStats(), d = dailyProgress(), streak = streakDays();
    const donePct = U.pct(g.done, g.total);
    const recentWrong = QUESTIONS.filter(q => inWrongBook(q.id)).sort((a,b)=>(recOf(b.id)?.lastAt||0)-(recOf(a.id)?.lastAt||0)).slice(0,4);
    const chapterCards = [1,2,3,4,5].map(ch => {
      const s = chapterStats(ch), meta = CHAPTER_TITLES[ch];
      return '<a class="chapter-card" href="#/chapter/' + ch + '"><div class="chapter-num">0' + ch + '</div><div><div class="chapter-title">' + U.esc(meta.title) + '</div><div class="chapter-meta">' + s.total + ' 题 · 已完成 ' + s.done + ' · 正确率 ' + (s.attempts ? s.accuracy + '%' : '—') + '</div><div style="margin-top:8px">' + pctBar(s.done, s.total) + '</div></div><span class="chapter-arrow">' + U.icon('arrow') + '</span></a>';
    }).join('');
    const topics = KNOWLEDGE.map(k => ({ k, s: topicStats(k.id) })).filter(x => x.s.attempts > 0).sort((a,b)=>a.s.accuracy-b.s.accuracy || b.s.attempts-a.s.attempts).slice(0,4);
    const topicHtml = topics.length ? topics.map(({k,s}) => '<div class="topic-row"><div><h4>' + U.esc(k.title) + '</h4><p>第 ' + k.chapter + ' 章 · 已做 ' + s.done + '/' + s.total + ' 题</p></div><span class="pill ' + (s.accuracy>=80?'ok':s.accuracy>=60?'gold':'bad') + '">' + s.accuracy + '%</span></div>').join('') : '<div class="empty" style="padding:24px 8px"><p>做几道题后，这里会指出你最该复习的知识点。</p></div>';
    const todayTip = ['先后看规则，再读代码：先判断考的是类型、优先级还是控制流。','填空题先写最小正确形式，不必背冗长表达式。','错题连续答对两次才会移出错题本，别靠一次记忆。','编程题先跑通样例，再提交全部测试。'][new Date().getDate() % 4];
    const recents = (state.lastPractice && state.lastPractice.answered) ? '<div class="card" style="margin-top:14px"><div class="card-head"><div><h3>继续上次练习</h3><p>' + U.esc(state.lastPractice.title) + ' · 已做 ' + state.lastPractice.answered + '/' + state.lastPractice.qids.length + ' 题</p></div><button class="btn btn-soft btn-sm" data-action="resume-last">继续</button></div><div class="progress"><i style="width:' + U.pct(state.lastPractice.answered, state.lastPractice.qids.length) + '%"></i></div></div>' : '';
    const content = '<div class="home-grid"><div>' +
      '<section class="hero"><div class="row between" style="align-items:flex-start"><div><div class="kicker" style="color:rgba(255,255,255,.72)">AUTUMN SEMESTER · C++</div><h1>把“看得懂”变成<br><em style="color:#fff">写得对、跑得通。</em></h1><p>297 道题覆盖 PPT 第 1–5 章，六种题型、四档难度，配合真正能编译运行的 C++ 沙箱。</p></div>' + ringSvg(donePct, '已练') + '</div><div class="hero-stats"><div class="hero-stat"><b>' + g.done + '<span style="font-size:13px;opacity:.65"> / ' + g.total + '</span></b><span>已做题数</span></div><div class="hero-stat"><b>' + g.accuracy + '%</b><span>累计正确率</span></div><div class="hero-stat"><b>' + streak + '</b><span>连续学习天数</span></div><div class="hero-stat"><b>' + g.wrongCount + '</b><span>待复习错题</span></div></div></section>' +
      '<div class="section-head"><h2>今天从哪儿开始？</h2><span class="hint">推荐按“新题 → 错题 → 弱项”循环</span></div><div class="quick-grid">' +
        quickCard('start-smart','spark','智能练习 20 题','优先新题与到期错题') + quickCard('start-wrong','fire', g.wrongCount ? '错题重练 · ' + g.wrongCount + ' 题' : '错题重练', g.wrongCount ? '连续答对 2 次移出' : '错题本是空的，保持住') + quickCard('open-sandbox','terminal','打开 C++ 沙箱','写代码，真实编译运行') +
      '</div>' + recents +
      '<div class="section-head"><h2>按章节推进</h2><a href="#/practice">查看全部题库 →</a></div><div class="chapter-grid">' + chapterCards + '</div>' +
      '<div class="section-head"><h2>最该补的知识点</h2><a href="#/knowledge">知识点地图 →</a></div><div class="card" style="padding:8px 20px"><div class="topic-list">' + topicHtml + '</div></div>' +
      '</div><aside>' +
      '<div class="card"><div class="card-head"><div><h3>今日目标</h3><p>' + U.esc(todayTip) + '</p></div><span class="pill accent">' + d.answered + ' / ' + d.goal + '</span></div><div class="progress gold"><i style="width:' + U.pct(d.answered,d.goal) + '%"></i></div><div class="row between" style="margin-top:12px"><span class="small muted">' + (d.answered>=d.goal?'目标完成，去挑战困难题吧':('还差 ' + (d.goal-d.answered) + ' 题完成今日目标')) + '</span><button class="btn btn-soft btn-sm" data-action="change-goal">调整</button></div></div>' +
      '<div class="card" style="margin-top:14px"><div class="card-head"><div><h3>最近错题</h3><p>按最近作答时间排序</p></div><a href="#/wrong" class="small">全部</a></div>' + (recentWrong.length ? recentWrong.map(q => '<button class="q-list-item" style="grid-template-columns:minmax(0,1fr) auto;padding:11px 0;border-width:0 0 1px;border-radius:0;background:none" data-action="practice-one" data-id="' + q.id + '"><div><div class="q-list-stem" style="font-size:12.5px">' + U.esc(q.stem) + '</div><div class="q-list-meta"><span class="pill">' + TYPE_LABEL[q.type] + '</span><span class="tiny muted">第' + q.chapter + '章 · ' + DIFF_LABEL[q.difficulty] + '</span></div></div><span class="q-status bad"></span></button>').join('') : '<p class="small muted">暂无错题，继续按节奏练习。</p>') + '</div>' +
      '<div class="card" style="margin-top:14px"><div class="row wrap"><span class="pill blue">沙箱在线</span><span class="pill">GCC · C++17</span></div><h3 style="font-size:16px;margin-top:12px">代码不是看起来对，<br>而是跑起来对。</h3><p class="small muted" style="margin-top:7px;line-height:1.7">编辑器 + stdin + 编译错误诊断，支持把编程题初始代码一键载入。</p><button class="btn btn-primary btn-block" style="margin-top:14px" data-action="open-sandbox">' + U.icon('play') + '进入沙箱</button></div>' +
      '</aside></div>';
    return pageShell(content);
  }

  /* ---------- practice hub ---------- */
  function filterQuestions() {
    const f = practiceFilter;
    return QUESTIONS.filter(q => {
      if (f.chapter !== 'all' && q.chapter !== Number(f.chapter)) return false;
      if (f.topic !== 'all' && q.topicId !== f.topic) return false;
      if (f.type !== 'all' && q.type !== f.type) return false;
      if (f.diff !== 'all' && q.difficulty !== Number(f.diff)) return false;
      if (f.q) { const s = (q.stem + ' ' + (q.options||[]).join(' ') + ' ' + (q.knowledge||'') + ' ' + (q.source||'')).toLowerCase(); if (!s.includes(f.q.toLowerCase())) return false; }
      if (f.status === 'new' && isDone(q.id)) return false;
      if (f.status === 'wrong' && !inWrongBook(q.id)) return false;
      if (f.status === 'fav' && !isFav(q.id)) return false;
      if (f.status === 'done' && !isDone(q.id)) return false;
      if (f.status === 'mastered' && questionStatus(q.id).key !== 'mastered') return false;
      return true;
    });
  }
  function topicOptions(selected) {
    return '<option value="all">全部知识点</option>' + KNOWLEDGE.map(k => '<option value="' + U.attr(k.id) + '" ' + (selected===k.id?'selected':'') + '>第' + k.chapter + '章 · ' + U.esc(k.title) + '</option>').join('');
  }
  function practiceListHtml(list) {
    if (!list.length) return emptyState('search','没有匹配的题目','试着放宽筛选条件，或清空关键词后重新查找。','<button class="btn btn-ghost btn-sm" style="margin-top:14px" data-action="clear-filters">清空筛选</button>');
    return '<div class="question-list">' + list.map(q => {
      const st = questionStatus(q.id);
      return '<button class="q-list-item" data-action="practice-one" data-id="' + q.id + '"><span class="q-index">' + q.id.replace('q','#') + '</span><div><div class="q-list-stem">' + U.esc(q.stem) + '</div><div class="q-list-meta"><span class="pill ' + DIFF_CLASS[q.difficulty] + '">' + DIFF_LABEL[q.difficulty] + '</span><span class="pill">' + TYPE_LABEL[q.type] + '</span><span class="tiny muted">第' + q.chapter + '章 · ' + U.esc(q.knowledge) + '</span></div></div><span class="q-status ' + (st.cls==='ok'?'ok':st.cls==='bad'?'bad':'') + '"></span></button>';
    }).join('') + '</div>';
  }
  function renderPractice() {
    const list = filterQuestions();
    const activeFilters = ['chapter','topic','type','diff','status'].filter(k=>practiceFilter[k]!=='all').length + (practiceFilter.q?1:0);
    const counts = { total:QUESTIONS.length, single:QUESTIONS.filter(q=>q.type==='single').length, multiple:QUESTIONS.filter(q=>q.type==='multiple').length, judge:QUESTIONS.filter(q=>q.type==='judge').length, fill:QUESTIONS.filter(q=>q.type==='fill').length, code:QUESTIONS.filter(q=>q.type==='code').length, programming:QUESTIONS.filter(q=>q.type==='programming').length };
    const content = '<div class="row between wrap" style="margin-bottom:18px"><div><div class="kicker">QUESTION BANK · 297 QUESTIONS</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">题库<br><em>按你的薄弱点来。</em></h1></div><div class="row wrap"><span class="pill accent">' + counts.single + ' 单选</span><span class="pill coral">' + counts.multiple + ' 多选</span><span class="pill blue">' + counts.judge + ' 判断</span><span class="pill gold">' + counts.fill + ' 填空</span><span class="pill">' + counts.code + ' 代码阅读</span><span class="pill">' + counts.programming + ' 编程</span></div></div>' +
      '<div class="filter-panel"><div class="filter-grid">' +
        '<label class="field"><span>章节</span><select class="select" data-filter="chapter"><option value="all">全部章节</option>' + [1,2,3,4,5].map(c=>'<option value="'+c+'" '+(String(practiceFilter.chapter)===String(c)?'selected':'')+'>第'+c+'章 '+U.esc(CHAPTER_TITLES[c].title)+'</option>').join('') + '</select></label>' +
        '<label class="field"><span>知识点</span><select class="select" data-filter="topic">' + topicOptions(practiceFilter.topic) + '</select></label>' +
        '<label class="field"><span>题型</span><select class="select" data-filter="type"><option value="all">全部题型</option>' + Object.keys(TYPE_LABEL).map(t=>'<option value="'+t+'" '+(practiceFilter.type===t?'selected':'')+'>'+TYPE_LABEL[t]+'</option>').join('') + '</select></label>' +
        '<label class="field"><span>难度</span><select class="select" data-filter="diff"><option value="all">全部难度</option>' + [1,2,3,4].map(d=>'<option value="'+d+'" '+(String(practiceFilter.diff)===String(d)?'selected':'')+'>'+DIFF_LABEL[d]+'</option>').join('') + '</select></label>' +
        '<label class="field"><span>状态</span><select class="select" data-filter="status"><option value="all">全部状态</option><option value="new" '+(practiceFilter.status==='new'?'selected':'')+'>未做</option><option value="done" '+(practiceFilter.status==='done'?'selected':'')+'>已做</option><option value="wrong" '+(practiceFilter.status==='wrong'?'selected':'')+'>错题</option><option value="mastered" '+(practiceFilter.status==='mastered'?'selected':'')+'>已掌握</option><option value="fav" '+(practiceFilter.status==='fav'?'selected':'')+'>收藏</option></select></label>' +
      '</div><div class="filter-foot"><div class="search-box" style="flex:1;min-width:220px">' + U.icon('search') + '<input class="input" data-filter="q" placeholder="搜索题干、选项、知识点…" value="' + U.attr(practiceFilter.q) + '"></div><span class="result-count" id="practice-count">匹配 <b>' + list.length + '</b> 题</span><button class="btn btn-ghost btn-sm" data-action="clear-filters">' + (activeFilters?'清空 ' + activeFilters + ' 个条件':'重置筛选') + '</button><button class="btn btn-primary btn-sm" data-action="start-filtered" data-shuffle="0">' + U.icon('play') + '顺序练</button><button class="btn btn-ink btn-sm" data-action="start-filtered" data-shuffle="1">' + U.icon('refresh') + '随机练</button></div></div>' +
      '<div class="section-head"><h2 id="practice-result-title">' + (activeFilters?'筛选结果':'全部题目') + '</h2><span class="hint">点击任意题目即刻开始；题目作答记录与错题本自动同步</span></div>' +
      '<div id="practice-results">' + practiceListHtml(list) + '</div>' +
      '<div class="section-head"><h2>题型 × 难度覆盖</h2><span class="hint">24 个档位均有题目</span></div><div class="card" style="overflow:auto"><div class="heatmap">' + renderHeatmap() + '</div></div>';
    return pageShell(content);
  }
  function renderHeatmap() {
    const typeOrder = ['single','multiple','judge','fill','code','programming'];
    let h = '<div class="heat-head"></div>' + [1,2,3,4].map(d=>'<div class="heat-head">'+DIFF_LABEL[d]+'</div>').join('');
    typeOrder.forEach(t => {
      h += '<div class="heat-head" style="text-align:left;color:var(--ink-2)">'+TYPE_LABEL[t]+'</div>';
      [1,2,3,4].forEach(d => { const n=QUESTIONS.filter(q=>q.type===t&&q.difficulty===d).length; h += '<div class="heat-cell ' + (n>15?'high':n?'has':'') + '">'+n+'</div>'; });
    });
    return h;
  }
  function refreshPracticeResults() {
    const list = filterQuestions();
    const box = document.getElementById('practice-results');
    if (box) box.innerHTML = practiceListHtml(list);
    const count = document.getElementById('practice-count'); if (count) count.innerHTML = '匹配 <b>' + list.length + '</b> 题';
  }

  /* ---------- chapter / topic ---------- */
  function renderChapter(ch) {
    ch = Number(ch) || 1; const meta = CHAPTER_TITLES[ch]; const s = chapterStats(ch);
    const topics = KNOWLEDGE.filter(k => k.chapter === ch);
    const qs = QUESTIONS.filter(q => q.chapter === ch);
    const content = '<div class="row wrap" style="margin-bottom:8px"><button class="icon-btn" data-action="back" aria-label="返回">' + U.icon('back') + '</button><span class="pill accent">第 ' + ch + ' 章</span><span class="pill">' + qs.length + ' 题</span></div>' +
      '<h1 class="display" style="font-size:clamp(27px,4vw,44px);margin-top:10px">' + U.esc(meta.title) + '</h1><p class="lede" style="margin-top:8px">' + U.esc(meta.desc) + '</p>' +
      '<div class="grid-3" style="margin-top:20px"><div class="stat-card"><div class="stat-label">完成进度</div><div class="stat-value">' + s.done + '<small> / ' + s.total + '</small></div><div class="progress thin" style="margin-top:8px"><i style="width:' + U.pct(s.done,s.total) + '%"></i></div></div><div class="stat-card"><div class="stat-label">累计正确率</div><div class="stat-value">' + (s.attempts?s.accuracy+'%':'—') + '</div><div class="stat-sub">' + s.correct + ' / ' + s.attempts + ' 次作答</div></div><div class="stat-card"><div class="stat-label">已掌握</div><div class="stat-value">' + s.mastered + '<small> 题</small></div><div class="stat-sub">连续答对 2 次</div></div></div>' +
      '<div class="row wrap" style="margin-top:16px"><button class="btn btn-primary" data-action="start-chapter" data-ch="' + ch + '">' + U.icon('play') + '练本章全部</button><button class="btn btn-ghost" data-action="start-chapter-random" data-ch="' + ch + '">' + U.icon('refresh') + '随机 15 题</button><a class="btn btn-ghost" href="#/knowledge">' + U.icon('brain') + '知识点速查</a></div>' +
      '<div class="section-head"><h2>本章知识点</h2><span class="hint">点击速查，或直接专练一个知识点</span></div><div class="card" style="padding:4px 20px"><div class="topic-list">' + topics.map(k => { const ts=topicStats(k.id); return '<div class="topic-row"><div><h4><span class="muted mono tiny" style="margin-right:6px">' + U.esc(k.section) + '</span>' + U.esc(k.title) + '</h4><p>' + ts.done + ' / ' + ts.total + ' 题已做 · 正确率 ' + (ts.attempts?ts.accuracy+'%':'—') + ' · 来源 ' + U.esc(k.source) + '</p></div><div class="row"><button class="chip" data-action="practice-topic" data-topic="' + U.attr(k.id) + '">开始</button><a class="icon-btn" href="#/topic/' + encodeURIComponent(k.id) + '" aria-label="查看知识点">' + U.icon('arrow') + '</a></div></div>'; }).join('') + '</div></div>' +
      '<div class="section-head"><h2>本章题目</h2><span class="hint">按题号排序</span></div>' + practiceListHtml(qs);
    return pageShell(content);
  }
  function renderTopic(topicId) {
    const k = TOPICS[topicId]; if (!k) return pageShell('<div class="empty"><h3>知识点不存在</h3></div>');
    const qs = QUESTIONS.filter(q => q.topicId === topicId); const s = topicStats(topicId);
    const content = '<div class="row wrap" style="margin-bottom:8px"><button class="icon-btn" data-action="back">' + U.icon('back') + '</button><span class="pill accent">第 ' + k.chapter + ' 章 · ' + U.esc(k.section) + '</span><span class="pill">' + qs.length + ' 题</span></div>' +
      '<h1 class="display" style="font-size:clamp(26px,3.5vw,40px);margin-top:10px">' + U.esc(k.title) + '</h1><p class="lede" style="margin-top:10px">' + U.esc(k.summary) + '</p>' +
      '<div class="source-line" style="margin-top:14px">' + U.icon('doc') + '<span>来源：' + U.esc(k.source) + ' · ' + U.esc(k.slides) + '</span></div>' +
      '<div class="grid-2" style="margin-top:22px"><div class="card"><h3 style="font-size:15px;margin-bottom:11px">核心规则</h3><ul class="k-points" style="padding-left:18px">' + k.points.map(p=>'<li>'+U.esc(p)+'</li>').join('') + '</ul></div><div class="card"><h3 style="font-size:15px;margin-bottom:11px">易错提醒</h3><div class="k-warn" style="margin-top:0">' + k.pitfalls.map(p=>'<div>· '+U.esc(p)+'</div>').join('') + '</div><button class="btn btn-primary btn-block" style="margin-top:16px" data-action="practice-topic" data-topic="' + U.attr(k.id) + '">' + U.icon('play') + '专练这个知识点</button></div></div>' +
      '<div class="section-head"><h2>相关题目</h2><span class="hint">你的掌握度：' + (s.attempts?s.accuracy+'%':'还没开始') + '</span></div>' + practiceListHtml(qs);
    return pageShell(content);
  }
  function renderKnowledge() {
    const q = (practiceFilter.kq || '').toLowerCase();
    const list = KNOWLEDGE.filter(k => !q || (k.title + ' ' + k.summary + ' ' + (k.points||[]).join(' ') + ' ' + k.source).toLowerCase().includes(q));
    const content = '<div class="row between wrap"><div><div class="kicker">KNOWLEDGE MAP · FROM PPT</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">知识点地图<br><em>只学 PPT 讲过的。</em></h1><p class="lede" style="margin-top:10px">29 个知识点逐项标注来源 PPT、章节与页码。题目与解析不超出这张地图。</p></div><div class="card" style="min-width:220px;padding:15px"><div class="small muted">题库覆盖</div><div style="font-size:30px;font-weight:760">29<span class="small muted" style="font-weight:500"> 个知识点</span></div><div class="small muted">297 道题 · 6 种题型 · 4 档难度</div></div></div>' +
      '<div class="filter-panel" style="margin-top:20px"><div class="row wrap"><div class="search-box" style="flex:1;min-width:240px">' + U.icon('search') + '<input class="input" id="knowledge-search" placeholder="搜索知识点、规则关键词…" value="' + U.attr(practiceFilter.kq||'') + '"></div><span class="result-count">共 <b>' + list.length + '</b> 个知识点</span><a class="btn btn-ghost btn-sm" href="#/practice">' + U.icon('book') + '去题库</a></div></div>' +
      '<div class="knowledge-grid" style="margin-top:16px" id="knowledge-grid">' + list.map(k => { const ts=topicStats(k.id); return '<article class="k-card"><div class="row between"><span class="pill accent">第 ' + k.chapter + ' 章 · ' + U.esc(k.section) + '</span><span class="tiny muted">' + ts.total + ' 题</span></div><h3 style="margin-top:10px">' + U.esc(k.title) + '</h3><div class="k-meta">来源：' + U.esc(k.source) + ' · ' + U.esc(k.slides) + '</div><p>' + U.esc(k.summary) + '</p><ul class="k-points">' + k.points.slice(0,3).map(p=>'<li>'+U.esc(p)+'</li>').join('') + '</ul><div class="k-foot"><span class="tiny muted">' + (ts.attempts ? '正确率 '+ts.accuracy+'% · 已做 '+ts.done+'/'+ts.total : '尚未练习') + '</span><div class="row"><a class="btn btn-ghost btn-sm" href="#/topic/' + encodeURIComponent(k.id) + '">详情</a><button class="btn btn-soft btn-sm" data-action="practice-topic" data-topic="' + U.attr(k.id) + '">练习</button></div></div></article>'; }).join('') + '</div>';
    return pageShell(content);
  }

  /* ---------- session / quiz ---------- */
  function startSession(qids, title, mode) {
    const list = (qids || []).filter(id => QID[id]);
    if (!list.length) { U.toast('当前筛选下没有题目'); return; }
    state.session = { id:'s' + Date.now(), qids:list, idx:0, title:title || '练习', mode:mode||'normal', answers:{}, draft:{}, startedAt:Date.now() };
    state.session.startedAt = Date.now(); save(true); go('quiz');
  }
  function curQ() { const s=state.session; return s && s.qids[s.idx] ? QID[s.qids[s.idx]] : null; }
  function getDraft(q) {
    const s=state.session; if (!s) return null;
    if (s.draft[q.id] === undefined) s.draft[q.id] = q.type === 'multiple' ? [] : q.type === 'fill' ? new Array((q.answer||[]).length||1).fill('') : null;
    return s.draft[q.id];
  }
  function draftReady(q) {
    const d=getDraft(q);
    if (q.type==='single'||q.type==='code') return typeof d==='number';
    if (q.type==='multiple') return Array.isArray(d)&&d.length>0;
    if (q.type==='judge') return typeof d==='boolean';
    if (q.type==='fill') return (d||[]).every(x=>String(x).trim()!=='');
    return false;
  }
  function renderQuiz() {
    const s=state.session; if (!s || !curQ()) { go('home'); return pageShell('<div class="loading-screen"><div class="loader"></div></div>'); }
    const q=curQ(), answered=s.answers[q.id]!==undefined, rec=recOf(q.id);
    const idx=s.idx, total=s.qids.length, pct=U.pct(idx,total);
    const qMeta='<div class="q-meta"><span class="pill accent">第 '+q.chapter+' 章 · '+U.esc(q.knowledge)+'</span><span class="pill '+DIFF_CLASS[q.difficulty]+'">'+DIFF_LABEL[q.difficulty]+'</span><span class="pill">'+TYPE_LABEL[q.type]+'</span>'+(isFav(q.id)?'<span class="pill gold">'+U.icon('star')+' 已收藏</span>':'')+'</div>';
    const source = state.settings.showSource ? '<div class="source-line">'+U.icon('doc')+'<span>来源：'+U.esc(q.source)+'</span></div>' : '';
    const feedback = answered ? renderFeedback(q, isAnswerCorrect(q,s.answers[q.id])) : '';
    const actions = answered ? '<div class="quiz-actions"><button class="btn btn-ghost" data-action="prev-question" '+(idx===0?'disabled':'')+'>'+U.icon('back')+'上一题</button><button class="btn btn-ghost btn-sm" data-action="toggle-favorite" data-id="'+q.id+'">'+U.icon('star')+(isFav(q.id)?'已收藏':'收藏')+'</button><span class="spacer"></span>'+(idx<total-1?'<button class="btn btn-primary" data-action="next-question">下一题'+U.icon('arrow')+'</button>':'<button class="btn btn-primary" data-action="finish-session">'+U.icon('check')+'完成练习</button>')+'</div>' : '<div class="quiz-actions"><button class="btn btn-ghost" data-action="prev-question" '+(idx===0?'disabled':'')+'>'+U.icon('back')+'上一题</button><button class="btn btn-ghost btn-sm" data-action="reveal-answer">看答案</button><button class="btn btn-ghost btn-sm" data-action="toggle-favorite" data-id="'+q.id+'">'+U.icon('star')+'收藏</button><span class="spacer"></span><button class="btn btn-primary" id="submit-answer" data-action="submit-answer" '+(draftReady(q)?'':'disabled')+'>提交答案</button></div>';
    const content='<div class="quiz-top"><button class="icon-btn" data-action="back" aria-label="返回">'+U.icon('back')+'</button><div class="quiz-progress"><div class="row between" style="margin-bottom:5px"><span class="quiz-title">'+U.esc(s.title)+'</span><span class="quiz-counter">'+(idx+1)+' / '+total+'</span></div><div class="track"><i style="width:'+pct+'%"></i></div></div><button class="icon-btn" data-action="open-map" aria-label="题目地图">'+U.icon('grid')+'</button></div>' +
      '<div class="card question-card">'+qMeta+'<h2 class="q-stem">'+U.esc(q.stem)+'</h2>'+(q.code&&q.code.length?'<div class="code-block"><div class="code-bar"><i></i><i></i><i></i><span>C++</span></div><pre><code>'+U.esc(q.code.join('\n'))+'</code></pre></div>':'') + renderInput(q, s.answers[q.id], answered) + source + '</div>' + feedback + actions +
      '<div class="quiz-drawer" id="quiz-drawer"><div class="drawer-mask" data-action="close-map"></div><aside class="drawer"><div class="row"><h3>题目地图</h3><button class="icon-btn" style="margin-left:auto" data-action="close-map">'+U.icon('x')+'</button></div><p class="small muted" style="margin-bottom:16px">颜色代表作答结果；点击跳转。</p><div class="map-grid">'+s.qids.map((id,i)=>{const r=recOf(id),aq=s.answers[id]!==undefined;const cls=aq?(isAnswerCorrect(QID[id],s.answers[id])?'ok':'bad'):'';return '<button class="map-btn '+(i===idx?'current ':'')+cls+'" data-action="goto-question" data-i="'+i+'">'+(i+1)+'</button>';}).join('')+'</div><div class="divider"></div><div class="small muted">快捷键：<kbd>1</kbd>–<kbd>6</kbd> 选择选项，<kbd>Enter</kbd> 提交 / 下一题，<kbd>←</kbd> <kbd>→</kbd> 切题。</div><button class="btn btn-danger btn-block" style="margin-top:18px" data-action="quit-session">退出本次练习</button></aside></div>';
    return pageShell(content);
  }
  function renderInput(q, resp, answered) {
    const disabled = answered ? 'disabled' : '';
    if (q.type==='single'||q.type==='multiple'||q.type==='code') {
      const d=getDraft(q), chosen=q.type==='multiple'?(Array.isArray(d)?d:[]):(typeof d==='number'?d:null);
      return '<div class="options" id="option-list">'+q.options.map((o,i)=>{
        let cls='opt';
        if (answered) {
          const isAns=q.type==='multiple'?q.answer.includes(i):i===q.answer;
          const isSel=q.type==='multiple'?chosen.includes(i):chosen===i;
          if (isAns&&isSel) cls+=' correct'; else if (isAns) cls+=' missed'; else if (isSel) cls+=' wrong';
        } else if (q.type==='multiple'?chosen.includes(i):chosen===i) cls+=' sel';
        return '<button class="'+cls+'" data-action="pick-option" data-i="'+i+'" '+disabled+'><span class="opt-key">'+U.LETTERS[i]+'</span><span class="opt-text">'+U.esc(o)+'</span></button>';
      }).join('')+'</div>'+(q.type==='multiple'?'<div class="q-hint">多选题：选择所有正确项后再提交。</div>':'');
    }
    if (q.type==='judge') {
      const d=getDraft(q); const sel=typeof d==='boolean'?d:null;
      return '<div class="judge-row">'+[true,false].map(v=>{let cls='judge-btn';if(answered){if(v===q.answer)cls+=' correct';else if(sel===v)cls+=' wrong';}else if(sel===v)cls+=' sel';return '<button class="'+cls+'" data-action="pick-judge" data-v="'+v+'" '+disabled+'>'+(v?'✓ 正确':'✗ 错误')+'</button>';}).join('')+'</div>';
    }
    if (q.type==='fill') {
      const n=(q.answer||[]).length||1; const d=getDraft(q)||[];
      let h='<div class="fill-list">';
      for(let i=0;i<n;i++){ const cls=answered?(U.fillKey(d[i])===U.fillKey(q.answer[i])||((q.alt&&q.alt[i])||[]).some(a=>U.fillKey(a)===U.fillKey(d[i]))?' correct':' wrong'):''; h+='<div class="fill-row">'+(n>1?'<label>第 '+(i+1)+' 空</label>':'')+'<input class="fill-input '+cls+'" data-action="fill-input" data-i="'+i+'" value="'+U.attr(d[i]||'')+'" placeholder="输入答案" autocomplete="off" spellcheck="false" '+disabled+'></div>'; }
      return h+'</div><div class="fill-tip">空格、行末分号可省略；全角符号与弯引号会自动转换为半角；<code>std::</code> 前缀、<code>static_cast&lt;double&gt;(x)</code> 与 <code>(double)x</code> 等常见等价写法可互相判对。</div>';
    }
    if (q.type==='programming') return renderProgramming(q, answered);
    return '';
  }

  function renderFeedback(q, ok) {
    const ans = U.answerText(q);
    const solution = q.type==='programming' && q.solution ? '<div class="code-block" style="margin-top:14px"><div class="code-bar"><i></i><i></i><i></i><span>参考解 · C++</span></div><pre><code>'+U.esc(q.solution)+'</code></pre></div>' : '';
    return '<div class="feedback '+(ok?'ok':'bad')+'"><div class="feedback-head">'+U.icon(ok?'check':'x')+(ok?'回答正确':'回答错误')+'<span class="pill '+(ok?'ok':'bad')+'" style="margin-left:auto">'+(ok?'+1 正确':'已加入错题复习')+'</span></div><div class="feedback-body">'+U.esc(q.explain)+(ok?'':'<div class="answer-line">正确答案：<b>'+U.esc(ans)+'</b></div>')+'<div class="source-line">'+U.icon('doc')+'<span>PPT 来源：'+U.esc(q.source)+'</span></div>'+solution+'</div></div>';
  }

  function progDraft(q) {
    if (!state.drafts[q.id] || typeof state.drafts[q.id] !== 'object') state.drafts[q.id] = { code:q.starter, stdin:(q.tests[0]&&q.tests[0].input)||'' };
    if (typeof state.drafts[q.id].code !== 'string') state.drafts[q.id].code = q.starter;
    if (typeof state.drafts[q.id].stdin !== 'string') state.drafts[q.id].stdin = (q.tests[0]&&q.tests[0].input)||'';
    return state.drafts[q.id];
  }
  function renderProgramming(q, answered) {
    const d = progDraft(q);
    const p = pendingProgram[q.id] || {};
    const visible = q.tests.map((t,i)=>!t.hidden?i:-1).filter(i=>i>=0);
    const sample = q.tests[0];
    let testsHtml = '<div class="prog-tests" id="prog-tests-'+q.id+'">' + q.tests.map((t,i) => {
      const r = p.testResults && p.testResults[i];
      const before = t.hidden ? '提交后评测' : ('输入 ' + U.esc(String(t.input||'空').split(String.fromCharCode(10)).join('↵')) + ' → 期望 ' + U.esc(String(t.output).split(String.fromCharCode(10)).join('↵')));
      const after = r ? (r.passed ? '通过' : ('未通过 · 期望 ' + U.esc(String(t.output).split(String.fromCharCode(10)).join('↵')) + ' · 实际 ' + U.esc(String(r.actual||'').split(String.fromCharCode(10)).join('↵')))) : '未执行';
      return '<div class="test-row '+(r?(r.passed?'pass':'fail'):'')+'" title="'+U.attr((t.input||'')+' -> '+(t.output||''))+'"><span class="test-name">'+(t.hidden?'隐藏测试':'样例 '+(i+1))+'</span><span class="test-detail">'+(r?after:before)+'</span></div>';
    }).join('') + '</div>';
    return '<div class="code-wrap"><div class="editor-card card" style="border-radius:16px"><div class="editor-head"><div class="editor-dots"><i></i><i></i><i></i></div><span class="editor-name">main.cpp</span><div class="editor-tools"><button class="btn btn-ghost btn-sm" data-action="reset-prog" data-id="'+q.id+'">'+U.icon('refresh')+'重置</button><button class="btn btn-soft btn-sm" data-action="prog-beautify" data-id="'+q.id+'">对齐</button></div></div><div class="editor-wrap"><div class="line-nums" id="prog-lines-'+q.id+'">'+d.code.split('\n').map((_,i)=>'<span>'+(i+1)+'</span>').join('')+'</div><textarea class="code-editor" id="prog-code-'+q.id+'" data-action="prog-code" data-id="'+q.id+'" spellcheck="false" '+(answered?'disabled':'')+'>'+U.esc(d.code)+'</textarea></div></div>' +
      '<div class="grid-2" style="margin-top:12px"><div><label class="field"><span>自定义输入 stdin</span><textarea class="stdin-area" id="prog-stdin-'+q.id+'" data-action="prog-stdin" data-id="'+q.id+'" '+(answered?'disabled':'')+'>'+U.esc(d.stdin)+'</textarea></label></div><div><div class="row wrap" style="height:100%;align-content:center"><button class="btn btn-primary" data-action="run-prog" data-id="'+q.id+'" '+(answered?'disabled':'')+'>'+U.icon('play')+'运行</button><button class="btn btn-ink" data-action="judge-prog" data-id="'+q.id+'" '+(answered?'disabled':'')+'>'+U.icon('check')+'提交评测</button><button class="btn btn-ghost btn-sm" data-action="load-sample" data-id="'+q.id+'">'+U.icon('task')+'载入样例输入</button></div></div></div>' +
      '<div class="console" id="prog-console-'+q.id+'">'+(p.html || '<div class="console-head"><span class="status-dot"></span>OUTPUT</div><div class="console-body"><pre class="muted">点击「运行」使用自定义输入；点击「提交评测」将依次运行全部测试用例。</pre></div>')+'</div>' +
      '<div class="row between wrap" style="margin-top:10px"><span class="small muted">评测会真实编译并运行你的代码。失败后可修改再提交；成功即记录为答对。</span><span class="pill">'+q.tests.length+' 个测试 · '+q.tests.filter(t=>t.hidden).length+' 个隐藏</span></div>' + testsHtml + '</div>';
  }
  function consoleHtml(r) {
    if (!r) return '';
    if (!r.compiled) {
      return '<div class="console-head"><span class="status-dot bad"></span>COMPILER ERROR · '+r.durationMs+'ms</div><div class="console-body"><pre class="err">'+U.esc(r.error||'编译失败')+'</pre>'+(r.friendly?'<pre class="warn" style="margin-top:10px">'+U.esc(r.friendly)+'</pre>':'')+'</div>';
    }
    const out = r.stdout ? U.esc(r.stdout) : '(无标准输出)';
    const err = r.stderr ? '<pre class="err" style="margin-top:10px">'+U.esc(r.stderr)+'</pre>' : '';
    return '<div class="console-head"><span class="status-dot '+(r.stderr?'bad':'ok')+'"></span>RUN COMPLETE · '+r.durationMs+'ms</div><div class="console-body"><div class="meta-line">$ g++ -std=c++17 main.cpp && ./a.out</div><pre class="'+(r.stderr?'':'ok')+'">'+out+'</pre>'+err+(r.friendly?'<pre class="warn" style="margin-top:10px">'+U.esc(r.friendly)+'</pre>':'')+'</div>';
  }
  function updateConsole(qid, html) {
    const el=document.getElementById('prog-console-'+qid); if(el) el.innerHTML=html;
    const p=pendingProgram[qid]||(pendingProgram[qid]={}); p.html=html;
  }
  async function runProgram(q, judge) {
    const codeEl=document.getElementById('prog-code-'+q.id); if(!codeEl) return;
    const stdinEl=document.getElementById('prog-stdin-'+q.id);
    const code=codeEl.value, stdin=stdinEl?stdinEl.value:'';
    const d=progDraft(q); d.code=code; d.stdin=stdin; save();
    const p=pendingProgram[q.id]||(pendingProgram[q.id]={});
    if (judge) {
      if (p.judging) return; p.judging=true; p.testResults=[];
      const start=Date.now();
      updateConsole(q.id,'<div class="console-head"><span class="status-dot running"></span>RUNNING TESTS</div><div class="console-body"><pre class="warn">正在编译并运行 '+q.tests.length+' 个测试用例…首次编译可能需要几秒。</pre></div>');
      const res=await SAND.judgeTests(code,q.tests,(i,total,t)=>{
        const html='<div class="console-head"><span class="status-dot running"></span>TEST '+(i+1)+' / '+total+'</div><div class="console-body"><pre class="warn">正在运行 '+(t.hidden?'隐藏测试':'样例 '+(i+1))+'…</pre></div>';
        updateConsole(q.id,html);
        const box=document.getElementById('prog-tests-'+q.id);
        if(box){const rows=box.querySelectorAll('.test-row'); if(rows[i]) rows[i].className='test-row '+(pendingProgram[q.id].testResults[i]?.passed?'pass':'');}
      });
      p.judging=false; p.testResults=res.results;
      const firstFail=res.results.find(r=>!r.passed);
      const run=firstFail?firstFail.run:res.results[res.results.length-1]?.run;
      updateConsole(q.id,consoleHtml(run)||'');
      const testsBox=document.getElementById('prog-tests-'+q.id);
      if(testsBox){testsBox.innerHTML=q.tests.map((t,i)=>{const r=res.results[i];return '<div class="test-row '+(r?(r.passed?'pass':'fail'):'')+'"><span class="test-name">'+(t.hidden?'隐藏测试':'样例 '+(i+1))+'</span><span class="test-detail">'+(r?(r.passed?'通过':('未通过 · 期望 '+U.esc(String(t.output).split(String.fromCharCode(10)).join('↵'))+' · 实际 '+U.esc(String(r.actual||'').split(String.fromCharCode(10)).join('↵')))):'未执行')+'</span></div>';}).join('');}
      if(res.allPassed){
        const s=state.session; if(s){s.answers[q.id]=code;} recordAttempt(q,true,code,Date.now()-currentQuestionStarted); pendingProgram[q.id]={html:p.html,testResults:res.results,passed:true};
        save(); U.toast('全部测试通过！'); setTimeout(()=>{ if(route.name==='quiz') renderRoute(); },450);
      }else{
        recordAttempt(q,false,code,Date.now()-currentQuestionStarted); pendingProgram[q.id]={html:p.html,testResults:res.results,passed:false};
        save(); U.toast(firstFail&&!firstFail.run.compiled?'编译失败，请查看错误信息':'未通过全部测试，修改后可以再提交');
      }
      return;
    }
    updateConsole(q.id,'<div class="console-head"><span class="status-dot running"></span>COMPILING</div><div class="console-body"><pre class="warn">正在请求在线编译器…</pre></div>');
    const r=await SAND.runCpp(code,stdin);
    pendingProgram[q.id]={html:consoleHtml(r),lastRun:r}; updateConsole(q.id,consoleHtml(r));
  }

  /* ---------- free sandbox ---------- */
  const EXAMPLES = [
    { name:'Hello, C++', code:'#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << "Hello, C++!" << endl;\n    return 0;\n}\n', stdin:'' },
    { name:'输入与计算', code:'#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a + b << endl;\n    return 0;\n}\n', stdin:'3 5\n' },
    { name:'循环与累加', code:'#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, sum = 0;\n    cin >> n;\n    for (int i = 1; i <= n; i++) sum += i;\n    cout << sum << endl;\n    return 0;\n}\n', stdin:'10\n' },
    { name:'数组与逆序', code:'#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, a[100];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    for (int i = n - 1; i >= 0; i--) cout << a[i] << " ";\n    return 0;\n}\n', stdin:'5\n1 2 3 4 5\n' },
    { name:'结构体', code:'#include <iostream>\nusing namespace std;\n\nstruct Student { int no; int score; };\n\nint main() {\n    Student s;\n    cin >> s.no >> s.score;\n    cout << s.no << ":" << s.score << endl;\n    return 0;\n}\n', stdin:'7 95\n' },
    { name:'递归阶乘', code:'#include <iostream>\nusing namespace std;\n\nint factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}\n\nint main() {\n    cout << factorial(6) << endl;\n    return 0;\n}\n', stdin:'' },
    { name:'指针交换', code:'#include <iostream>\nusing namespace std;\n\nvoid swap(int* a, int* b) {\n    int t = *a; *a = *b; *b = t;\n}\n\nint main() {\n    int x = 1, y = 2;\n    swap(&x, &y);\n    cout << x << " " << y << endl;\n    return 0;\n}\n', stdin:'' },
    { name:'动态数组', code:'#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    int* p = new int[n];\n    for (int i = 0; i < n; i++) p[i] = i * i;\n    for (int i = 0; i < n; i++) cout << p[i] << " ";\n    delete[] p;\n    return 0;\n}\n', stdin:'6\n' }
  ];
  function sandboxDraft() {
    if (!state.sandbox || typeof state.sandbox !== 'object') state.sandbox = { code:EXAMPLES[0].code, stdin:'' };
    return state.sandbox;
  }
  function lineNums(code) { return code.split('\n').map((_,i)=>'<span>'+(i+1)+'</span>').join(''); }
  function renderSandbox(qid) {
    const d = sandboxDraft();
    const p = pendingProgram['__sandbox__'] || {};
    const preload = qid && QID[qid];
    const content = '<div class="row between wrap"><div><div class="kicker">LIVE C++ SANDBOX · GCC</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">写一段代码，<br><em>让编译器回答。</em></h1><p class="lede" style="margin-top:10px">在页面内编辑、编译、运行 C++ 程序；输出、编译错误与运行错误都会原样呈现。需要联网。</p></div><div class="row wrap"><span class="pill accent">C++17</span><span class="pill">GCC Head</span><span class="pill blue">Wandbox API</span></div></div>' +
      (preload?'<div class="card" style="margin-top:18px;padding:14px 18px"><div class="row wrap"><span class="pill accent">已载入题目</span><b class="small">'+U.esc(preload.stem)+'</b><button class="btn btn-soft btn-sm" style="margin-left:auto" data-action="practice-one" data-id="'+preload.id+'">回到题目</button></div></div>':'') +
      '<div class="sandbox-layout" style="margin-top:18px"><div><div class="editor-card card"><div class="editor-head"><div class="editor-dots"><i></i><i></i><i></i></div><span class="editor-name">main.cpp</span><span class="pill" style="margin-left:4px">C++17</span><div class="editor-tools"><button class="btn btn-ghost btn-sm" data-action="sandbox-reset">'+U.icon('refresh')+'重置</button><button class="btn btn-soft btn-sm" data-action="sandbox-clear">'+U.icon('trash')+'清空</button><button class="btn btn-primary btn-sm" data-action="run-sandbox">'+U.icon('play')+'运行 Ctrl+Enter</button></div></div><div class="editor-wrap"><div class="line-nums" id="sandbox-lines">'+lineNums(d.code)+'</div><textarea class="code-editor" id="sandbox-code" spellcheck="false" '+(preload?'':'')+'>'+U.esc(d.code)+'</textarea></div></div>' +
        '<div class="grid-2" style="margin-top:14px"><div class="card" style="padding:15px"><label class="field"><span>标准输入 stdin</span><textarea class="stdin-area" id="sandbox-stdin" placeholder="程序运行时从 cin 读取的数据">'+U.esc(d.stdin)+'</textarea></label><div class="row between" style="margin-top:9px"><span class="tiny muted">可粘贴多行输入</span><button class="btn btn-ghost btn-sm" data-action="sandbox-load-stdin">载入示例输入</button></div></div><div class="card" style="padding:15px"><div class="row wrap"><span class="pill accent">真实编译</span><span class="pill">隔离执行</span></div><p class="small muted" style="margin-top:10px;line-height:1.75">首次编译可能需要 2–8 秒。编译失败会显示 GCC 原始诊断和中文排查提示。</p><div class="row" style="margin-top:12px"><button class="btn btn-ink btn-block" data-action="run-sandbox">'+U.icon('terminal')+'编译并运行</button></div></div></div>' +
        '<div class="console" id="sandbox-console">'+(p.html||'<div class="console-head"><span class="status-dot"></span>OUTPUT</div><div class="console-body"><pre class="muted">等待运行…</pre></div>')+'</div></div>' +
        '<aside class="sandbox-side"><div class="card"><div class="card-head"><div><h3>快速示例</h3><p>点击载入，不覆盖当前作答记录</p></div></div><div class="example-grid">'+EXAMPLES.map((e,i)=>'<button class="example-btn" data-action="sandbox-example" data-i="'+i+'">'+U.esc(e.name)+'</button>').join('')+'</div></div><div class="api-note">编译能力由公共 Wandbox 服务提供，源码与 stdin 会发送到远端隔离环境。它不依赖自建后端，适合 GitHub Pages。若服务不可用，请稍后重试。</div><div class="card"><div class="card-head"><div><h3>编程题</h3><p>带测试用例与自动评测</p></div><span class="pill">'+QUESTIONS.filter(q=>q.type==='programming').length+' 道</span></div><div class="stack">'+QUESTIONS.filter(q=>q.type==='programming').slice(0,4).map(q=>'<button class="q-list-item" style="grid-template-columns:minmax(0,1fr) auto;padding:9px 0;border-width:0 0 1px;border-radius:0;background:none" data-action="practice-one" data-id="'+q.id+'"><div><div class="q-list-stem" style="font-size:12px">'+U.esc(q.stem)+'</div><div class="q-list-meta"><span class="pill '+DIFF_CLASS[q.difficulty]+'">'+DIFF_LABEL[q.difficulty]+'</span><span class="tiny muted">第'+q.chapter+'章</span></div></div><span class="chapter-arrow">'+U.icon('arrow')+'</span></button>').join('')+'</div></div></aside></div>';
    return pageShell(content);
  }
  async function runFreeSandbox() {
    const codeEl=document.getElementById('sandbox-code'), stdinEl=document.getElementById('sandbox-stdin');
    if(!codeEl) return;
    const code=codeEl.value, stdin=stdinEl?stdinEl.value:'';
    state.sandbox={code,stdin}; save();
    const p=pendingProgram['__sandbox__']||(pendingProgram['__sandbox__']={});
    p.html='<div class="console-head"><span class="status-dot running"></span>COMPILING</div><div class="console-body"><pre class="warn">正在请求在线编译器…</pre></div>';
    const box=document.getElementById('sandbox-console'); if(box) box.innerHTML=p.html;
    const r=await SAND.runCpp(code,stdin);
    p.html=consoleHtml(r); p.lastRun=r;
    const box2=document.getElementById('sandbox-console'); if(box2) box2.innerHTML=p.html;
  }


  /* ---------- statistics ---------- */
  function statBar(name, value, label, extra) {
    const color = value>=80?'var(--ok)':value>=60?'var(--warn)':'var(--bad)';
    return '<div class="bar-row"><span class="bar-name">'+name+(extra||'')+'</span><div class="bar-track"><i style="width:'+value+'%;background:'+color+'"></i></div><span class="bar-val">'+label+'</span></div>';
  }
  function renderStats() {
    const g=globalStats(), days=activitySeries(7), maxDay=Math.max(1,...days.map(d=>d.data.answered));
    const weak=KNOWLEDGE.map(k=>({k,s:topicStats(k.id)})).filter(x=>x.s.attempts>0).sort((a,b)=>a.s.accuracy-b.s.accuracy||b.s.wrong-a.s.wrong).slice(0,8);
    const byType=Object.keys(TYPE_LABEL).map(t=>{const qs=QUESTIONS.filter(q=>q.type===t);let a=0,c=0;qs.forEach(q=>{const r=recOf(q.id);if(r){a+=r.attempts;c+=r.correct||0;}});return {t,total:qs.length,attempts:a,correct:c,acc:a?U.pct(c,a):0};});
    const byDiff=[1,2,3,4].map(d=>{const qs=QUESTIONS.filter(q=>q.difficulty===d);let a=0,c=0;qs.forEach(q=>{const r=recOf(q.id);if(r){a+=r.attempts;c+=r.correct||0;}});return {d,total:qs.length,attempts:a,correct:c,acc:a?U.pct(c,a):0};});
    const head='<div class="row between wrap"><div><div class="kicker">LEARNING ANALYTICS</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">学习统计<br><em>看清进步，也看清漏洞。</em></h1></div><button class="btn btn-ghost" data-action="export-data">'+U.icon('download')+'导出记录</button></div>' +
      '<div class="grid-4" style="margin-top:20px"><div class="stat-card"><div class="stat-label">已做题目</div><div class="stat-value">'+g.done+'<small> / '+g.total+'</small></div><div class="progress thin" style="margin-top:8px"><i style="width:'+U.pct(g.done,g.total)+'%"></i></div></div><div class="stat-card"><div class="stat-label">累计正确率</div><div class="stat-value">'+g.accuracy+'%</div><div class="stat-sub">'+g.correct+' 正确 / '+g.attempts+' 次作答</div></div><div class="stat-card"><div class="stat-label">已掌握</div><div class="stat-value">'+g.mastered+'<small> 题</small></div><div class="stat-sub">连续答对 ≥ 2 次</div></div><div class="stat-card"><div class="stat-label">学习时长</div><div class="stat-value" style="font-size:22px">'+Math.round(g.time/60000)+'<small> 分钟</small></div><div class="stat-sub">按答题会话估算</div></div></div>';
    const week='<div class="grid-2" style="margin-top:18px"><div class="card"><div class="card-head"><div><h3>最近 7 天作答</h3><p>每天的有效答题次数</p></div><span class="pill accent">连续 '+streakDays()+' 天</span></div><div class="week-chart">'+days.map(d=>'<div class="day-col"><span class="day-count">'+d.data.answered+'</span><div class="day-bar '+(d.data.answered?'has':'')+'" style="height:'+(d.data.answered?Math.max(8,U.pct(d.data.answered,maxDay)*100):4)+'%"></div><span class="day-label">'+(d.date.getMonth()+1)+'/'+d.date.getDate()+'</span></div>').join('')+'</div></div><div class="card"><div class="card-head"><div><h3>每日目标</h3><p>完成 '+dailyProgress().answered+' / '+dailyProgress().goal+' 题</p></div><button class="chip" data-action="change-goal">调整目标</button></div><div class="progress gold" style="height:12px"><i style="width:'+U.pct(dailyProgress().answered,dailyProgress().goal)+'%"></i></div><div class="grid-2" style="margin-top:16px"><div class="stat-card flat" style="padding:12px"><div class="stat-label">今日答对</div><div class="stat-value" style="font-size:21px">'+(dailyProgress().correct||0)+'</div></div><div class="stat-card flat" style="padding:12px"><div class="stat-label">今日学习</div><div class="stat-value" style="font-size:21px">'+Math.round((dailyProgress().seconds||0)/60)+'<small> 分</small></div></div></div></div></div>';
    const chapterBars=[1,2,3,4,5].map(ch=>{const s=chapterStats(ch);return statBar('第'+ch+'章 '+U.esc(CHAPTER_TITLES[ch].short),s.attempts?s.accuracy:0,s.attempts?s.accuracy+'% · '+s.done+'/'+s.total:'未开始');}).join('');
    const typeBars=byType.map(x=>statBar(TYPE_LABEL[x.t],x.acc,x.attempts?x.acc+'%':'—',' <span class="tiny muted">'+x.total+'题</span>')).join('');
    const diffBars=byDiff.map(x=>statBar(DIFF_LABEL[x.d],x.acc,x.attempts?x.acc+'%':'—',' <span class="tiny muted">'+x.total+'题</span>')).join('');
    const weakBars=weak.length?weak.map(x=>statBar(U.esc(x.k.title),x.s.accuracy,x.s.accuracy+'%')).join(''):'<p class="small muted">做几道题后显示。</p>';
    const rest='<div class="grid-2" style="margin-top:18px"><div class="card"><div class="card-head"><div><h3>各章掌握情况</h3><p>正确率与完成度</p></div></div>'+chapterBars+'</div><div class="card"><div class="card-head"><div><h3>题型正确率</h3><p>找出最不稳的题型</p></div></div>'+typeBars+'</div></div>' +
      '<div class="grid-2" style="margin-top:18px"><div class="card"><div class="card-head"><div><h3>难度正确率</h3><p>困难题是否稳定</p></div></div>'+diffBars+'</div><div class="card"><div class="card-head"><div><h3>薄弱知识点</h3><p>按正确率从低到高</p></div></div>'+weakBars+'</div></div>' +
      '<div class="section-head"><h2>题型 × 难度题量</h2><span class="hint">24 个组合全部覆盖</span></div><div class="card" style="overflow:auto"><div class="heatmap">'+renderHeatmap()+'</div></div>';
    return pageShell(head+week+rest);
  }

  /* ---------- wrong / favorites ---------- */
  function renderWrong() {
    const list=QUESTIONS.filter(q=>inWrongBook(q.id)).sort((a,b)=>(recOf(b.id)?.lastAt||0)-(recOf(a.id)?.lastAt||0));
    const content='<div class="row between wrap"><div><div class="kicker">REVIEW QUEUE</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">错题本<br><em>只留下还没掌握的。</em></h1><p class="lede" style="margin-top:10px">答错自动进入；连续答对 2 次后自动移出。复习时优先做最近错的题。</p></div><div class="card" style="min-width:180px;text-align:center"><div style="font-size:38px;font-weight:760;line-height:1.2">'+list.length+'</div><div class="small muted">道待巩固</div><button class="btn btn-primary btn-sm" style="margin-top:10px" data-action="start-wrong" '+(list.length?'':'disabled')+'>'+U.icon('fire')+'开始重练</button></div></div>' +
      '<div class="section-head"><h2>题目列表</h2><span class="hint">颜色条代表最近一次状态</span></div>' + (list.length? '<div class="question-list">'+list.map(q=>{const r=recOf(q.id)||{};return '<button class="q-list-item" data-action="practice-one" data-id="'+q.id+'"><span class="q-status bad"></span><div><div class="q-list-stem">'+U.esc(q.stem)+'</div><div class="q-list-meta"><span class="pill bad">错 '+(r.wrong||0)+' 次</span><span class="pill">连续答对 '+((r.streak||0))+' / 2</span><span class="pill">'+TYPE_LABEL[q.type]+'</span><span class="tiny muted">第'+q.chapter+'章 · '+U.esc(q.knowledge)+'</span></div></div><span class="chapter-arrow">'+U.icon('arrow')+'</span></button>';}).join('')+'</div>' : emptyState('check','错题本是空的','做错题会自动收进来；连续答对 2 次后移出。','<a class="btn btn-soft btn-sm" style="margin-top:14px" href="#/practice">去练几道题</a>'));
    return pageShell(content);
  }
  function renderFavorites() {
    const list=QUESTIONS.filter(q=>isFav(q.id));
    const content='<div class="row between wrap"><div><div class="kicker">STARRED QUESTIONS</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">收藏夹<br><em>把值得再看的题留下。</em></h1></div><span class="pill accent">'+list.length+' 题</span></div>' +
      (list.length?'<div class="question-list" style="margin-top:20px">'+list.map(q=>'<button class="q-list-item" data-action="practice-one" data-id="'+q.id+'"><span class="q-index">'+q.id.replace('q','#')+'</span><div><div class="q-list-stem">'+U.esc(q.stem)+'</div><div class="q-list-meta"><span class="pill gold">已收藏</span><span class="pill">'+TYPE_LABEL[q.type]+'</span><span class="tiny muted">'+U.esc(q.knowledge)+'</span></div></div><span class="chapter-arrow">'+U.icon('arrow')+'</span></button>').join('')+'</div>':emptyState('star','还没有收藏题目','在答题页点击“收藏”，题目会出现在这里。','<a class="btn btn-soft btn-sm" style="margin-top:14px" href="#/practice">去题库看看</a>'));
    return pageShell(content);
  }

  /* ---------- docs / settings ---------- */
  function renderDocs() {
    const groups=DOWNLOADS.map(g=>'<div class="section-head"><h2>'+U.esc(g.group)+'</h2></div><div class="grid-2">'+g.items.map(it=>'<a class="card hoverable" style="display:flex;gap:13px;align-items:flex-start;color:var(--ink)" href="'+U.attr(it.file)+'" download><div class="quick-icon" style="margin:0;flex:0 0 auto">'+U.icon('doc')+'</div><div style="flex:1"><div class="row between"><b style="font-size:13.5px">'+U.esc(it.title)+'</b><span class="pill">'+U.esc(it.tag)+'</span></div><p class="small muted" style="margin-top:5px;line-height:1.6">'+U.esc(it.desc)+'</p><div class="tiny muted" style="margin-top:8px">'+U.icon('download')+' 点击下载</div></div></a>').join('')+'</div>').join('');
    const content='<div class="row between wrap"><div><div class="kicker">MATERIALS</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">学习资料<br><em>带走，随时翻。</em></h1><p class="lede" style="margin-top:10px">知识点清单、完整题库 JSON、功能对照表与错题模板；全部静态文件，可直接下载。</p></div><a class="btn btn-ghost" href="#/knowledge">'+U.icon('brain')+'在线知识点地图</a></div>'+groups+'<div class="card" style="margin-top:20px"><div class="row wrap"><span class="pill blue">数据可迁移</span><span class="pill">本地优先</span></div><p class="small muted" style="margin-top:10px;line-height:1.8">题库 JSON 与网站代码分离，新增题目时只需编辑 data/questions 并重新生成，不需要改页面逻辑。学习记录保存在浏览器 localStorage，可在设置中导出/导入。</p></div>';
    return pageShell(content);
  }
  function renderSettings() {
    const g=globalStats();
    const themeOptions=[{k:'system',t:'跟随系统'},{k:'light',t:'浅色'},{k:'dark',t:'深色'}];
    const content='<div class="row between wrap"><div><div class="kicker">PREFERENCES</div><h1 class="display" style="font-size:clamp(28px,4vw,44px)">设置</h1></div><span class="pill accent">记录已保存在本机</span></div>' +
      '<div class="section-head"><h2>外观与体验</h2></div><div class="card"><div class="set-row"><div class="set-label"><b>主题</b><span>选择浅色、深色或跟随系统</span></div><div class="seg">'+themeOptions.map(o=>'<button class="'+(state.settings.theme===o.k?'active':'')+'" data-action="set-theme" data-theme="'+o.k+'">'+o.t+'</button>').join('')+'</div></div><div class="set-row"><div class="set-label"><b>交互动效</b><span>关闭后减少动画，适合专注练习</span></div><div class="switch '+(state.settings.motion?'on':'')+'" data-action="toggle-setting" data-key="motion" role="switch" aria-checked="'+!!state.settings.motion+'"></div></div><div class="set-row"><div class="set-label"><b>答对后自动下一题</b><span>编程题通过后也会自动前进</span></div><div class="switch '+(state.settings.autoNext?'on':'')+'" data-action="toggle-setting" data-key="autoNext" role="switch" aria-checked="'+!!state.settings.autoNext+'"></div></div><div class="set-row"><div class="set-label"><b>显示 PPT 来源</b><span>在题目下方显示对应课件章节与页码</span></div><div class="switch '+(state.settings.showSource?'on':'')+'" data-action="toggle-setting" data-key="showSource" role="switch" aria-checked="'+!!state.settings.showSource+'"></div></div></div>' +
      '<div class="section-head"><h2>学习节奏</h2></div><div class="card"><div class="set-row"><div class="set-label"><b>每日目标</b><span>完成多少道有效作答算达标</span></div><div class="row">'+[10,20,30,50].map(n=>'<button class="chip '+(state.settings.dailyGoal===n?'active':'')+'" data-action="set-goal" data-goal="'+n+'">'+n+' 题</button>').join('')+'</div></div></div>' +
      '<div class="section-head"><h2>数据</h2></div><div class="card"><div class="set-row"><div class="set-label"><b>导出学习记录</b><span>包含作答记录、收藏、每日活动与设置</span></div><button class="btn btn-ghost btn-sm" data-action="export-data">'+U.icon('download')+'导出 JSON</button></div><div class="set-row"><div class="set-label"><b>导入学习记录</b><span>从 JSON 恢复，会覆盖当前记录</span></div><button class="btn btn-ghost btn-sm" data-action="import-data">'+U.icon('upload')+'导入</button></div><div class="set-row"><div class="set-label"><b>清空全部记录</b><span>已做 '+g.done+' 题；请先导出备份</span></div><button class="btn btn-danger btn-sm" data-action="reset-data">'+U.icon('trash')+'清空</button></div></div>' +
      '<div class="section-head"><h2>快捷键</h2></div><div class="card"><div class="modal-grid"><div class="row"><kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd><span class="small muted">选择选项 / 判断</span></div><div class="row"><kbd>Enter</kbd><span class="small muted">提交 / 下一题</span></div><div class="row"><kbd>←</kbd><kbd>→</kbd><span class="small muted">上一题 / 下一题</span></div><div class="row"><kbd>/</kbd><span class="small muted">聚焦题目搜索</span></div><div class="row"><kbd>Ctrl</kbd><span>+</span><kbd>Enter</kbd><span class="small muted">运行沙箱代码</span></div><div class="row"><kbd>Esc</kbd><span class="small muted">关闭弹层</span></div></div></div>' +
      '<div class="section-head"><h2>关于</h2></div><div class="card"><p class="small muted" style="line-height:1.8">C++ Lab 是一个纯静态的 GitHub Pages 练习站。知识点与题目范围严格来自本地课程 PPT 第 1–5 章；编译运行由公共 Wandbox 服务完成，不需要自建后端。学习记录只保存在本机浏览器。</p><div class="row wrap" style="margin-top:12px"><span class="pill">'+QUESTIONS.length+' 题</span><span class="pill">'+KNOWLEDGE.length+' 个知识点</span><span class="pill">6 种题型</span><span class="pill">4 档难度</span><a class="pill blue" href="#/docs">资料下载</a></div></div>';
    return pageShell(content);
  }

  /* ---------- quiz interactions ---------- */
  function updateSubmitState() {
    const q=curQ(); if(!q) return; const btn=document.getElementById('submit-answer'); if(btn) btn.disabled=!draftReady(q);
  }
  function pickOption(i) {
    const q=curQ(); if(!q || state.session.answers[q.id]!==undefined) return;
    const d=getDraft(q);
    if (q.type==='multiple') { const at=d.indexOf(i); if(at>=0)d.splice(at,1);else d.push(i); }
    else state.session.draft[q.id]=i;
    const current=q.type==='multiple'?d:i;
    U.qsa('#option-list .opt').forEach((el,idx)=>{ const on=q.type==='multiple'?(current.includes(idx)):(current===idx); el.classList.toggle('sel',on); });
    updateSubmitState(); save();
  }
  function pickJudge(v) {
    const q=curQ(); if(!q||state.session.answers[q.id]!==undefined) return;
    state.session.draft[q.id]=v; U.qsa('.judge-btn').forEach(el=>el.classList.toggle('sel',String(v)===el.dataset.v)); updateSubmitState(); save();
  }
  function submitAnswer() {
    const q=curQ(), s=state.session; if(!q||!s||s.answers[q.id]!==undefined) return;
    const d=getDraft(q); if(!draftReady(q)) return;
    const resp=JSON.parse(JSON.stringify(d)); s.answers[q.id]=resp;
    const ok=U.grade(q,resp); recordAttempt(q,ok,resp,Date.now()-currentQuestionStarted);
    updateLastPractice(); save(true); renderRoute();
    setTimeout(()=>{ const fb=document.querySelector('.feedback'); if(fb) fb.scrollIntoView({behavior:'smooth',block:'center'}); },40);
    if (state.settings.autoNext && ok) setTimeout(()=>{ if(route.name==='quiz') nextQuestion(); },900);
  }
  async function revealAnswer() {
    const q=curQ(), s=state.session; if(!q||!s||s.answers[q.id]!==undefined) return;
    const yes=await U.confirm('看答案会记为答错','本题会加入错题复习，并显示标准答案与解析。确定查看吗？'); if(!yes) return;
    s.answers[q.id]=q.type==='programming'?'__revealed__':null; recordAttempt(q,false,null,Date.now()-currentQuestionStarted);
    updateLastPractice(); save(true); renderRoute();
  }
  function nextQuestion() {
    const s=state.session; if(!s) return;
    if(s.idx<s.qids.length-1){ s.idx++; save(true); currentQuestionStarted=Date.now(); renderRoute(); window.scrollTo({top:0,behavior:'smooth'}); }
    else finishSession();
  }
  function prevQuestion() {
    const s=state.session; if(!s||s.idx===0) return;
    s.idx--; save(true); currentQuestionStarted=Date.now(); renderRoute(); window.scrollTo({top:0,behavior:'smooth'});
  }
  function finishSession() {
    const s=state.session; if(!s) return;
    let done=0,ok=0; const wrongIds=[];
    s.qids.forEach(id=>{ if(s.answers[id]!==undefined){done++; if(isAnswerCorrect(QID[id],s.answers[id]))ok++; else wrongIds.push(id);} });
    const duration=Math.round((Date.now()-s.startedAt)/1000); const p=done?U.pct(ok,done):0;
    state.lastPractice={title:s.title,qids:s.qids.slice(),answered:done,ok,startedAt:s.startedAt,at:Date.now()};
    state.session=null; save(true); go('home');
    setTimeout(()=>{
      const verdict=p>=90?'掌握得很扎实，保持这个节奏。':p>=70?'基本掌握，重点再看错题。':p>=50?'还有明显漏洞，建议回到知识点地图。':'先补基础规则，再来一轮会更轻松。';
      const m=U.modal('<h2>本次练习完成</h2><div style="text-align:center;padding:16px 0"><div style="font-size:52px;font-weight:800;letter-spacing:-.05em;line-height:1">'+p+'<span style="font-size:20px;color:var(--ink-3)">%</span></div><div class="small muted" style="margin-top:6px">答对 '+ok+' / '+done+' 题 · 用时 '+U.formatTime(duration)+'</div><div class="pill '+(p>=70?'ok':'bad')+'" style="margin-top:12px">'+verdict+'</div></div><div class="row" style="justify-content:center;margin-top:12px">'+(wrongIds.length?'<button class="btn btn-primary" data-action="retry-wrong-list" data-ids="'+wrongIds.join(',')+'">重练本次错题</button>':'<button class="btn btn-primary" data-action="close-modal">继续学习</button>')+'<button class="btn btn-ghost" data-action="close-modal">返回首页</button></div>');
    },80);
  }
  function closeModalFromAction(el) { const back=el.closest('.modal-backdrop'); if(back) back.remove(); }

  /* ---------- navigation / data actions ---------- */
  function startFiltered(shuffle) {
    let list=filterQuestions(); if(!list.length){U.toast('没有匹配的题目');return;}
    if(shuffle) list=U.shuffle(list); const title=shuffle?'随机练习 · '+list.length+' 题':'筛选练习 · '+list.length+' 题';
    startSession(list.map(q=>q.id),title,shuffle?'random':'filtered');
  }
  function practiceOne(id) { const q=QID[id]; if(!q){U.toast('题目不存在');return;} startSession([id],'第'+q.chapter+'章 · '+q.knowledge,'single'); }
  function practiceTopic(id) { const list=QUESTIONS.filter(q=>q.topicId===id); if(!list.length){U.toast('该知识点暂无题目');return;} startSession(list.map(q=>q.id),'专练 · '+TOPICS[id].title,'topic'); }
  function startChapter(ch,shuffle) { let list=QUESTIONS.filter(q=>q.chapter===ch); if(shuffle) list=U.shuffle(list).slice(0,15); if(!list.length){U.toast('暂无题目');return;} startSession(list.map(q=>q.id),'第'+ch+'章 · '+CHAPTER_TITLES[ch].title,shuffle?'random':'chapter'); }
  function startWrong() { const list=QUESTIONS.filter(q=>inWrongBook(q.id)); if(!list.length){U.toast('错题本是空的');return;} startSession(list.map(q=>q.id),'错题重练 · '+list.length+' 题','wrong'); }
  function toggleFavorite(id) {
    const i=state.favorites.indexOf(id); if(i>=0) state.favorites.splice(i,1); else state.favorites.push(id); save(true); U.toast(i>=0?'已取消收藏':'已加入收藏');
    if(route.name==='quiz') renderRoute(); else if(route.name==='favorites') renderRoute(); else {
      const btn=document.querySelector('[data-action="toggle-favorite"][data-id="'+CSS.escape(id)+'"]'); if(btn && isFav(id)) btn.classList.add('on');
    }
  }

  /* ---------- export / import / reset ---------- */
  function exportData() {
    const data={app:'cpp-lab',version:2,exportedAt:new Date().toISOString(),state:state,manifest:MANIFEST};
    const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a');
    const d=new Date(),p=n=>String(n).padStart(2,'0'); a.href=url; a.download='cpp-lab-record-'+d.getFullYear()+p(d.getMonth()+1)+p(d.getDate())+'.json'; document.body.appendChild(a); a.click(); a.remove(); setTimeout(()=>URL.revokeObjectURL(url),1500); U.toast('学习记录已导出');
  }
  function importData() {
    const input=document.createElement('input'); input.type='file'; input.accept='application/json,.json';
    input.onchange=()=>{ const f=input.files&&input.files[0]; if(!f)return; const fr=new FileReader(); fr.onload=()=>{ try{ const obj=JSON.parse(fr.result); const incoming=obj.state||obj; if(!incoming||!incoming.records)throw new Error('无 records'); const count=Object.keys(incoming.records).length; U.confirm('导入学习记录','将覆盖当前记录，共 '+count+' 条。继续吗？').then(yes=>{ if(!yes)return; state=Object.assign({},JSON.parse(JSON.stringify(DEFAULT_STATE)),incoming); state.settings=Object.assign({},DEFAULT_STATE.settings,incoming.settings||{}); state.favorites=incoming.favorites||[]; state.activity=incoming.activity||{}; state.records=incoming.records||{}; state.drafts=incoming.drafts||{}; state.session=null; save(true); applyTheme(); U.toast('已导入 '+count+' 条记录'); renderRoute(); }); }catch(e){ U.toast('导入失败：文件格式不正确'); } }; fr.readAsText(f); };
    input.click();
  }
  async function resetData() {
    const yes=await U.confirm('清空全部学习记录','这会删除作答记录、错题本、收藏、活动统计和当前练习，且不可恢复。建议先导出备份。'); if(!yes)return;
    const yes2=await U.confirm('再次确认','确定要清空吗？'); if(!yes2)return;
    state.records={}; state.favorites=[]; state.activity={}; state.session=null; state.lastPractice=null; save(true); U.toast('记录已清空'); renderRoute();
  }
  function changeGoalModal() {
    const m=U.modal('<h2>设置每日目标</h2><p class="lede" style="font-size:13px;margin:8px 0 18px">每天完成多少道有效作答？</p><div class="row wrap">'+[5,10,20,30,50,100].map(n=>'<button class="chip '+(state.settings.dailyGoal===n?'active':'')+'" data-action="set-goal" data-goal="'+n+'">'+n+' 题</button>').join('')+'</div>');
  }

  /* ---------- route rendering ---------- */
  function renderRoute() {
    if (!QUESTIONS.length) return;
    route=parseHash();
    let html='';
    try {
      switch(route.name){
        case 'home': html=renderHome(); break;
        case 'practice': html=renderPractice(); break;
        case 'chapter': html=renderChapter(route.params.ch); break;
        case 'topic': html=renderTopic(route.params.id); break;
        case 'quiz': html=renderQuiz(); break;
        case 'knowledge': html=renderKnowledge(); break;
        case 'stats': html=renderStats(); break;
        case 'wrong': html=renderWrong(); break;
        case 'favorites': html=renderFavorites(); break;
        case 'sandbox': html=renderSandbox(route.params.qid); break;
        case 'docs': html=renderDocs(); break;
        case 'settings': html=renderSettings(); break;
        default: html=renderHome();
      }
    } catch(err) {
      console.error(err); html=pageShell('<div class="empty"><h3>页面加载出错</h3><p>'+U.esc(err.message)+'</p><button class="btn btn-primary" data-action="back">返回首页</button></div>');
    }
    const app=document.getElementById('app'); if(app) app.innerHTML=html;
    currentQuestionId = curQ()?curQ().id:null; currentQuestionStarted=Date.now();
    window.scrollTo({top:0,behavior:'auto'});
    const topnav=document.getElementById('topnav'); if(topnav) topnav.classList.toggle('scrolled',window.scrollY>4);
  }
  function ensureRouteData() {
    route=parseHash();
    if(route.name==='quiz' && (!state.session || !state.session.qids || !state.session.qids.length)) go('home');
  }
  window.addEventListener('hashchange',()=>{ renderRoute(); });
  window.addEventListener('scroll',()=>{ const n=document.getElementById('topnav'); if(n)n.classList.toggle('scrolled',window.scrollY>4); },{passive:true});

  /* ---------- global actions ---------- */
  document.addEventListener('click',function(e){
    const el=e.target.closest('[data-action]'); if(!el) return;
    const act=el.dataset.action;
    switch(act){
      case 'tab': go(el.dataset.tab); break;
      case 'back': if(history.length>1) history.back(); else go('home'); break;
      case 'open-settings': go('settings'); break;
      case 'open-sandbox': go('sandbox'); break;
      case 'open-search': go('practice'); setTimeout(()=>{const i=document.querySelector('[data-filter="q"]');if(i)i.focus();},80); break;
      case 'toggle-theme': state.settings.theme=state.settings.theme==='dark'?'light':'dark'; applyTheme(); save(); renderRoute(); break;
      case 'start-smart': { const list=smartPool(20); startSession(list.map(q=>q.id),'智能练习 · 20 题','smart'); break; }
      case 'start-wrong': startWrong(); break;
      case 'start-filtered': startFiltered(el.dataset.shuffle==='1'); break;
      case 'clear-filters': practiceFilter={chapter:'all',topic:'all',type:'all',diff:'all',status:'all',q:''}; renderRoute(); break;
      case 'practice-one': practiceOne(el.dataset.id); break;
      case 'practice-topic': practiceTopic(el.dataset.topic); break;
      case 'start-chapter': startChapter(Number(el.dataset.ch),false); break;
      case 'start-chapter-random': startChapter(Number(el.dataset.ch),true); break;
      case 'resume-last': if(state.lastPractice&&state.lastPractice.qids.length)startSession(state.lastPractice.qids,'继续 · '+state.lastPractice.title,'resume'); else U.toast('暂无可继续的练习'); break;
      case 'pick-option': pickOption(Number(el.dataset.i)); break;
      case 'pick-judge': pickJudge(el.dataset.v==='true'); break;
      case 'submit-answer': submitAnswer(); break;
      case 'reveal-answer': revealAnswer(); break;
      case 'next-question': nextQuestion(); break;
      case 'prev-question': prevQuestion(); break;
      case 'finish-session': finishSession(); break;
      case 'toggle-favorite': toggleFavorite(el.dataset.id); break;
      case 'open-map': { const d=document.getElementById('quiz-drawer'); if(d)d.classList.add('open'); break; }
      case 'close-map': { const d=document.getElementById('quiz-drawer'); if(d)d.classList.remove('open'); break; }
      case 'goto-question': { const s=state.session; if(s){ s.idx=Number(el.dataset.i); save(true); renderRoute(); } break; }
      case 'quit-session': U.confirm('退出练习','当前作答记录会保留，但本次练习进度会丢失。确定退出吗？').then(y=>{if(y){state.session=null;save(true);go('home');}}); break;
      case 'retry-wrong-list': { const ids=(el.dataset.ids||'').split(',').filter(Boolean); closeModalFromAction(el); if(ids.length)startSession(ids,'重练本次错题','wrong'); break; }
      case 'close-modal': closeModalFromAction(el); break;
      case 'change-goal': changeGoalModal(); break;
      case 'set-goal': state.settings.dailyGoal=Number(el.dataset.goal); save(true); const mb=el.closest('.modal-backdrop'); if(mb)mb.remove(); renderRoute(); U.toast('每日目标已更新'); break;
      case 'set-theme': state.settings.theme=el.dataset.theme; applyTheme(); save(true); renderRoute(); break;
      case 'toggle-setting': { const k=el.dataset.key; state.settings[k]=!state.settings[k]; el.classList.toggle('on',!!state.settings[k]); el.setAttribute('aria-checked',String(!!state.settings[k])); applyTheme(); save(); if(k==='showSource')renderRoute(); break; }
      case 'export-data': exportData(); break;
      case 'import-data': importData(); break;
      case 'reset-data': resetData(); break;
      case 'run-sandbox': runFreeSandbox(); break;
      case 'sandbox-reset': {state.sandbox={code:EXAMPLES[0].code,stdin:''};save();renderRoute();break;}
      case 'sandbox-clear': {state.sandbox={code:'#include <iostream>\nusing namespace std;\n\nint main() {\n    \n    return 0;\n}\n',stdin:''};save();renderRoute();break;}
      case 'sandbox-example': { const ex=EXAMPLES[Number(el.dataset.i)]; state.sandbox={code:ex.code,stdin:ex.stdin}; pendingProgram['__sandbox__']=null; save(); renderRoute(); break; }
      case 'sandbox-load-stdin': { const ex=EXAMPLES[0]; const t=document.getElementById('sandbox-stdin'); if(t)t.value=ex.stdin; state.sandbox=sandboxDraft(); state.sandbox.stdin=ex.stdin; save(); U.toast('已载入示例输入'); break; }
      case 'run-prog': { const q=curQ(); if(q&&q.type==='programming')runProgram(q,false); break; }
      case 'judge-prog': { const q=curQ(); if(q&&q.type==='programming')runProgram(q,true); break; }
      case 'reset-prog': { const q=QID[el.dataset.id]; if(q){state.drafts[q.id]={code:q.starter,stdin:(q.tests[0]&&q.tests[0].input)||''};pendingProgram[q.id]=null;save();renderRoute();U.toast('已恢复初始代码');} break; }
      case 'load-sample': { const q=QID[el.dataset.id]; if(q){progDraft(q).stdin=(q.tests[0]&&q.tests[0].input)||'';save();const t=document.getElementById('prog-stdin-'+q.id);if(t)t.value=progDraft(q).stdin;U.toast('已载入样例输入');} break; }
      case 'prog-beautify': { const q=QID[el.dataset.id]; const ta=document.getElementById('prog-code-'+q.id); if(ta){ta.value=ta.value.split('\n').map(x=>x.replace(/\s+$/,'')).join('\n'); progDraft(q).code=ta.value; save(); updateLineNumbers('prog-lines-'+q.id,ta.value);} break; }
    }
  });
  document.addEventListener('input',function(e){
    const t=e.target;
    if(t.dataset&&t.dataset.action==='prog-code'){ const q=QID[t.dataset.id]; if(q){progDraft(q).code=t.value; save(); updateLineNumbers('prog-lines-'+q.id,t.value);} }
    if(t.dataset&&t.dataset.action==='prog-stdin'){ const q=QID[t.dataset.id]; if(q){progDraft(q).stdin=t.value; save();} }
    if(t.id==='sandbox-code'){ const d=sandboxDraft(); d.code=t.value; save(); updateLineNumbers('sandbox-lines',t.value); }
    if(t.id==='sandbox-stdin'){ const d=sandboxDraft(); d.stdin=t.value; save(); }
    if(t.dataset&&t.dataset.action==='fill-input'){ const q=curQ(); if(q){const d=getDraft(q);d[Number(t.dataset.i)]=t.value;save();updateSubmitState();} }
    if(t.dataset&&t.dataset.filter==='q'){ practiceFilter.q=t.value; U.debounce(refreshPracticeResults,120)(); }
    if(t.id==='knowledge-search'){ practiceFilter.kq=t.value; refreshKnowledgeResults(); }
  });
  document.addEventListener('change',function(e){
    const t=e.target; if(!t.dataset||!t.dataset.filter)return;
    const key=t.dataset.filter; practiceFilter[key]=t.value;
    if(key==='chapter'&&practiceFilter.topic!=='all'&&TOPICS[practiceFilter.topic]&&String(TOPICS[practiceFilter.topic].chapter)!==String(t.value))practiceFilter.topic='all';
    renderRoute();
  });
  function refreshKnowledgeResults(){
    const q=(practiceFilter.kq||'').toLowerCase();
    const list=KNOWLEDGE.filter(k=>!q||(k.title+' '+k.summary+' '+(k.points||[]).join(' ')+' '+k.source).toLowerCase().includes(q));
    const grid=document.getElementById('knowledge-grid'); if(!grid)return;
    grid.innerHTML=list.map(k=>{const ts=topicStats(k.id);return '<article class="k-card"><div class="row between"><span class="pill accent">第 '+k.chapter+' 章 · '+U.esc(k.section)+'</span><span class="tiny muted">'+ts.total+' 题</span></div><h3 style="margin-top:10px">'+U.esc(k.title)+'</h3><div class="k-meta">来源：'+U.esc(k.source)+' · '+U.esc(k.slides)+'</div><p>'+U.esc(k.summary)+'</p><ul class="k-points">'+k.points.slice(0,3).map(p=>'<li>'+U.esc(p)+'</li>').join('')+'</ul><div class="k-foot"><span class="tiny muted">'+(ts.attempts?'正确率 '+ts.accuracy+'% · 已做 '+ts.done+'/'+ts.total:'尚未练习')+'</span><div class="row"><a class="btn btn-ghost btn-sm" href="#/topic/'+encodeURIComponent(k.id)+'">详情</a><button class="btn btn-soft btn-sm" data-action="practice-topic" data-topic="'+U.attr(k.id)+'">练习</button></div></div></article>';}).join('');
    const count=document.querySelector('.filter-panel .result-count b'); if(count)count.textContent=list.length;
  }
  function updateLineNumbers(id,code){ const el=document.getElementById(id); if(el)el.innerHTML=code.split('\n').map((_,i)=>'<span>'+(i+1)+'</span>').join(''); }

  /* ---------- keyboard ---------- */
  document.addEventListener('keydown',function(e){
    const tag=(e.target.tagName||'').toLowerCase();
    const editing=tag==='input'||tag==='textarea'||tag==='select'||e.target.isContentEditable;
    if((e.ctrlKey||e.metaKey)&&e.key==='Enter'){
      if(document.getElementById('sandbox-code')){e.preventDefault();runFreeSandbox();return;}
      const q=curQ(); if(q&&q.type==='programming'){e.preventDefault();runProgram(q,false);return;}
    }
    if(e.key==='/'&&!editing){ const box=document.querySelector('[data-filter="q"]'); if(box){e.preventDefault();box.focus();} else {go('practice');setTimeout(()=>{const b=document.querySelector('[data-filter="q"]');if(b)b.focus();},80);} return; }
    if(route.name!=='quiz')return;
    const q=curQ(); if(!q)return;
    const answered=state.session.answers[q.id]!==undefined;
    if(e.key==='Enter'){
      if(editing&&tag!=='input')return;
      if(!answered&&q.type!=='programming'){e.preventDefault();submitAnswer();return;}
      if(answered){e.preventDefault();nextQuestion();}
      return;
    }
    if(answered&&e.key==='ArrowRight'&&!editing){e.preventDefault();nextQuestion();return;}
    if(e.key==='ArrowLeft'&&!editing){e.preventDefault();prevQuestion();return;}
    if(!answered&&!editing&&/^[1-9]$/.test(e.key)){
      const n=Number(e.key);
      if(q.type==='single'||q.type==='multiple'||q.type==='code'){if(n<=(q.options||[]).length){e.preventDefault();pickOption(n-1);}}
      else if(q.type==='judge'&&n<=2){e.preventDefault();pickJudge(n===1);}
    }
  });

  /* ---------- boot ---------- */
  function showBootError(err){
    const app=document.getElementById('app');
    if(app) app.innerHTML='<div class="shell"><div class="empty" style="padding-top:12vh"><div class="empty-ic">'+U.icon('terminal')+'</div><h3>题库加载失败</h3><p style="max-width:540px;margin:0 auto 18px">'+U.esc(err&&err.message||'未知错误')+'。如果你是本地直接双击打开 index.html，浏览器会阻止读取 JSON；请按 README 使用本地静态服务器。</p><button class="btn btn-primary" data-action="reload">重新加载</button></div></div>';
  }
  async function boot(){
    applyTheme();
    const app=document.getElementById('app'); if(app)app.innerHTML='<div class="loading-screen"><div style="text-align:center"><div class="loader" style="margin:0 auto 14px"></div><div class="small muted">正在加载 297 道题与知识点…</div></div></div>';
    try{
      await loadData();
      if(!state.sandbox) state.sandbox={code:EXAMPLES[0].code,stdin:''};
      ensureRouteData();
      renderRoute();
      if('serviceWorker' in navigator && location.protocol.startsWith('http')) navigator.serviceWorker.register('./sw.js').catch(()=>{});
      window.__CPPLAB={state,QUESTIONS,KNOWLEDGE,QID,go,render:renderRoute,grade:U.grade};
    }catch(err){ console.error(err); showBootError(err); }
  }
  document.addEventListener('click',function(e){ if(e.target.closest('[data-action="reload"]')) location.reload(); });
  boot();
})();

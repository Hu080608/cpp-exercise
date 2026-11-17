#!/usr/bin/env node
/* 生成：知识点清单 Markdown、可打印速查、题库 JSON 下载包 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const ROOT = path.resolve(__dirname, '..');
const sandbox = { window: {} };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(path.join(ROOT, 'data/knowledge.js'), 'utf8'), sandbox);
const KB = sandbox.window.CPP_KNOWLEDGE;
const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/questions/manifest.json'), 'utf8'));
let questions = [];
for (const ch of manifest.chapters) {
  questions = questions.concat(JSON.parse(fs.readFileSync(path.join(ROOT, `data/questions/ch${ch}.json`), 'utf8')).questions);
}
const chapterTitles = {
  1: '程序和 C++ 基础', 2: '数据与表达式', 3: '流程控制', 4: '函数与过程抽象', 5: '复合数据类型'
};
function mdEscape(s) { return String(s).replace(/\|/g, '\|').replace(/\n/g, '<br>'); }
let md = `# C++ 程序设计 · 知识点清单\n\n> 唯一知识来源：本地「程序设计」文件夹内课程 PPT（第01章～第05章）。\n> 题库中每道题的 \`source\` 字段均回指本清单与原始 PPT 页码；未在 PPT 出现的语言特性不进入题目。\n\n## 覆盖统计\n\n- 知识点：${KB.length} 个\n- 题目：${questions.length} 道\n- 题型：单选、多选、判断、填空、代码阅读、编程（6 种）\n- 难度：入门、简单、中等、困难（4 档）\n\n---\n\n`;
const byChapter = {};
KB.forEach(k => (byChapter[k.chapter] = byChapter[k.chapter] || []).push(k));
for (const ch of Object.keys(byChapter).sort()) {
  md += `## 第 ${ch} 章 · ${chapterTitles[ch]}\n\n`;
  for (const k of byChapter[ch]) {
    const qs = questions.filter(q => q.topicId === k.id);
    const types = [...new Set(qs.map(q => q.type))].map(t => ({single:'单选',multiple:'多选',judge:'判断',fill:'填空',code:'代码阅读',programming:'编程'}[t] || t));
    const diffs = [...new Set(qs.map(q => q.difficulty))].sort().map(d => ({1:'入门',2:'简单',3:'中等',4:'困难'}[d] || d));
    md += `### ${k.id} ${k.title}\n\n`;
    md += `- **来源**：\`${k.source}\` · ${k.slides}\n`;
    md += `- **课程章节**：${k.section}\n`;
    md += `- **题库**：${qs.length} 题（${types.join('、')}；难度 ${diffs.join('、')}）\n\n`;
    md += `${k.summary}\n\n**核心知识点**\n\n`;
    k.points.forEach(p => { md += `- ${p}\n`; });
    md += `\n**易错提醒**\n\n`;
    k.pitfalls.forEach(p => { md += `- ${p}\n`; });
    md += `\n---\n\n`;
  }
}
md += `## 范围边界（硬性约束）\n\n`;
md += `- 不考 STL 容器（vector、string、map 等）：PPT 未系统讲解。\n`;
md += `- 不考异常处理的语法细节：仅在「C 与 C++ 区别」一页出现 try/throw/catch 概述，题库不以异常语法为考点。\n`;
md += `- 不考模板与泛型编程：PPT 仅在概述中提及模板，未展开语法。\n`;
md += `- 不考文件流、类与对象语法：本课程 PPT 第 1–5 章未系统讲解。\n`;
md += `- 字符串仅考 C 风格字符数组与 PPT 列出的 cstring 函数。\n`;
md += `- 指针、引用、动态内存、函数指针、Lambda、范围 for、auto 等均按 PPT 第 4–5 章出现范围命题。\n`;
fs.writeFileSync(path.join(ROOT, 'docs/KNOWLEDGE_POINTS.md'), md, 'utf8');
fs.writeFileSync(path.join(ROOT, 'downloads/knowledge-points.md'), md, 'utf8');
const all = {
  app: 'cpp-lab-question-bank', version: 2, source: '程序设计课程 PPT 第01–05章',
  generatedAt: new Date().toISOString(), count: questions.length, knowledge: KB, questions
};
fs.writeFileSync(path.join(ROOT, 'downloads/question-bank.json'), JSON.stringify(all, null, 2), 'utf8');

// 编程题专项题库
const progQuestions = questions.filter(q => q.type === 'programming');
fs.writeFileSync(path.join(ROOT, 'downloads/programming-bank.json'), JSON.stringify({
  app: 'cpp-lab-programming-bank', version: 2, count: progQuestions.length,
  source: '程序设计课程 PPT 第1–5章 + 原创/经典题情境改编',
  generatedAt: new Date().toISOString(), questions: progQuestions
}, null, 2), 'utf8');
let pmd = `# 编程题专项题库

> ${progQuestions.length} 道编程题，全部只使用课程 PPT 第 1–5 章讲过的语言特性。
> 题目情境包含原创题与经典题（洛谷/力扣等）改编；每题均附初始代码、测试用例和 PPT 知识点来源。

`;
for (const d of [1,2,3,4]) {
  pmd += `## ${['','入门','简单','中等','困难'][d]}

`;
  for (const q of progQuestions.filter(x=>x.difficulty===d)) {
    pmd += `### ${q.id} ${q.stem}

`;
    pmd += `- 章节/知识点：第 ${q.chapter} 章 · ${q.knowledge}
`;
    pmd += `- 题目来源：${q.origin || '课程综合编程'}
`;
    pmd += `- 测试用例：${q.tests.length} 组（${q.tests.filter(t=>t.hidden).length} 组隐藏）
`;
    pmd += `- PPT 来源：${q.source}

`;
  }
}
fs.writeFileSync(path.join(ROOT, 'docs/PROGRAMMING_BANK.md'), pmd, 'utf8');

console.log(`Generated KNOWLEDGE_POINTS.md (${KB.length} topics), question-bank.json (${questions.length} questions), programming-bank.json (${progQuestions.length} problems)`);

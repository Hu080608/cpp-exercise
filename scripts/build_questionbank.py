#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""汇总章节题库 -> data/questions/*.json，并做知识点/字段/覆盖矩阵校验。"""
import json, os, re, sys, shutil, subprocess
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import qcommon
import questions_ch1, questions_ch2, questions_ch3, questions_ch4, questions_ch5, questions_extra, questions_prog_extra, questions_prog_100

KNOWLEDGE = {}
with open(os.path.join(ROOT, "data", "knowledge.js"), encoding="utf-8") as f:
    src = f.read()
for m in re.finditer(r'id:\s*"([^"]+)"[\s\S]*?chapter:\s*(\d+)[\s\S]*?section:\s*"([^"]+)"[\s\S]*?title:\s*"([^"]+)"[\s\S]*?source:\s*"([^"]+)"[\s\S]*?slides:\s*"([^"]+)"', src):
    KNOWLEDGE[m.group(1)] = {"chapter": int(m.group(2)), "section": m.group(3), "title": m.group(4), "source": m.group(5), "slides": m.group(6)}

CLANG_FORMAT = shutil.which('clang-format')
FORMAT_STYLE = '{BasedOnStyle: Google, IndentWidth: 4, ColumnLimit: 0, AllowShortFunctionsOnASingleLine: None, AllowShortIfStatementsOnASingleLine: false, AllowShortLoopsOnASingleLine: false, BreakBeforeBraces: Attach}'

def pretty_cpp(code):
    """用 clang-format 生成参考解展示版；未安装时保留原解。"""
    code = str(code or '').strip()
    if not CLANG_FORMAT:
        return code + ('\n' if code else '')
    try:
        r = subprocess.run([CLANG_FORMAT, '--style=' + FORMAT_STYLE, '--assume-filename=main.cpp'],
                           input=code + '\n', text=True, capture_output=True, timeout=10)
        return (r.stdout or code).strip() + '\n'
    except Exception:
        return code + '\n'

TYPE_ORDER = ["single", "multiple", "judge", "fill", "code", "programming"]
DIFFS = [1, 2, 3, 4]
seen = set()
by_ch = defaultdict(list)
for i, item in enumerate(qcommon.QUESTIONS, 1):
    qid = "q%03d" % i
    item = dict(item)
    item["id"] = qid
    item["typeName"] = qcommon.TYPE_NAMES[item["type"]]
    item["difficultyName"] = qcommon.DIFF_NAMES[item["difficulty"]]
    tid = item["topicId"]
    if tid not in KNOWLEDGE:
        raise SystemExit("未知知识点 topicId=%s，题目=%s" % (tid, item["stem"][:40]))
    k = KNOWLEDGE[tid]
    item["chapter"] = k["chapter"]
    item["knowledge"] = k["title"]
    item.setdefault("source", k["source"] + " · " + k["slides"])
    if item.get("type") == "programming":
        item.setdefault("origin", "原创编程题 · 课程知识点综合")
        item["solutionPretty"] = pretty_cpp(item.get("solution", ""))
    if qid in seen:
        raise SystemExit("重复题号 " + qid)
    seen.add(qid)
    by_ch[k["chapter"]].append(item)

os.makedirs(os.path.join(ROOT, "data", "questions"), exist_ok=True)
all_q = []
for ch in sorted(by_ch):
    out = {
        "chapter": ch,
        "questions": by_ch[ch],
    }
    path = os.path.join(ROOT, "data", "questions", "ch%d.json" % ch)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    all_q.extend(by_ch[ch])

with open(os.path.join(ROOT, "data", "questions", "manifest.json"), "w", encoding="utf-8") as f:
    json.dump({"chapters": sorted(by_ch), "count": len(all_q), "generatedBy": "scripts/build_questionbank.py"}, f, ensure_ascii=False, indent=2)

matrix = Counter((q["type"], q["difficulty"]) for q in all_q)
missing = [(t, d) for t in TYPE_ORDER for d in DIFFS if matrix[(t, d)] == 0]
topics = Counter(q["topicId"] for q in all_q)

print("题目总数:", len(all_q))
print("各章题量:", {ch: len(by_ch[ch]) for ch in sorted(by_ch)})
print("题型 × 难度矩阵:")
for t in TYPE_ORDER:
    print("  %-12s" % t, " ".join("%s:%d" % (qcommon.DIFF_NAMES[d], matrix[(t, d)]) for d in DIFFS))
print("知识点覆盖:", len(topics), "/", len(KNOWLEDGE))
if missing:
    print("警告：缺少组合", missing, file=sys.stderr)
    sys.exit(1)
if set(topics) != set(KNOWLEDGE):
    print("警告：未覆盖知识点", set(KNOWLEDGE) - set(topics), file=sys.stderr)
    sys.exit(1)
print("校验通过：24 个题型×难度组合无空缺，29 个知识点均有题。")

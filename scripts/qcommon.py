"""题库构建公共工具。题目数据由 scripts/build_questionbank.py 汇总为 JSON。"""

TYPE_NAMES = {
    "single": "单选题", "multiple": "多选题", "judge": "判断题",
    "fill": "填空题", "code": "代码阅读题", "programming": "编程题",
}
DIFF_NAMES = {1: "入门", 2: "简单", 3: "中等", 4: "困难"}

QUESTIONS = []

def q(**kw):
    """注册一道题并做字段级检查。"""
    required = ["chapter", "section", "topicId", "type", "difficulty", "stem", "explain", "source"]
    for k in required:
        if k not in kw:
            raise ValueError("missing %s in %r" % (k, kw))
    t = kw["type"]
    if t not in TYPE_NAMES:
        raise ValueError("bad type " + t)
    if kw["difficulty"] not in (1, 2, 3, 4):
        raise ValueError("bad difficulty")
    kw.setdefault("topic", "")
    kw.setdefault("tags", [])
    if t in ("single", "multiple", "code"):
        if "options" not in kw or "answer" not in kw:
            raise ValueError("choice question missing options/answer: " + kw["stem"][:30])
        if t == "multiple":
            if not isinstance(kw["answer"], list) or not kw["answer"]:
                raise ValueError("multiple answer must be non-empty list")
        elif not isinstance(kw["answer"], int):
            raise ValueError("single/code answer must be int")
    if t == "judge" and not isinstance(kw["answer"], bool):
        raise ValueError("judge answer must be bool")
    if t == "fill":
        if not isinstance(kw.get("answer"), list) or not kw["answer"]:
            raise ValueError("fill answer must be list")
        kw.setdefault("alt", [[] for _ in kw["answer"]])
    if t == "programming":
        if not kw.get("starter") or not kw.get("solution") or not kw.get("tests"):
            raise ValueError("programming question incomplete: " + kw["stem"][:30])
        for test in kw["tests"]:
            if "input" not in test or "output" not in test:
                raise ValueError("programming test missing input/output")
    QUESTIONS.append(kw)
    return kw


def match_all(correct, chosen):
    return sorted(correct) == sorted(chosen)

# C++ Lab · 程序设计练习场

一个面向「程序设计」课程的 C++ 在线练习网站，功能对齐参考站 [cpp-quiz-690](https://cpp-quiz-690.netlify.app) 并做了明显增强：六种题型、四档难度、编程训练场、29 个知识点、347 道题、67 道编程题、多条件筛选、错题本、收藏夹、学习统计，以及**能在页面里真实编译运行 C++ 的沙箱和编程题自动评测**。

目标仓库与 GitHub Pages 地址：

- 仓库：<https://github.com/Hu080608/cpp-exercise>
- Pages：<https://hu080608.github.io/cpp-exercise/>

> 知识范围严格来自本地「程序设计」文件夹中的课程 PPT（第01章～第05章）。完整知识点清单及每道题的 PPT 来源见 [docs/KNOWLEDGE_POINTS.md](docs/KNOWLEDGE_POINTS.md)。

---

## 1. 项目结构

```text
cpp-exercise/
├─ index.html                     # 唯一入口（纯静态）
├─ 404.html                       # GitHub Pages 404 回退
├─ manifest.webmanifest           # PWA manifest
├─ sw.js                          # Service Worker 离线壳
├─ assets/
│  ├─ css/style.css               # 全站样式（响应式 + 深浅色）
│  └─ js/
│     ├─ utils.js                 # DOM/图标/本地存储/填空判分/弹层
│     ├─ sandbox.js               # Wandbox C++ 编译运行封装
│     └─ app.js                   # 路由、题库、练习、统计、编程题评测
├─ data/
│  ├─ knowledge.js                # 29 个知识点（唯一知识清单）
│  ├─ downloads.js                # 资料下载清单
│  └─ questions/
│     ├─ manifest.json            # 题库索引
│     ├─ ch1.json … ch5.json      # 按章拆分的题库（与代码分离）
├─ docs/
│  ├─ KNOWLEDGE_POINTS.md         # 知识点清单（含来源 PPT / slide）
│  ├─ PROGRAMMING_BANK.md         # 编程题专项清单（按难度/来源）
│  ├─ REFERENCE_FEATURE_MATRIX.md # 参考站功能对照表
│  └─ PPT_AMBIGUITIES.md          # PPT 歧义与处理方案
├─ downloads/
│  ├─ question-bank.json          # 完整题库导出（含答案/解析/测试用例）
│  ├─ programming-bank.json       # 67 道编程题专项导出
│  ├─ knowledge-points.md         # 可打印知识点速查
│  └─ wrongbook-template.md       # 错题复盘模板
├─ scripts/
│  ├─ qcommon.py                  # 题目构建公共函数
│  ├─ questions_ch1.py … ch5.py   # 章节题库源
│  ├─ questions_extra.py          # 矩阵补全题
│  ├─ questions_prog_extra.py     # 50 道综合编程题（原创/经典题改编）
│  ├─ build_questionbank.py       # 生成 JSON + 覆盖矩阵校验
│  ├─ test_programming.py         # 用本机 g++ 回归测试编程题标准解
│  ├─ audit_code_questions.py     # 代码阅读题输出抽查
│  └─ export_docs.js              # 生成知识点清单/题库下载包
└─ .github/workflows/pages.yml    # GitHub Pages 自动发布
```

**题库数据与代码分离**：页面只读取 `data/questions/*.json` 和 `data/knowledge.js`。增删题目无需修改 `app.js`。

---

## 2. 本地运行

因为浏览器会阻止 `file://` 页面读取 JSON，请使用任意静态服务器。

```bash
cd cpp-exercise

# 方式一：Python
python -m http.server 8080

# 方式二：Node
npx serve .
```

打开 <http://localhost:8080>。

> 沙箱与编程题评测需要联网：前端会把源码和 stdin 发送到 Wandbox 公共编译 API（CORS 可用），不需要自建后端。题目、知识点、错题本、统计与本地进度均可离线使用。

### 题库构建与校验

```bash
# 从 scripts/questions_*.py 重新生成 data/questions/*.json
python scripts/build_questionbank.py

# 校验全部编程题标准解（需要本机 g++ 和 C++17）
python scripts/test_programming.py

# 生成知识点清单、可打印速查、题库下载包
node scripts/export_docs.js
```

`build_questionbank.py` 会检查：

- 题号唯一、字段完整；
- 每个 `topicId` 都能在 `data/knowledge.js` 中找到；
- **6 种题型 × 4 档难度 = 24 个组合无空缺**；
- 29 个知识点全部有题。
- 编程题专项：67 道，覆盖 12 / 27 / 22 / 6（入门/简单/中等/困难）。

---

## 3. 部署到 GitHub Pages

### 方式 A：GitHub Actions（推荐，仓库已带 workflow）

1. 把代码推送到 `main` 分支。
2. 打开仓库 **Settings → Pages**。
3. 在 **Build and deployment → Source** 选择 **GitHub Actions**。
4. 推送后自动运行 `.github/workflows/pages.yml`，发布整个静态站点到 Pages。
5. 访问 `https://hu080608.github.io/cpp-exercise/`。

### 方式 B：从分支直接发布

1. 将代码推送到 `main`。
2. **Settings → Pages → Source** 选择 `Deploy from a branch`。
3. 分支选 `main`，目录选 `/ (root)`，保存。
4. GitHub Pages 会直接以根目录作为站点。

本项目不依赖构建工具、不需要 `npm install`，因此两种方式都能直接使用。

---

## 4. 功能说明

### 题库与练习

- **题型**：单选、多选、判断、填空、代码阅读、编程。
- **难度**：入门、简单、中等、困难，全部可在筛选器中筛选。
- **筛选维度**：章节、知识点、题型、难度、作答状态（未做/已做/错题/已掌握/收藏）、关键词。
- **即时反馈**：提交后显示对错、正确答案、完整解析与 PPT 来源。
- **填空判分**：自动统一全角/半角、空白符、行末分号、`std::` 前缀、常见类型转换等价写法；每题还可配置备选答案。
- **键盘操作**：`1–6` 选项，`T/F`/选项数字判断，`Enter` 提交/下一题，`←/→` 切题，`/` 搜索，`Ctrl+Enter` 运行沙箱。
- **自动保存**：作答、收藏、草稿、当前练习进度都写入 localStorage；刷新后可恢复。
- **错题本**：答错自动收录；连续答对 2 次自动移出。
- **收藏夹**：任意题目可收藏并单独重练。

### C++ 沙箱

- 编辑 C++ 源码、输入自定义 stdin、编译并运行。
- 显示编译错误、运行输出、stderr、耗时；对常见 GCC 错误给出中文排查提示。
- 编程题可载入初始代码，运行样例，提交后逐个测试用例显示通过状态；提交或看答案后，编辑区、运行和重新评测仍可使用。

- 代码编辑区支持 `Tab` 插入 4 个空格、`Shift+Tab` 删除缩进，沙箱和编程题共用同一套编辑器行为。
- 编程题标准解与测试用例在 `data/questions/*.json` 中，`scripts/test_programming.py` 会实际编译验证。

### 视觉与响应式

- 桌面端最大 1200px 双栏/三栏布局；移动端底部导航 + 单列卡片。
- 浅色/深色/跟随系统三种主题；支持减少动效。
- 题目地图、筛选面板、代码编辑器、控制台均适配手机宽度。
- PWA 离线壳：断网时仍可打开已缓存页面和题库（编译功能需联网）。

---

## 5. 新增题目

1. 在 `scripts/questions_chN.py` 中用 `q(...)` 添加题目。字段示例：

```python
q(
  chapter=3, section="3.4", topicId="3.3", type="single", difficulty=2,
  stem="题干……",
  options=["A 选项", "B 选项", "C 选项", "D 选项"],
  answer=1,
  explain="为什么对、为什么错……",
  source="第03章.pptx · 3.4 循环结构（slide 38）"
)
```

2. 编程题需要额外提供 `starter`、`solution`、`tests`：

```python
q(
  chapter=4, section="4.4", topicId="4.4", type="programming", difficulty=2,
  stem="……", starter="...", solution="...",
  tests=[{"input":"5\n","output":"120"}, {"input":"1\n","output":"1","hidden":True}],
  explain="……", source="……"
)
```

3. 运行：

```bash
python scripts/build_questionbank.py
python scripts/test_programming.py
node scripts/export_docs.js
```

4. 若新增了**新知识点**，必须先在 `data/knowledge.js` 中登记，并提供 `source` 与 `slides`；构建脚本会拒绝未知 `topicId`。

---

## 6. 知识范围与边界

- 唯一知识来源：`程序设计/` 下的 9 个 PPT 文件。
- PPT 中只被提及、未系统讲解的模板、异常处理细节、STL 容器、类与对象语法等**不进入题库**。
- 详细边界与对 PPT 歧义的处理见 [docs/PPT_AMBIGUITIES.md](docs/PPT_AMBIGUITIES.md)。
- 每道题解析均附 `source` 字段（PPT 文件名 + 章节/slide）。

## 7. 参考站对照

逐项功能对照、实现状态与超越点见 [docs/REFERENCE_FEATURE_MATRIX.md](docs/REFERENCE_FEATURE_MATRIX.md)。

## 8. 技术说明

- 无构建、无框架、无依赖；原生 HTML/CSS/JavaScript。
- 题库 JSON 由 Python 构建脚本从易维护的 Python 源生成。
- 沙箱使用 [Wandbox API](https://wandbox.org/api/compile.json)（公共 CORS 编译服务），默认 `gcc-head`、`-std=c++17`。如果公共 API 不可用，页面会显示可读的联网/服务错误提示，不影响刷题功能。
- 所有编程题标准解均用本机 g++ 实际编译运行验证；代码阅读题抽样结果也通过脚本核对。

## 9. 许可

仅用于课程学习与复习。PPT 内容版权归原课程作者所有；本站题目为原创练习内容。

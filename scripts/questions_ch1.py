# -*- coding: utf-8 -*-
from qcommon import q

# ======================= 第 1 章 =======================
q(chapter=1, section="1.1", topicId="1.1", type="single", difficulty=1,
  stem="程序（Program）通常被描述为下列哪两项的结合？",
  options=["算法 + 数据结构", "CPU + 内存", "源程序 + 可执行文件", "硬件 + 操作系统"],
  answer=0,
  explain="PPT 第01章 1.2 节指出：程序 = 算法 + 数据结构。算法描述对数据的加工处理步骤，数据结构描述待处理的数据。CPU、内存等是运行程序的硬件基础，不是程序本身的组成公式。",
  source="第01章.pptx · 1.2 程序设计概述（slide 24）")

q(chapter=1, section="1.1", topicId="1.1", type="single", difficulty=2,
  stem="冯·诺依曼计算机的逻辑结构包含五个基本单元。下列哪一项不属于这五个单元？",
  options=["存储单元", "运算单元", "控制单元", "网络路由单元"],
  answer=3,
  explain="五个单元是存储、运算、控制、输入、输出。网络路由单元不是冯·诺依曼机的基本逻辑组成；输入/输出由外设完成，网络通信只是外设功能的一种应用。",
  source="第01章.pptx · 1.1 计算机的工作原理（slide 12）")

q(chapter=1, section="1.1", topicId="1.1", type="multiple", difficulty=2,
  stem="关于冯·诺依曼“存储程序”思想，下列说法正确的有？",
  options=["程序要先装入存储单元，然后才能逐条执行", "指令和数据都以二进制形式存放在存储器中", "控制单元负责逐条取出指令并控制执行", "程序运行时不需要输入设备参与任何数据来源"],
  answer=[0, 1, 2],
  explain="存储程序思想强调程序与数据一起放入存储器，由控制单元逐条取指执行，所以 A、B、C 正确。程序运行中仍可以从输入单元获得数据，D 错误。",
  source="第01章.pptx · 1.1 计算机的工作原理（slide 12）")

q(chapter=1, section="1.1", topicId="1.1", type="multiple", difficulty=3,
  stem="下列软件中，属于系统软件或支撑软件的有？",
  options=["操作系统", "设备驱动程序", "集成开发环境（IDE）", "人口普查业务系统"],
  answer=[0, 1, 2],
  explain="操作系统和设备驱动程序直接让硬件发挥作用，属于系统软件；IDE 支持软件开发与维护，属于支撑软件。人口普查业务系统面向特定领域，属于应用软件。",
  source="第01章.pptx · 1.1 计算机的工作原理（slide 13）")

q(chapter=1, section="1.1", topicId="1.1", type="judge", difficulty=1,
  stem="计算机的功能主要由硬件决定，而性能主要由软件提供。",
  answer=False,
  explain="PPT 的表述恰好相反：一台计算机的性能和基本指令主要由硬件决定，而它的功能主要由软件提供。硬件提供执行能力，软件决定用这些能力完成什么任务。",
  source="第01章.pptx · 1.1 计算机的工作原理（slide 7）")

q(chapter=1, section="1.1", topicId="1.1", type="judge", difficulty=2,
  stem="Cache 利用程序访问的局部性，把可能要访问的内容预先从低速设备取到高速设备中，从而减少访问低速设备的次数。",
  answer=True,
  explain="这正是 cache 的基本思想。CPU 与内存、内存与外存之间存在速度差，利用时间局部性和空间局部性设置高速缓存可以减少等待。",
  source="第01章.pptx · 1.1 计算机的工作原理（slide 12）")

q(chapter=1, section="1.1", topicId="1.1", type="fill", difficulty=1,
  stem="程序的经典组成公式是：程序 = ____ + 数据结构。请填写缺失的一项。",
  answer=["算法"],
  explain="PPT 明确给出“程序 = 算法 + 数据结构”。算法是处理步骤，数据结构是数据的组织方式，两者共同构成程序。",
  source="第01章.pptx · 1.2 程序设计概述（slide 24）")

q(chapter=1, section="1.1", topicId="1.1", type="fill", difficulty=2,
  stem="冯·诺依曼计算机中，负责“逐条取出指令并控制其它单元执行”的单元是____单元。",
  answer=["控制"],
  alt=[["控制器"]],
  explain="控制单元根据指令向其它单元发出控制信号并控制程序执行流程；运算单元负责算术/逻辑运算，存储单元保存程序和数据。",
  source="第01章.pptx · 1.1 计算机的工作原理（slide 12）")

q(chapter=1, section="1.1", topicId="1.1", type="code", difficulty=3,
  stem="阅读下面的伪代码，程序执行结束后输出是什么？",
  code=["x = 2", "y = 3", "x = y", "y = x", "输出 x, y"],
  options=["2 3", "3 2", "3 3", "2 2"],
  answer=2,
  explain="x = y 后 x 变成 3；随后 y = x 使用的是已经更新后的 x=3，因此 y 也为 3。变量赋值会覆盖原值，不是交换。",
  source="第01章.pptx · 1.2 程序设计概述（slide 24）；变量赋值见第02章 2.3")

q(chapter=1, section="1.2", topicId="1.2", type="single", difficulty=1,
  stem="十进制整数 13 转换成二进制是？",
  options=["1011", "1101", "1110", "1001"],
  answer=1,
  explain="除 2 取余逆序：13÷2 余 1，6÷2 余 0，3÷2 余 1，1÷2 余 1，逆序得到 1101。",
  source="第01章.pptx · 1.1 数制转换（slide 16）")

q(chapter=1, section="1.2", topicId="1.2", type="single", difficulty=2,
  stem="二进制数 (101101.11)₂ 转换成八进制是？",
  options=["(55.6)₈", "(45.6)₈", "(55.3)₈", "(65.6)₈"],
  answer=0,
  explain="以小数点为界，向左每 3 位分组：101 101 → 5 5；向右补足 3 位：110 → 6。所以结果是 (55.6)₈。",
  source="第01章.pptx · 1.1 进制互转（slide 19）")

q(chapter=1, section="1.2", topicId="1.2", type="single", difficulty=2,
  stem="8 位补码 11110100 表示的十进制整数是？",
  options=["-12", "-11", "244", "-244"],
  answer=0,
  explain="最高位为 1，是负数。按补码求值：取反得 00001011，再加 1 得 00001100，即 12，因此原数是 -12。",
  source="第01章.pptx · 1.1 补码（slide 22）")

q(chapter=1, section="1.2", topicId="1.2", type="multiple", difficulty=2,
  stem="关于整数的原码、反码和补码，下列说法正确的有？",
  options=["正数的原码、反码、补码相同", "8 位补码能表示 -128", "补码中 0 只有一种表示", "负数的补码等于原码除符号位外按位取反"],
  answer=[0, 1, 2],
  explain="正数三种表示相同；8 位补码范围是 -128～127；补码的 0 唯一。负数补码是“反码加 1”，而 D 描述的是反码，不是补码。",
  source="第01章.pptx · 1.1 原码、反码、补码（slide 20–23）")

q(chapter=1, section="1.2", topicId="1.2", type="multiple", difficulty=3,
  stem="下列进制转换结果正确的有？",
  options=["(29)₁₀ = (11101)₂", "(29)₁₀ = (35)₈", "(29)₁₀ = (1D)₁₆", "(0.625)₁₀ = (0.101)₂"],
  answer=[0, 1, 2, 3],
  explain="29 = 16+8+4+1 = 11101₂；11101₂ 按三位分组为 35₈；按四位分组为 0001 1101 = 1D₁₆。0.625 连续乘 2 得 1、0、1，因此是 0.101₂。",
  source="第01章.pptx · 1.1 数制与进制转换（slide 15–19）")

q(chapter=1, section="1.2", topicId="1.2", type="judge", difficulty=1,
  stem="计算机内部通常使用二进制表示指令、数据和地址。",
  answer=True,
  explain="PPT 指出，计算机中的任何信息（指令、数据、地址）都用由 0 和 1 组成的二进制数字序列表示。",
  source="第01章.pptx · 1.1 计算机中的信息表示（slide 14）")

q(chapter=1, section="1.2", topicId="1.2", type="judge", difficulty=2,
  stem="对于 n 位补码，其能表示的整数范围是 -2ⁿ～2ⁿ-1。",
  answer=False,
  explain="正确的 n 位补码范围是 -2^(n-1)～2^(n-1)-1。例如 8 位补码为 -128～127，而不是 -256～255。",
  source="第01章.pptx · 1.1 补码（slide 22）")

q(chapter=1, section="1.2", topicId="1.2", type="judge", difficulty=3,
  stem="补码表示下，减法可以转换成加上减数的补码来完成，最高位产生的进位舍去。",
  answer=True,
  explain="补码的重要优势就是把减法统一为加法，CPU 的整数运算器可以只做加法。最高位进位不在固定字长内时被舍去。",
  source="第01章.pptx · 1.1 补码（slide 23）")

q(chapter=1, section="1.2", topicId="1.2", type="fill", difficulty=1,
  stem="十进制整数转二进制整数可用“除 2 取余、____排列”的方法。",
  answer=["逆序"],
  alt=[["反向", "倒序"]],
  explain="每次除以 2 得到的余数先是最低位，最后得到的余数是最高位，所以要把余数从下往上逆序排列。",
  source="第01章.pptx · 1.1 十进制转二进制（slide 16）")

q(chapter=1, section="1.2", topicId="1.2", type="fill", difficulty=2,
  stem="十六进制数 0x2F 对应的十进制数是____。",
  answer=["47"],
  explain="0x2F = 2×16 + 15 = 32 + 15 = 47。",
  source="第01章.pptx · 1.1 数制转换（slide 15）")

q(chapter=1, section="1.2", topicId="1.2", type="fill", difficulty=3,
  stem="用 8 位补码表示十进制整数 -5，结果是二进制____。",
  answer=["11111011"],
  alt=[["1111 1011"]],
  explain="5 的 8 位原码是 00000101；按位取反得 11111010，再加 1 得 11111011。",
  source="第01章.pptx · 1.1 补码（slide 22）")

q(chapter=1, section="1.2", topicId="1.2", type="code", difficulty=2,
  stem="阅读下面这段说明，若按“除 2 取余、逆序排列”把 10 转成二进制，结果是什么？",
  code=["10 ÷ 2 = 5 余 0", "5 ÷ 2 = 2 余 1", "2 ÷ 2 = 1 余 0", "1 ÷ 2 = 0 余 1"],
  options=["0101", "1010", "1100", "1001"],
  answer=1,
  explain="余数依次为 0、1、0、1，逆序排列得到 1010。不能按计算顺序直接写成 0101。",
  source="第01章.pptx · 1.1 十进制转二进制（slide 16）")

q(chapter=1, section="1.2", topicId="1.3", type="single", difficulty=1,
  stem="程序设计一般步骤中，紧接在“需求分析”之后的是？",
  options=["运行维护", "系统设计", "编码实现", "测试与调试"],
  answer=1,
  explain="PPT 给出的顺序是：需求分析 → 系统设计 → 实现（编码）→ 测试与调试 → 运行维护。需求分析回答“做什么”，系统设计回答“如何做”。",
  source="第01章.pptx · 1.2 程序设计步骤（slide 27）")

q(chapter=1, section="1.2", topicId="1.3", type="single", difficulty=2,
  stem="下列关于编译方式和解释方式的说法，正确的是？",
  options=["解释方式会产生独立的目标代码程序", "编译方式执行目标代码时不再需要源程序", "编译方式对源程序逐条翻译并执行", "解释方式第一次执行后就不再需要源程序"],
  answer=1,
  explain="编译方式先把源程序整体翻译为目标代码，之后执行目标代码，因此运行时不再需要源程序。解释方式逐条翻译执行且通常不产生目标代码，每次运行都需要解释器和源程序。",
  source="第01章.pptx · 1.2 高级语言的翻译（slide 30）")

q(chapter=1, section="1.2", topicId="1.3", type="single", difficulty=3,
  stem="下列关于程序设计范式的说法，正确的是？",
  options=["过程式程序的数据处于中心地位，函数从属于数据", "面向对象程序由对象构成，对象封装数据及可施加于数据的操作", "函数式程序以事实和推理规则为组织核心", "逻辑式程序把函数作为值，强调函数应用"],
  answer=1,
  explain="面向对象以对象为中心，对象封装数据与操作，通过消息协作。过程式以功能为中心；函数式以函数应用为中心；逻辑式以事实和推理规则为中心。",
  source="第01章.pptx · 1.2 程序设计范式（slide 25–26）")

q(chapter=1, section="1.2", topicId="1.3", type="multiple", difficulty=2,
  stem="下列属于高级语言的有？",
  options=["C++", "Java", "Python", "汇编语言"],
  answer=[0, 1, 2],
  explain="C++、Java、Python 都是高级语言；汇编语言与机器指令一一对应，需要汇编程序翻译，属于低级语言。",
  source="第01章.pptx · 1.2 程序设计语言（slide 28–31）")

q(chapter=1, section="1.2", topicId="1.3", type="multiple", difficulty=3,
  stem="关于测试与调试，下列说法正确的有？",
  options=["测试是通过测试数据运行程序并检查结果是否符合预期", "调试是定位并改正程序错误的过程", "测试手段可以证明程序完全没有错误", "运行维护可能包括改正错误、完善功能和移植程序"],
  answer=[0, 1, 3],
  explain="测试只能发现程序有错误，不能证明程序没有错误，所以 C 错误。A、B 是测试/调试的基本定义，D 对应正确性维护、完善性维护和适应性维护。",
  source="第01章.pptx · 1.2 程序设计步骤（slide 27）")

q(chapter=1, section="1.2", topicId="1.3", type="judge", difficulty=1,
  stem="C++ 同时支持过程式程序设计和面向对象程序设计，属于编译型高级语言。",
  answer=True,
  explain="C++ 保留 C 的过程式能力，又增加了支持面向对象的语言成分，并且需要编译成机器代码/目标代码后执行。",
  source="第01章.pptx · 1.3 C++ 语言概述（slide 33）")

q(chapter=1, section="1.2", topicId="1.3", type="judge", difficulty=2,
  stem="解释方式会把整个源程序一次性翻译成目标代码，然后执行目标代码。",
  answer=False,
  explain="这是编译方式。解释方式对源程序逐条翻译并执行，通常不生成完整的目标代码程序，程序的每次执行都需要源程序。",
  source="第01章.pptx · 1.2 高级语言的翻译（slide 30）")

q(chapter=1, section="1.2", topicId="1.3", type="fill", difficulty=1,
  stem="C++ 程序从名为 ____ 的函数开始执行。",
  answer=["main"],
  alt=[["Main"]],
  explain="C++ 程序有且只有一个 main 函数，程序从它开始执行，main 返回时程序结束。注意 C++ 区分大小写，习惯写 main。",
  source="第01章.pptx · 1.2 C++ 语言概述（slide 33）；函数入口见第04章-01 slide 9")

q(chapter=1, section="1.2", topicId="1.3", type="fill", difficulty=2,
  stem="高级语言常见的三种翻译方式是编译、解释和____。",
  answer=["混合"],
  explain="混合方式先把高级语言程序编译成中间语言程序，再以解释方式执行中间语言程序，兼顾灵活性与效率。",
  source="第01章.pptx · 1.2 高级语言的翻译（slide 30）")

q(chapter=1, section="1.2", topicId="1.3", type="code", difficulty=4,
  stem="某程序的三种运行过程描述如下。若源程序需要先整体翻译成目标代码，然后不再依赖源代码直接运行，它属于哪种方式？",
  code=["源程序 → 翻译器 → 目标代码", "执行目标代码", "运行时不读取源程序"],
  options=["编译方式", "解释方式", "混合方式", "汇编方式"],
  answer=0,
  explain="先整体翻译产生功能等价的目标代码，再执行目标代码，是编译方式。解释方式逐条翻译执行；混合方式生成中间语言后再解释。",
  source="第01章.pptx · 1.2 高级语言的翻译（slide 30）")

q(chapter=1, section="1.3", topicId="1.4", type="single", difficulty=1,
  stem="下列哪个是合法的 C++ 标识符？",
  options=["8bc", "student_name", "int", "a-b"],
  answer=1,
  explain="标识符由字母、数字、下划线构成且首字符不能为数字。8bc 以数字开头；int 是关键词；a-b 含减号；student_name 合法。",
  source="第01章.pptx · 1.3 C++ 的标识符（slide 35）")

q(chapter=1, section="1.3", topicId="1.4", type="single", difficulty=2,
  stem="关于 C++ 标识符，下列说法正确的是？",
  options=["abc、Abc 和 ABC 是同一个标识符", "标识符可以包含空格", "标识符区分大小写，关键词不能作为用户标识符", "标识符必须以字母或下划线开头，不能以下划线开头"],
  answer=2,
  explain="C++ 区分大小写；关键词有固定含义不能用作自定义实体名。标识符可以由下划线开头；不能包含空格。",
  source="第01章.pptx · 1.3 C++ 的标识符（slide 35）")

q(chapter=1, section="1.3", topicId="1.4", type="multiple", difficulty=2,
  stem="下列属于 C++ 单词的有？",
  options=["标识符", "关键词", "字面常量", "操作符和标点符号"],
  answer=[0, 1, 2, 3],
  explain="C++ 的单词包括标识符、关键词、字面常量、操作符和标点符号。它们都是字符集中字符按规则构成的最小语法单位。",
  source="第01章.pptx · 1.3 C++ 的词法（slide 34）")

q(chapter=1, section="1.3", topicId="1.4", type="multiple", difficulty=3,
  stem="关于 C++ 注释，下列说法正确的有？",
  options=["// 注释延续到本行结束", "/* ... */ 可以跨多行", "多行注释可以相互嵌套", "注释内容不参与程序的执行"],
  answer=[0, 1, 3],
  explain="// 是单行注释；/* */ 可跨行；注释只是说明性文字，不参与执行。C++ 的多行注释不能相互嵌套，因此 C 错误。",
  source="第01章.pptx · 1.3 C++ 的词法（slide 37）")

q(chapter=1, section="1.3", topicId="1.4", type="judge", difficulty=1,
  stem="C++ 中的关键词可以作为用户自定义变量名，只要程序能编译即可。",
  answer=False,
  explain="关键词是语言预定义、有固定作用的标识符，不能用作自定义实体名。若强行使用，编译器会报错。",
  source="第01章.pptx · 1.3 C++ 的关键词（slide 36）")

q(chapter=1, section="1.3", topicId="1.4", type="judge", difficulty=2,
  stem="字符常量 'A' 和字符串字面量 \"A\" 的类型与存储形式相同。",
  answer=False,
  explain="'A' 是 char 类型字符常量；\"A\" 是由 'A' 和结尾 '\\0' 组成的字符串字面量，类型是一维字符常量数组。两者不能混为一谈。",
  source="第01章.pptx · 1.3 字面常量（slide 37）；第02章 slide 14")

q(chapter=1, section="1.3", topicId="1.4", type="fill", difficulty=1,
  stem="C++ 标识符的第一个字符不能是____。",
  answer=["数字"],
  explain="标识符可由字母、数字、下划线组成，但首字符不能是数字；例如 8bc 不合法，_name1 合法。",
  source="第01章.pptx · 1.3 C++ 的标识符（slide 35）")

q(chapter=1, section="1.3", topicId="1.4", type="fill", difficulty=2,
  stem="C++ 单行注释以两个连续的____符号开始。",
  answer=["//"],
  alt=[["斜杠", "斜线"]],
  explain="单行注释从 // 开始延续到本行结束；多行注释从 /* 开始、以 */ 结束。",
  source="第01章.pptx · 1.3 C++ 的词法（slide 37）")

q(chapter=1, section="1.3", topicId="1.4", type="code", difficulty=2,
  stem="下面代码中有几处会导致编译错误的词法问题？",
  code=["int 2count = 3;", "int _total = 2;", "int class = 4;", "int ok_1 = 5;"],
  options=["1 处", "2 处", "3 处", "4 处"],
  answer=1,
  explain="2count 以数字开头，不合法；class 是关键词，不能作变量名；_total 与 ok_1 合法。因此共 2 处错误。",
  source="第01章.pptx · 1.3 标识符与关键词（slide 35–36）")

q(chapter=1, section="1.3", topicId="1.4", type="code", difficulty=3,
  stem="阅读程序，输出结果是？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int a = 3, b = 4;", "    cout << a << b;", "    return 0;", "}"],
  options=["34", "3 4", "7", "43"],
  answer=0,
  explain="cout 连续输出两个整数时不会自动插入空格，所以先输出 3 再输出 4，得到 34。要输出空格需显式写 \" \"。",
  source="第01章.pptx · 1.3 C++ 程序结构（slide 33）；cout 见第02章 slide 37")

q(chapter=1, section="1.1", topicId="1.1", type="programming", difficulty=1,
  stem="编写一个 C++ 程序，在屏幕上输出一行：Hello, C++!（不要输出多余内容）",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    // 在这里完成输出\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){ cout << \"Hello, C++!\"; return 0; }\n",
  tests=[{"input": "", "output": "Hello, C++!"}, {"input": "任意内容会被忽略\n", "output": "Hello, C++!", "hidden": True}],
  hints=["使用 cout 和 << 输出字符串。", "字符串两侧使用英文双引号。"],
  explain="本题只考查程序入口 main 与标准输出。cout << \"Hello, C++!\"; 将字符串送到标准输出。评测会忽略行末多余空白，但不会忽略额外文字。",
  source="第01章.pptx · 1.3 C++ 程序结构（slide 33）；第02章 slide 37")

q(chapter=1, section="1.1", topicId="1.3", type="programming", difficulty=2,
  stem="编写程序：读入一个整数 n，输出它的 2 倍。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 输出 n 的 2 倍\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){ int n; cin>>n; cout<<n*2; return 0; }\n",
  tests=[{"input":"5\n","output":"10"},{"input":"-3\n","output":"-6"},{"input":"0\n","output":"0","hidden":True},{"input":"123456\n","output":"246912","hidden":True}],
  hints=["用 cin >> n; 读入。", "乘 2 后交给 cout 输出。"],
  explain="用 cin 读取整数，表达式 n*2 完成计算，再用 cout 输出结果。注意整数读入不需要额外格式控制。",
  source="第02章.pptx · 2.3 输入输出（slide 18）；第02章 2.4 算术运算（slide 19）")

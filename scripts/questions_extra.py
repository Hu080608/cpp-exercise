# -*- coding: utf-8 -*-
"""补充题：确保 6 种题型 × 4 档难度矩阵无空缺。"""
from qcommon import q

q(chapter=2, section="2.4", topicId="2.4", type="code", difficulty=1,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int a = 2;", "    a += 3;", "    cout << a;", "    return 0;", "}"],
  options=["2", "3", "5", "6"], answer=2,
  explain="a 初值 2，a += 3 等价于 a = a + 3，因此 a 变为 5，输出 5。",
  source="第02章.pptx · 2.4 复合赋值（slide 30）")

q(chapter=3, section="3.1", topicId="3.1", type="code", difficulty=1,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    cout << \"C++\";", "    return 0;", "}"],
  options=["C++", "C", "0", "没有输出"], answer=0,
  explain="cout << \"C++\" 将双引号中的字符序列输出到屏幕，结果为 C++；return 0 只表示程序正常结束。",
  source="第03章.pptx · 3.2 表达式语句（slide 14–15）；第02章 slide 37")

q(chapter=2, section="2.1", topicId="2.1", type="multiple", difficulty=1,
  stem="下列属于 C++ 基本数据类型的有？",
  options=["int", "char", "bool", "struct Student"], answer=[0, 1, 2],
  explain="int、char、bool 都是语言预定义的基本类型；struct Student 是用户自定义的构造类型，不属于基本数据类型。",
  source="第02章.pptx · 2.2 C++ 数据类型（slide 4–9）")

q(chapter=2, section="2.4", topicId="2.4", type="multiple", difficulty=4,
  stem="关于求值规则，下列说法正确的有？",
  options=["&& 和 || 支持短路求值", "赋值运算符是右结合的", "条件运算符是右结合的", "C++ 总是从左到右规定所有操作符的求值次序"],
  answer=[0, 1, 2],
  explain="&&、|| 短路；赋值与条件运算符右结合。C++ 对不相邻操作符一般不规定求值次序，因此 D 错误。",
  source="第02章.pptx · 2.5 优先级、结合性与求值次序（slide 32–36）")

q(chapter=4, section="4.5", topicId="4.5", type="multiple", difficulty=4,
  stem="关于宏、inline 与默认参数，下列说法正确的有？",
  options=["宏替换发生在预处理阶段，不检查参数类型", "inline 函数仍然遵守函数参数求值规则", "默认参数必须从参数表右端开始连续给出", "经过宏展开后，带副作用的实参一定只求值一次"],
  answer=[0, 1, 2],
  explain="宏没有函数参数类型检查，且实参可能重复求值；inline 是真正的函数，遵守参数求值规则；默认参数从右端连续给出。D 错误。",
  source="第04章-3.pptx · 宏、inline、默认参数（slide 15–28）")

q(chapter=4, section="4.6", topicId="4.6", type="single", difficulty=4,
  stem="关于函数重载与函数指针，下列说法正确的是？",
  options=["double (*fp)(int) 声明了一个返回 double* 的函数", "带捕获的 Lambda 可以赋给普通函数指针", "函数名可以直接赋给类型匹配的函数指针", "仅返回值不同的两个同名函数构成合法重载"],
  answer=2,
  explain="函数名在表达式中可转换为函数地址，直接赋给匹配的函数指针。double (*fp)(int) 是函数指针；带捕获 Lambda 不能转普通函数指针；仅返回值不同不能重载。",
  source="第04章 - 3-2.pptx · 函数指针、Lambda、重载（slide 5、26–27、39）")

q(chapter=5, section="5.6", topicId="5.9", type="single", difficulty=4,
  stem="关于引用，下列说法正确的是？",
  options=["引用初始化后可以重新绑定到另一个变量", "返回局部变量的引用是安全的", "const 引用可以绑定到临时对象并保持只读使用", "引用定义时可以暂不初始化，以后再绑定"],
  answer=2,
  explain="const 引用可以绑定临时对象，常用于只读传参；引用必须初始化且不能重新绑定；返回局部变量引用会在函数结束后悬空，因此 A、B、D 错误。",
  source="第05章 - 2.pptx · 5.6 引用规则与返回引用（slide 126、136–137）")

q(chapter=5, section="5.5", topicId="5.7", type="single", difficulty=4,
  stem="若有 int a[5] = {1,2,3,4,5}; int *p = a; int *q = &a[4];，则 *(q-2) 的值是？",
  options=["1", "2", "3", "4"], answer=2,
  explain="q 指向 a[4]=5；q-2 指向 a[2]，解引用得 a[2]=3。指针减整数按元素大小移动。",
  source="第05章 - 2.pptx · 5.5 指针运算与数组（slide 15–18）")

q(chapter=2, section="2.4", topicId="2.5", type="judge", difficulty=4,
  stem="表达式 int i=-10; unsigned int j=3; cout << i+j; 会输出 -7。",
  answer=False,
  explain="i 与 j 混合时 i 转换为 unsigned int，-10 变成很大的无符号数，i+j 的结果也是无符号数，不会输出 -7。这是隐式转换陷阱。",
  source="第02章.pptx · 2.4 隐式转换问题（slide 27）")

q(chapter=4, section="4.6", topicId="4.6", type="judge", difficulty=4,
  stem="无捕获 Lambda 能否转换为函数指针取决于它是否在函数体内使用了外层变量；只要函数体没用到外层变量，即使捕获列表写 [=] 也一定能转换为函数指针。",
  answer=False,
  explain="能否转换取决于捕获列表是否为空，而不是函数体实际有没有用到外层变量。写了 [=] 就带有捕获语义，不能转换为普通函数指针。",
  source="第04章 - 3-2.pptx · 无捕获 Lambda（slide 26–27）")

q(chapter=1, section="1.2", topicId="1.2", type="fill", difficulty=4,
  stem="用 8 位补码表示十进制整数 -128，其二进制补码是____。",
  answer=["10000000"],
  alt=[["1000 0000"]],
  explain="8 位补码范围是 -128～127，-128 的补码是 10000000，这是补码中唯一没有对应正数同绝对值的边界值。",
  source="第01章.pptx · 1.1 补码范围（slide 22）")

q(chapter=2, section="2.5", topicId="2.5", type="fill", difficulty=4,
  stem="若 short a=2; int b=2147483647; 按从左到右计算，表达式 a*b/c（c 为 double 且 c=2.0）在常见 32 位 int 下会发生____（填“溢出”或“正常”）。",
  answer=["溢出"],
  explain="a*b 会先在 int 中计算，a 先型提升为 int，2×2147483647 超出 int 范围，发生有符号溢出；正确写法是 (double)a*b/c，先把一个操作数转为 double。",
  source="第02章.pptx · 2.4 逐操作符转换与溢出（slide 28）")

q(chapter=3, section="3.4", topicId="3.4", type="multiple", difficulty=4,
  stem="关于 break、continue、goto 与 return，下列说法正确的有？",
  options=["break 只结束最近一层循环或 switch", "for 中 continue 会先执行表达式3", "goto 不能跨函数跳转", "return 可以结束当前函数并返回调用处"],
  answer=[0, 1, 2, 3],
  explain="四项都正确：break 作用范围是最近一层结构；for 的 continue 跳到更新表达式；goto 限于同一函数；return 结束函数。",
  source="第03章.pptx · 3.5 无条件转移（slide 65–77）")

# -*- coding: utf-8 -*-
from qcommon import q

# ======================= 第 2 章 =======================
q(chapter=2, section="2.1", topicId="2.1", type="single", difficulty=1,
  stem="下列哪一组全部属于 C++ 的基本数据类型？",
  options=["int、double、char、bool", "数组、结构体、联合体", "class、vector、string", "指针、引用、函数"],
  answer=0,
  explain="int/double/char/bool 是语言预定义的基本类型。数组、结构体、联合体是构造类型；class/vector/string 属于用户自定义或标准库类型；指针和引用不是基本数据类型。",
  source="第02章.pptx · 2.2 C++ 数据类型（slide 4–9）")

q(chapter=2, section="2.1", topicId="2.1", type="single", difficulty=2,
  stem="关于无符号整数类型，下列说法正确的是？",
  options=["无符号整数能够表示负数", "无符号整数的最大正整数通常约为同宽度有符号整数的两倍", "无符号整数相减一定仍是非负数", "unsigned 比 int 占用更多字节"],
  answer=1,
  explain="无符号类型不保留符号位，所有位都表示绝对值，因此同宽度下最大正整数约为有符号的两倍。无符号减法可能下溢（如 1-2 得到很大的数），并不封闭。空间通常与对应有符号类型相同。",
  source="第02章.pptx · 2.2 无符号整数类型（slide 6）")

q(chapter=2, section="2.1", topicId="2.1", type="single", difficulty=3,
  stem="在常见 C++ 实现中，下列哪项描述最准确？",
  options=["float 的精度和范围都高于 double", "double 通常占 8 字节，精度高于 float", "long double 一定只占 8 字节", "char 一定是有符号类型"],
  answer=1,
  explain="常见实现中 float 占 4 字节、double 占 8 字节，double 精度与范围更大；long double 由实现决定（8 或 10 字节等）；char 是否有符号由实现决定。",
  source="第02章.pptx · 2.2 实数与字符类型（slide 7–10）")

q(chapter=2, section="2.1", topicId="2.1", type="multiple", difficulty=2,
  stem="下列属于“整型（integral types）”的有？",
  options=["int", "char", "bool", "double"],
  answer=[0, 1, 2],
  explain="C++ 的整型包括各种 int 类型、各种 char 类型以及 bool。double 属于实数（浮点）类型，不属于整型。",
  source="第02章.pptx · 2.2 基本数据类型（slide 9–10）")

q(chapter=2, section="2.1", topicId="2.1", type="multiple", difficulty=3,
  stem="关于 typedef，下列说法正确的有？",
  options=["typedef 为已有类型定义别名", "typedef int Word; 后 Word 与 int 是同一种类型", "typedef 会创建一种全新的类型", "typedef 可让复杂声明更易读"],
  answer=[0, 1, 3],
  explain="typedef 只是已有类型的别名，不创造新类型，所以 Word 与 int 完全相同；它常用于简化复杂声明、提高可读性。C 错误。",
  source="第02章.pptx · 2.2 typedef（slide 10）")

q(chapter=2, section="2.1", topicId="2.1", type="judge", difficulty=1,
  stem="bool 类型的值只有 true 和 false，通常 true 存为 1、false 存为 0。",
  answer=True,
  explain="bool 是逻辑类型。在大多数实现中占 1 字节，true 存 1、false 存 0；输出时可用 boolalpha 显示 true/false。",
  source="第02章.pptx · 2.2 逻辑类型（slide 9）")

q(chapter=2, section="2.1", topicId="2.1", type="judge", difficulty=2,
  stem="C++ 的 double 类型能够精确表示所有十进制小数，包括 0.1。",
  answer=False,
  explain="实数类型采用固定长度浮点表示，很多十进制小数（如 0.1）无法用二进制精确表示，只能得到近似值。",
  source="第02章.pptx · 2.2 实数类型（slide 7）")

q(chapter=2, section="2.1", topicId="2.1", type="fill", difficulty=1,
  stem="表示“没有返回值”的函数返回值类型或通用指针 void* 的类型是____。",
  answer=["void"],
  explain="void 是空值类型，值集为空；可用作无返回值函数的返回类型，也可用于 void* 通用指针。",
  source="第02章.pptx · 2.2 空值类型（slide 9）")

q(chapter=2, section="2.1", topicId="2.1", type="fill", difficulty=2,
  stem="在常见实现中，char 通常占____个字节。",
  answer=["1"],
  alt=[["一"]],
  explain="char 用于表示单字节编码的字符，常见实现占 1 个字节；它同时可参与整型提升，字符编码可当作小整数使用。",
  source="第02章.pptx · 2.2 字符类型（slide 8、10）")

q(chapter=2, section="2.1", topicId="2.1", type="code", difficulty=2,
  stem="阅读程序，若 char 占 1 字节、short 占 2 字节，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    cout << sizeof(char) << sizeof(short);", "    return 0;", "}"],
  options=["12", "1 2", "3", "21"],
  answer=0,
  explain="sizeof 返回所占字节数，sizeof(char) 为 1、sizeof(short) 为 2。连续输出两个整数之间不会自动加空格，所以结果是 12。",
  source="第02章.pptx · 2.5 sizeof（slide 30）；类型大小见 slide 5–9")

q(chapter=2, section="2.1", topicId="2.1", type="code", difficulty=3,
  stem="阅读程序，输出结果是？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    unsigned int a = 1;", "    int b = -2;", "    cout << (a + b > 0);", "    return 0;", "}"],
  options=["0", "1", "-1", "编译错误"],
  answer=1,
  explain="int 与 unsigned int 混合时，int 会被转换为 unsigned int。-2 转换后成为很大的无符号数，加上 1 仍远大于 0，因此比较结果为 true，输出 1。",
  source="第02章.pptx · 2.4 常规算术转换（slide 22–24、27）")

q(chapter=2, section="2.3", topicId="2.2", type="single", difficulty=1,
  stem="下列哪个是合法的变量定义？",
  options=["int a=b=1;", "int a=1,b=1;", "int 1a=1;", "int a=1; b=1;（b 未定义）"],
  answer=1,
  explain="同类型变量可在一条定义中逗号分隔：int a=1,b=1;。int a=b=1; 中 b 尚未定义；1a 不是合法标识符；最后一项 b 未定义。",
  source="第02章.pptx · 2.3 变量定义（slide 16）")

q(chapter=2, section="2.3", topicId="2.2", type="single", difficulty=2,
  stem="关于 const double PI = 3.14159;，下列说法正确的是？",
  options=["PI 是变量，可以在后面重新赋值", "PI 是符号常量，程序中不能再修改它的值", "const 只能用于整数", "PI 会在运行时随机变化"],
  answer=1,
  explain="const 定义符号常量，必须在定义时初始化，之后不能修改。使用符号常量能提高程序可读性和可维护性。",
  source="第02章.pptx · 2.3 符号常量（slide 15）")

q(chapter=2, section="2.3", topicId="2.2", type="multiple", difficulty=2,
  stem="关于整数字面量，下列说法正确的有？",
  options=["十进制整数字面量不能以 0 开头（0 本身除外）", "以 0 开头的整数常量表示八进制", "以 0x 开头的整数常量表示十六进制", "后缀 L 表示 long 类型"],
  answer=[0, 1, 2, 3],
  explain="这些是 PPT 列出的整数常量书写规则：十进制首字符不能为 0（0 除外），0 开头为八进制，0x 开头为十六进制，L 后缀表示 long。",
  source="第02章.pptx · 2.3 整数类型字面常量（slide 12）")

q(chapter=2, section="2.3", topicId="2.2", type="judge", difficulty=1,
  stem="字符串字面量 \"abc\" 在内存中通常需要 4 个字符位置：'a'、'b'、'c' 和 '\\0'。",
  answer=True,
  explain="字符串字面量末尾会自动加字符串结束标记 '\\0'，所以存储 \"abc\" 至少需要 4 个 char 位置。",
  source="第02章.pptx · 2.3 字符串字面常量（slide 14）")

q(chapter=2, section="2.3", topicId="2.2", type="judge", difficulty=2,
  stem="在 C++ 中，int a(0); 是一种合法的变量定义和初始化写法。",
  answer=True,
  explain="变量可以用等号初始化（int a = 0;），也可以用圆括号直接初始化（int a(0);）；C++11 还支持花括号初始化。",
  source="第02章.pptx · 2.3 变量定义（slide 16）；第04章-3 slide 7")

q(chapter=2, section="2.3", topicId="2.2", type="fill", difficulty=1,
  stem="默认情况下，实数类型字面常量 3.14 的类型是____。",
  answer=["double"],
  explain="实数类型字面常量默认是 double；加 F 后缀表示 float，加 L 后缀表示 long double。",
  source="第02章.pptx · 2.3 实数类型字面常量（slide 13）")

q(chapter=2, section="2.3", topicId="2.2", type="fill", difficulty=2,
  stem="定义符号常量 PI 并初始化为 3.14 的语句是：const double PI = ____;",
  answer=["3.14"],
  explain="const double PI = 3.14; 定义了 double 型符号常量 PI。const 常量必须在定义时初始化，之后不可修改。",
  source="第02章.pptx · 2.3 符号常量（slide 15）")

q(chapter=2, section="2.3", topicId="2.2", type="code", difficulty=3,
  stem="阅读程序，输出结果是？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int a = 1, b = 1;", "    int t = a;", "    a = b;", "    b = t;", "    cout << a << b;", "    return 0;", "}"],
  options=["11", "10", "01", "12"],
  answer=0,
  explain="a、b 初值都是 1，交换后仍都为 1，连续输出得到 11。交换逻辑本身正确，只是两个相同值看不出变化。",
  source="第02章.pptx · 2.3 交换两个变量（slide 16）")

q(chapter=2, section="2.3", topicId="2.3", type="single", difficulty=1,
  stem="使用 cin 读取两个整数 a、b 的正确写法是？",
  options=["cin << a << b;", "cin >> a >> b;", "cout >> a >> b;", "cin >> a, b;"],
  answer=1,
  explain="cin 与提取运算符 >> 配合读取输入，可连续写 cin >> a >> b;。<< 用于输出流 cout，逗号不能替代连续的 >>。",
  source="第02章.pptx · 2.3 变量值的输入（slide 18）")

q(chapter=2, section="2.3", topicId="2.3", type="single", difficulty=2,
  stem="执行 cout << setw(5) << 10 << 20; 假设已包含 <iomanip>，显示结果是？",
  options=["   1020", "10   20", "    10", "1020   "],
  answer=0,
  explain="setw(5) 只控制紧接着的一次输出，因此 10 占 5 格、前面补 3 个空格；随后 20 不受宽度影响，紧跟输出，得到“   1020”。",
  source="第02章.pptx · 2.5 设置输出宽度（slide 37）")

q(chapter=2, section="2.3", topicId="2.3", type="single", difficulty=3,
  stem="执行 cout << fixed << setprecision(2) << 3.14159; 输出是？",
  options=["3.14", "3.1", "3.142", "3.14159"],
  answer=0,
  explain="fixed 与 setprecision(2) 连用时，setprecision 表示小数点后保留 2 位，并按四舍五入显示，因此输出 3.14。",
  source="第02章.pptx · 2.5 cout 流控制（slide 39）")

q(chapter=2, section="2.3", topicId="2.3", type="multiple", difficulty=2,
  stem="关于输出格式控制，下列说法正确的有？",
  options=["setw(n) 只影响下一次输出", "setfill(c) 设置填充字符后会保持", "hex 会把变量内部存储的数值改成十六进制", "endl 输出换行并刷新输出流"],
  answer=[0, 1, 3],
  explain="setw 只影响下一次输出，setfill 会保持；hex 只改变显示方式，不改变变量中存储的值；endl 换行并刷新流。C 错误。",
  source="第02章.pptx · 2.5 cout 流控制（slide 37–39）")

q(chapter=2, section="2.3", topicId="2.3", type="multiple", difficulty=3,
  stem="执行下列语句后，描述正确的有？",
  options=["cout << hex << 26; 输出 1a", "cout << oct << 26; 输出 32", "cout << dec << 26; 输出 26", "hex 会永久改变整数变量的值"],
  answer=[0, 1, 2],
  explain="26 的十六进制为 1a，八进制为 32，十进制为 26。格式控制符只影响后续输出的显示方式，不改变变量存储值，D 错误。",
  source="第02章.pptx · 2.5 cout 流控制（slide 38）")

q(chapter=2, section="2.3", topicId="2.3", type="judge", difficulty=1,
  stem="cin >> 读取数据时，一般以空格、制表符或回车作为不同输入数据之间的分隔符。",
  answer=True,
  explain="默认的 >> 提取会跳过前导空白，并以空白符作为数据分隔；每个输入数据的格式应与变量类型相符。",
  source="第02章.pptx · 2.3 变量值的输入（slide 18）")

q(chapter=2, section="2.3", topicId="2.3", type="judge", difficulty=2,
  stem="cout << setfill('%') << setw(5) << 10 << 20; 的输出是 %%%%1020。",
  answer=False,
  explain="setw(5) 只作用一次：10 占 5 格，前面补 3 个 %，得到 %%%10；之后的 20 不再受 setw 控制，直接输出。完整结果是 %%%1020，而不是 %%%%1020，所以题干错误。",
  source="第02章.pptx · 2.5 setw/setfill（slide 37）")

q(chapter=2, section="2.3", topicId="2.3", type="fill", difficulty=1,
  stem="C++ 中输出换行并刷新输出流常用的控制符是____。",
  answer=["endl"],
  alt=[["std::endl"]],
  explain="cout << endl; 输出一个换行符并刷新流。也可用 \"\n\" 输出换行，但 endl 额外具有刷新作用。",
  source="第02章.pptx · 2.5 表达式的输出（slide 37）")

q(chapter=2, section="2.3", topicId="2.3", type="fill", difficulty=2,
  stem="使用 fixed 后，cout << setprecision(3) << 12.3456; 会输出____。",
  answer=["12.346"],
  explain="fixed 使 setprecision(3) 表示小数点后 3 位，12.3456 四舍五入为 12.346。",
  source="第02章.pptx · 2.5 控制浮点数值显示（slide 39）")

q(chapter=2, section="2.3", topicId="2.3", type="code", difficulty=2,
  stem="阅读程序，输入 12 3.4，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int i; double d;", "    cin >> i >> d;", "    cout << i + d;", "    return 0;", "}"],
  options=["12", "15.4", "3.4", "123.4"],
  answer=1,
  explain="i 读到 12，d 读到 3.4；i 在加法中隐式转换为 double，12+3.4=15.4，然后输出 15.4。",
  source="第02章.pptx · 2.3 输入（slide 18）；2.4 算术转换（slide 22）")

q(chapter=2, section="2.3", topicId="2.3", type="code", difficulty=3,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "#include <iomanip>", "using namespace std;", "int main() {", "    cout << setfill('0') << setw(4) << 7;", "    cout << setw(4) << 12;", "    return 0;", "}"],
  options=["00070012", "0007  12", "000712", "7 12"],
  answer=0,
  explain="setfill('0') 设置后保持有效；第一次 setw(4) 让 7 显示为 0007，第二次 setw(4) 让 12 显示为 0012。连续输出得到 00070012。",
  source="第02章.pptx · 2.5 setw/setfill（slide 37）")

q(chapter=2, section="2.3", topicId="2.3", type="programming", difficulty=1,
  stem="编写程序：读入一个整数，原样输出它。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 输出 n\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;cout<<n;return 0;}\n",
  tests=[{"input":"42\n","output":"42"},{"input":"-7\n","output":"-7"},{"input":"0\n","output":"0","hidden":True}],
  hints=["cin >> n; 已经读入值。", "直接 cout << n;"],
  explain="本题练习 cin 与 cout 的基本配合：读入数据后用 << 输出。评测会忽略行末多余空白。",
  source="第02章.pptx · 2.3 输入输出（slide 18）")

q(chapter=2, section="2.4", topicId="2.4", type="single", difficulty=1,
  stem="表达式 7 / 2 在 C++ 中的结果是？",
  options=["3.5", "3", "4", "2"],
  answer=1,
  explain="两个操作数都是整数时，/ 执行整除，结果向零截断，7/2 得 3。若要得到 3.5，需要至少一个操作数为浮点类型。",
  source="第02章.pptx · 2.4 算术操作符（slide 19）")

q(chapter=2, section="2.4", topicId="2.4", type="single", difficulty=2,
  stem="执行 int x = 1; int y = x++; 后，x 和 y 的值分别是？",
  options=["2 和 2", "2 和 1", "1 和 2", "1 和 1"],
  answer=1,
  explain="x++ 是后置自增：先把原值 1 赋给 y，再让 x 加 1。因此 y=1，x=2；若是 ++x 则两者都为 2。",
  source="第02章.pptx · 2.4 自增自减（slide 20）")

q(chapter=2, section="2.4", topicId="2.4", type="single", difficulty=3,
  stem="若有 int age = 25;，下列哪个表达式正确表示 10 < age < 30？",
  options=["10 < age < 30", "10 < age && age < 30", "10 < age || age < 30", "10 < age & age < 30"],
  answer=1,
  explain="C++ 中 10 < age 先得到 bool 值 true，再拿 true<30 比较，并不是数学区间。区间判断必须用逻辑与连接两个关系式：10 < age && age < 30。",
  source="第02章.pptx · 2.4 关系与逻辑运算（slide 25）")

q(chapter=2, section="2.4", topicId="2.4", type="multiple", difficulty=2,
  stem="关于逻辑运算 && 和 ||，下列说法正确的有？",
  options=["它们支持短路求值", "&& 只有两边都为 true 时结果才为 true", "|| 只有两边都为 false 时结果才为 false", "0 会被当作 true"],
  answer=[0, 1, 2],
  explain="&&、|| 支持短路求值；逻辑与要求两边均为 true，逻辑或要求两边均为 false 才为 false。0 转为 false，非 0 转为 true，D 错误。",
  source="第02章.pptx · 2.4 逻辑运算与短路求值（slide 25、29）")

q(chapter=2, section="2.4", topicId="2.4", type="multiple", difficulty=3,
  stem="关于自增、自减和复合赋值，下列说法正确的有？",
  options=["++x 先加 1 后再使用 x", "x++ 先使用 x 的原值再让 x 加 1", "x += 3 等价于 x = x + 3", "自增运算可以作用于常量"],
  answer=[0, 1, 2],
  explain="前置先加后用，后置先用后加；x += 3 是复合赋值。++/-- 的操作数必须是可修改的变量，常量不能被自增，D 错误。",
  source="第02章.pptx · 2.4 自增自减与复合赋值（slide 20、30）")

q(chapter=2, section="2.4", topicId="2.4", type="judge", difficulty=1,
  stem="关系运算的结果类型是 bool，结果为 true 或 false。",
  answer=True,
  explain=">、<、>=、<=、==、!= 等关系运算对操作数进行比较，结果是逻辑类型 bool。",
  source="第02章.pptx · 2.4 关系操作符（slide 25）")

q(chapter=2, section="2.4", topicId="2.4", type="judge", difficulty=2,
  stem="表达式 false && (1 / 0 > 0) 会因为 1/0 而必然产生除零错误。",
  answer=False,
  explain="&& 短路求值：左操作数为 false 时已能确定结果为 false，不会计算右侧表达式，因此此处不会执行 1/0。这正是短路求值可作为“卫士”的原因。",
  source="第02章.pptx · 2.4 短路求值（slide 29）")

q(chapter=2, section="2.4", topicId="2.4", type="fill", difficulty=1,
  stem="表达式 17 % 5 的值是____。",
  answer=["2"],
  explain="% 求两个整数相除的余数。17 = 5×3 + 2，所以 17 % 5 = 2。",
  source="第02章.pptx · 2.4 算术操作符（slide 19）")

q(chapter=2, section="2.4", topicId="2.4", type="fill", difficulty=2,
  stem="若 int a = 5;，执行 a += 3; 后 a 的值是____。",
  answer=["8"],
  explain="a += 3 等价于 a = a + 3，因此 a 从 5 变为 8。",
  source="第02章.pptx · 2.4 复合赋值（slide 30）")

q(chapter=2, section="2.4", topicId="2.4", type="code", difficulty=2,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int x = 3, y = 4;", "    int z = x++ + ++y;", "    cout << x << \",\" << y << \",\" << z;", "    return 0;", "}"],
  options=["4,5,8", "4,5,9", "3,5,8", "4,4,8"],
  answer=0,
  explain="x++ 先取 3 再使 x 变 4；++y 先使 y 变 5 再取值 5；z = 3+5 = 8。输出 4,5,8。",
  source="第02章.pptx · 2.4 自增自减（slide 20）")

q(chapter=2, section="2.4", topicId="2.4", type="code", difficulty=3,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int a = 5;", "    bool b = a > 3 && a < 10;", "    bool c = !b || a == 5;", "    cout << b << c;", "    return 0;", "}"],
  options=["11", "10", "01", "00"],
  answer=0,
  explain="a>3 且 a<10 为 true，b=true；!b 为 false，但 a==5 为 true，所以 c=true。输出时 bool 默认显示 1/0，得到 11。",
  source="第02章.pptx · 2.4 关系与逻辑运算（slide 25–26）")

q(chapter=2, section="2.4", topicId="2.4", type="programming", difficulty=2,
  stem="编写程序：读入两个整数 a、b，输出它们的和、差、积、整除商和余数，每项之间用一个空格分隔。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    // 依次输出 a+b a-b a*b a/b a%b\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int a,b;cin>>a>>b;cout<<a+b<<\" \"<<a-b<<\" \"<<a*b<<\" \"<<a/b<<\" \"<<a%b;return 0;}\n",
  tests=[{"input":"7 2\n","output":"9 5 14 3 1"},{"input":"10 3\n","output":"13 7 30 3 1","hidden":True},{"input":"-7 2\n","output":"-5 -9 -14 -3 -1","hidden":True}],
  hints=["依次使用 + - * / %。", "评测保证 b 不为 0。"],
  explain="整数 / 是整除，% 是求余；输出顺序必须与题目一致。C++ 的整数除法向零截断，本题测试包含负数以检查这一规则。",
  source="第02章.pptx · 2.4 算术操作符（slide 19）")

q(chapter=2, section="2.5", topicId="2.5", type="single", difficulty=1,
  stem="表达式 1 + 2.5 的结果类型是？",
  options=["int", "float", "double", "bool"],
  answer=2,
  explain="1 是 int，2.5 默认是 double。按常规算术转换，int 会转换为 double，运算结果也是 double。",
  source="第02章.pptx · 2.4 类型转换（slide 21–24）")

q(chapter=2, section="2.5", topicId="2.5", type="single", difficulty=2,
  stem="若 int n = 3; double x = 2.5;，表达式 n + x 中 n 的处理方式是？",
  options=["n 被转换为 double 放入临时单元，n 本身仍是 int", "x 被转换为 int，n 保持 int", "n 的内存被永久改成 double", "表达式无法编译"],
  answer=0,
  explain="隐式转换会把 n 的值转换成 double 放入临时存储单元，再与 x 相加；被转换的操作数本身类型和值都未改变。",
  source="第02章.pptx · 2.4 类型转换（slide 21）")

q(chapter=2, section="2.5", topicId="2.5", type="single", difficulty=3,
  stem="若有 int i = -10; unsigned int j = 3;，则 i < j 的结果是？",
  options=["true", "false", "编译错误", "不确定，取决于机器"],
  answer=1,
  explain="i 与 j 混合运算时，i 被转换为 unsigned int。-10 转换后是很大的无符号数，因此 i < j 为 false。这是有符号/无符号混合的典型陷阱。",
  source="第02章.pptx · 2.4 常规算术转换与隐式转换问题（slide 22–27）")

q(chapter=2, section="2.5", topicId="2.5", type="multiple", difficulty=2,
  stem="关于显式类型转换，下列说法正确的有？",
  options=["可以写成 (double)n", "可以写成 double(n)", "显式转换会改变被转换变量本身", "转换结果可能存入临时存储单元"],
  answer=[0, 1, 3],
  explain="C++ 支持 (类型名)操作数 和 类型名(操作数) 两种显式转换写法；转换产生结果，一般不改变原操作数本身，结果放在临时单元中。C 错误。",
  source="第02章.pptx · 2.4 类型转换（slide 21、24）")

q(chapter=2, section="2.5", topicId="2.5", type="judge", difficulty=1,
  stem="赋值时，如果左右两边类型不同，右边的值会按赋值转换规则转换成左边变量的类型。",
  answer=True,
  explain="赋值运算的结果类型是左边操作数的类型；右边表达式会先转换为左边类型，再存入变量。",
  source="第02章.pptx · 2.4 隐式转换（slide 26）")

q(chapter=2, section="2.5", topicId="2.5", type="judge", difficulty=2,
  stem="表达式 short a=2; int b=2147483647; a*b 会先把 a、b 都转换成 double 再计算。",
  answer=False,
  explain="C++ 按操作符逐个进行类型转换，不会先把所有操作数统一提升到最高类型。a 先整型提升为 int，a*b 在 int 中计算并可能溢出；若写成 (double)a*b 才会得到浮点结果。",
  source="第02章.pptx · 2.4 表达式中的逐操作符转换（slide 28）")

q(chapter=2, section="2.5", topicId="2.5", type="fill", difficulty=1,
  stem="C 风格显式类型转换把变量 x 转成 double 可写为 (double)x 或 double(____)。",
  answer=["x"],
  explain="函数式写法 double(x) 与 (double)x 都表示显式转换，结果类型为 double。",
  source="第02章.pptx · 2.4 强制类型转换（slide 24）")

q(chapter=2, section="2.5", topicId="2.5", type="fill", difficulty=2,
  stem="表达式 sizeof(int) 的结果单位是____。",
  answer=["字节"],
  alt=[["byte", "bytes", "B"]],
  explain="sizeof 计算类型或表达式占用的内存大小，结果的单位是字节（byte）。",
  source="第02章.pptx · 2.5 sizeof（slide 30）")

q(chapter=2, section="2.5", topicId="2.5", type="code", difficulty=2,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int a = 5, b = 2;", "    cout << a / b << \" \" << (double)a / b;", "    return 0;", "}"],
  options=["2 2.5", "2.5 2.5", "2 2", "3 2.5"],
  answer=0,
  explain="a/b 两个整数相除得 2；(double)a/b 先把 a 转成 double，再与 b 运算，得到 2.5。输出 2 2.5。",
  source="第02章.pptx · 2.4 算术与类型转换（slide 19、24）")

q(chapter=2, section="2.5", topicId="2.5", type="code", difficulty=3,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    char ch = 'A';", "    cout << ch + 1;", "    return 0;", "}"],
  options=["A1", "66", "B", "65"],
  answer=1,
  explain="ch 在算术运算中被整型提升为 int，'A' 的编码是 65，ch+1 得 66；cout 输出 int 值 66，不会自动转回字符。",
  source="第02章.pptx · 2.2 字符类型与整型提升（slide 8、10）；2.4 slide 21")

q(chapter=2, section="2.5", topicId="2.5", type="code", difficulty=4,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int a = 1, b = 2, c = 3;", "    int r = a < b ? b < c ? c : b : a;", "    cout << r;", "    return 0;", "}"],
  options=["1", "2", "3", "0"],
  answer=2,
  explain="条件运算符右结合，表达式等价于 a < b ? (b < c ? c : b) : a。a<b 为 true，进入内层；b<c 为 true，取 c=3。",
  source="第02章.pptx · 2.5 条件运算符与结合性（slide 30、33）")

q(chapter=2, section="2.6", topicId="2.5", type="single", difficulty=1,
  stem="表达式 0x3F80 & 0x7AE5 的结果是？",
  options=["0x3A80", "0x7FE5", "0xFD84", "0x0000"],
  answer=0,
  explain="按位与：只有对应位都为 1 结果才为 1。PPT 示例计算结果为 0x3A80。",
  source="第02章.pptx · 2.4 位操作符（slide 34）")

q(chapter=2, section="2.6", topicId="2.5", type="multiple", difficulty=2,
  stem="下列属于 C++ 位运算操作符的有？",
  options=["&", "|", "^", "&&"],
  answer=[0, 1, 2],
  explain="&、|、^ 分别表示按位与、按位或、按位异或，属于位运算；&& 是逻辑与，操作对象按 bool 处理，不是位运算。",
  source="第02章.pptx · 2.4 位操作符（slide 34）")

q(chapter=2, section="2.6", topicId="2.5", type="judge", difficulty=2,
  stem="逻辑运算 && 与位运算 & 的功能完全相同，只是写法不同。",
  answer=False,
  explain="&& 是逻辑与，支持短路求值，结果按 bool 语义；& 是按位与，对整数的二进制位逐一运算，两者不是一回事。",
  source="第02章.pptx · 2.4 位操作符与逻辑运算（slide 25、34）")

q(chapter=2, section="2.6", topicId="2.5", type="fill", difficulty=1,
  stem="将整数 0x3F61 左移 2 位的结果用十六进制表示为 0x____。",
  answer=["FD84"],
  alt=[["fd84"]],
  explain="PPT 示例：0x3F61 << 2 = 0xFD84。左移时低位补 0，超出固定宽度的最高位舍弃。",
  source="第02章.pptx · 2.4 位操作符（slide 34）")

q(chapter=2, section="2.6", topicId="2.5", type="code", difficulty=2,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int x = 6;", "    cout << (x & 1) << (x | 1) << (x ^ 1);", "    return 0;", "}"],
  options=["077", "170", "067", "777"],
  answer=0,
  explain="6 的二进制是 110。6&1=0；6|1=7；6^1=7。连续输出得到 077。",
  source="第02章.pptx · 2.4 位操作符（slide 34）")

q(chapter=2, section="2.6", topicId="2.5", type="code", difficulty=3,
  stem="阅读程序，输出是什么？",
  code=["#include <iostream>", "using namespace std;", "int main() {", "    int x = 1;", "    cout << (x << 3);", "    return 0;", "}"],
  options=["3", "4", "8", "9"],
  answer=2,
  explain="1 的二进制为 1，左移 3 位变成 1000，即十进制 8。左移 1 位相当于乘 2（在未溢出时）。",
  source="第02章.pptx · 2.4 位操作符（slide 34）")

q(chapter=2, section="2.3", topicId="2.3", type="programming", difficulty=3,
  stem="编写程序：读入一个双精度实数 x，按“固定格式保留 2 位小数”输出它的平方。",
  starter="#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nint main() {\n    double x;\n    cin >> x;\n    // 输出 fixed + setprecision(2) 的 x*x\n    return 0;\n}\n",
  solution="#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){double x;cin>>x;cout<<fixed<<setprecision(2)<<x*x;return 0;}\n",
  tests=[{"input":"1.5\n","output":"2.25"},{"input":"2\n","output":"4.00"},{"input":"-3.2\n","output":"10.24","hidden":True}],
  hints=["使用 fixed 和 setprecision(2)。", "需要包含 <iomanip>。"],
  explain="fixed 与 setprecision(2) 组合表示小数点后固定 2 位；先计算 x*x，再按该格式输出。",
  source="第02章.pptx · 2.5 控制浮点数值显示（slide 39）")

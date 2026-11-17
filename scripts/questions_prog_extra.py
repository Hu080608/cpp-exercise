# -*- coding: utf-8 -*-
"""综合编程题增补：情境原创，部分题目标注经典题源（洛谷/力扣）作灵感来源。
所有题目只使用课程 PPT 第 1–5 章讲过的语言特性。"""
from qcommon import q

def P(**kw):
    kw.setdefault('type', 'programming')
    kw.setdefault('tags', ['综合编程'])
    kw.setdefault('origin', '原创情境题')
    q(**kw)

# ---------- 输入输出 / 基本运算 ----------
P(chapter=1, section="1.3", topicId="1.4", difficulty=1,
  stem="【A+B 入门】输入两个整数 a 和 b，输出它们的和。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    // 输出 a + b\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int a,b;cin>>a>>b;cout<<a+b;}\n",
  tests=[{"input":"3 4\n","output":"7"},{"input":"-5 2\n","output":"-3"},{"input":"100000 200000\n","output":"300000","hidden":True}],
  hints=["读入两个 int，直接输出 a+b。"],
  explain="最基础的输入—计算—输出流程：cin 读入，算术运算符 + 计算，cout 输出。",
  origin="洛谷 P1001 同类 · A+B Problem", source="第02章.pptx · 2.3 输入输出（slide 18）")

P(chapter=2, section="2.3", topicId="2.3", difficulty=1,
  stem="【天气播报】输入摄氏温度 C（double），输出华氏温度 F = C × 9 / 5 + 32，保留 1 位小数。",
  starter="#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nint main() {\n    double c;\n    cin >> c;\n    // 计算并输出华氏温度\n    return 0;\n}\n",
  solution="#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){double c;cin>>c;cout<<fixed<<setprecision(1)<<c*9/5+32;}\n",
  tests=[{"input":"0\n","output":"32.0"},{"input":"100\n","output":"212.0"},{"input":"-40\n","output":"-40.0","hidden":True}],
  hints=["注意 9/5 是整数除法，应先乘 C 或写 9.0/5。", "用 fixed + setprecision(1) 固定一位小数。"],
  explain="公式 F=C×9/5+32。由于 C 是 double，c*9/5 会进行浮点运算；输出用 fixed 与 setprecision(1)。",
  origin="原创情境 · 温度转换", source="第02章.pptx · 2.4 算术运算；2.5 浮点格式（slide 19、39）")

P(chapter=2, section="2.3", topicId="2.3", difficulty=1,
  stem="【班级花坛】输入圆的半径 r，输出面积和周长（π 取 3.14），两者保留 2 位小数，空格分隔。",
  starter="#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nint main() {\n    double r;\n    cin >> r;\n    // 面积 = 3.14*r*r，周长 = 2*3.14*r\n    return 0;\n}\n",
  solution="#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){double r;cin>>r;cout<<fixed<<setprecision(2)<<3.14*r*r<<\" \"<<2*3.14*r;}\n",
  tests=[{"input":"2\n","output":"12.56 12.56"},{"input":"1\n","output":"3.14 6.28"},{"input":"3.5\n","output":"38.47 21.98","hidden":True}],
  hints=["先乘后除不会产生整数除法问题。", "fixed + setprecision(2) 输出两位小数。"],
  explain="面积 πr²、周长 2πr；两个表达式都以 double 参与运算，最后统一按两位小数输出。",
  origin="原创情境 · 圆的计算", source="第02章.pptx · 2.4 算术运算；2.5 输出格式（slide 19、39）")

P(chapter=2, section="2.4", topicId="2.4", difficulty=1,
  stem="【时间换算】输入一个非负整数秒数，输出“时:分:秒”格式，例如 3661 输出 1:1:1。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int total;\n    cin >> total;\n    // 用 / 和 % 拆出时、分、秒\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int t;cin>>t;cout<<t/3600<<\":\"<<t%3600/60<<\":\"<<t%60;}\n",
  tests=[{"input":"3661\n","output":"1:1:1"},{"input":"59\n","output":"0:0:59"},{"input":"7322\n","output":"2:2:2","hidden":True}],
  hints=["小时 = total / 3600。", "分钟 = total % 3600 / 60，秒 = total % 60。"],
  explain="整数除法和取余可把总秒数逐级拆分：先取小时，再在剩余秒数中取分钟，最后取秒。",
  origin="原创情境 · 时间换算", source="第02章.pptx · 2.4 整除与取余（slide 19）")

P(chapter=2, section="2.4", topicId="2.4", difficulty=1,
  stem="【数字谜题】输入一个三位正整数，输出它的百位、十位、个位之和。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 取出三位数字并求和\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;cout<<n/100+n/10%10+n%10;}\n",
  tests=[{"input":"123\n","output":"6"},{"input":"909\n","output":"18"},{"input":"500\n","output":"5","hidden":True}],
  hints=["百位 n/100，十位 n/10%10，个位 n%10。"],
  explain="利用整除与取余逐个拆位，是循环处理数字的基础。",
  origin="原创情境 · 数位拆分", source="第02章.pptx · 2.4 整除与取余（slide 19）")

P(chapter=3, section="3.3", topicId="3.2", difficulty=1,
  stem="【灯光控制】输入一个整数，若为偶数输出 EVEN，否则输出 ODD。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 使用 % 判断奇偶\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;if(n%2==0)cout<<\"EVEN\";else cout<<\"ODD\";}\n",
  tests=[{"input":"4\n","output":"EVEN"},{"input":"7\n","output":"ODD"},{"input":"0\n","output":"EVEN","hidden":True},{"input":"-3\n","output":"ODD","hidden":True}],
  hints=["n % 2 == 0 表示偶数。"],
  explain="整数 %2 的余数判断奇偶；0 是偶数，负数取余结果非零时也走奇数分支。",
  origin="原创情境 · 奇偶判断", source="第03章.pptx · 3.3 选择执行（slide 19）；第02章 slide 19")

P(chapter=3, section="3.3", topicId="3.2", difficulty=1,
  stem="【三人赛跑】输入三个整数成绩，输出其中的最大值。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b, c;\n    cin >> a >> b >> c;\n    // 输出最大值\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int a,b,c;cin>>a>>b>>c;int m=a;if(b>m)m=b;if(c>m)m=c;cout<<m;}\n",
  tests=[{"input":"3 9 5\n","output":"9"},{"input":"-1 -7 -2\n","output":"-1"},{"input":"5 5 5\n","output":"5","hidden":True}],
  hints=["先把 a 赋给 m，再依次与 b、c 比较。"],
  explain="用一个临时最大值 m 依次比较，可扩展到更多数据；初值取 a 能正确处理全负数。",
  origin="原创情境 · 三数最大值", source="第03章.pptx · 3.3 三个整数中的最大值（slide 20）")

P(chapter=3, section="3.3", topicId="3.2", difficulty=2,
  stem="【成绩报告】输入 0～100 的整数成绩，按 ≥90 输出 A、80～89 输出 B、70～79 输出 C、60～69 输出 D、其余输出 E。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int score;\n    cin >> score;\n    // 用 else-if 分级\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int s;cin>>s;if(s>=90)cout<<\"A\";else if(s>=80)cout<<\"B\";else if(s>=70)cout<<\"C\";else if(s>=60)cout<<\"D\";else cout<<\"E\";}\n",
  tests=[{"input":"95\n","output":"A"},{"input":"60\n","output":"D"},{"input":"59\n","output":"E"},{"input":"80\n","output":"B","hidden":True}],
  hints=["从高到低判断，前面的条件覆盖后，后面无需重复写上限。"],
  explain="互斥区间适合用 else-if 链；每个分支只负责一个等级。",
  origin="原创情境 · 成绩等级", source="第03章.pptx · 3.3 独立 if 与 else-if（slide 23）")

P(chapter=3, section="3.3", topicId="3.2", difficulty=2,
  stem="【日历判断】输入年份 year，判断是否为闰年：是输出 LEAP，否则输出 COMMON。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int year;\n    cin >> year;\n    // 判断闰年\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int y;cin>>y;if(y%400==0||(y%4==0&&y%100!=0))cout<<\"LEAP\";else cout<<\"COMMON\";}\n",
  tests=[{"input":"2000\n","output":"LEAP"},{"input":"1900\n","output":"COMMON"},{"input":"2024\n","output":"LEAP"},{"input":"2023\n","output":"COMMON","hidden":True}],
  hints=["能被 400 整除，或能被 4 整除且不能被 100 整除。"],
  explain="闰年条件必须写成 year%400==0 || (year%4==0 && year%100!=0)，注意逻辑与优先级高于逻辑或。",
  origin="原创情境 · 日历判断", source="第03章.pptx · 3.3 例 3-9 判断闰年（slide 30）")

P(chapter=3, section="3.3", topicId="3.2", difficulty=2,
  stem="【阶梯电费】某地电费按用电量分段：0～150 度每度 0.4463 元；151～400 度超出部分每度 0.4663 元；超过 400 度，超出部分每度 0.5663 元。输入用电量，输出电费，保留 1 位小数。",
  starter="#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nint main() {\n    int x;\n    cin >> x;\n    double fee = 0;\n    // 按阶梯分段累加\n    return 0;\n}\n",
  solution="#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){int x;cin>>x;double f=0;if(x<=150)f=x*0.4463;else if(x<=400)f=150*0.4463+(x-150)*0.4663;else f=150*0.4463+250*0.4663+(x-400)*0.5663;cout<<fixed<<setprecision(1)<<f;}\n",
  tests=[{"input":"100\n","output":"44.6"},{"input":"200\n","output":"90.3"},{"input":"500\n","output":"240.1","hidden":True}],
  hints=["分段计费时，前面的 150 度和 250 度要单独算。", "最终结果用 fixed 保留 1 位小数。"],
  explain="阶梯计费不是整段统一单价：先加满低档，再计算超出部分。用 else-if 拆成三段。",
  origin="洛谷 P1422 同类 · 小玉家的电费", source="第03章.pptx · 3.3 else-if（slide 23）；第02章 slide 39")

P(chapter=3, section="3.3", topicId="3.2", difficulty=3,
  stem="【文具采购】学校要买 n 支铅笔。商店有三种包装：每包数量与价格不同，可以买任意包，但必须买够至少 n 支。求最少花多少钱。第一行输入 n，接下来三行每行输入“每包数量 每包价格”。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 读入三种包装，计算每种包装买够 n 支所需费用，取最小值\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;int best=2147483647;for(int i=0;i<3;i++){int num,price;cin>>num>>price;int packs=(n+num-1)/num;int cost=packs*price;if(cost<best)best=cost;}cout<<best;}\n",
  tests=[{"input":"57\n2 2\n50 30\n30 27\n","output":"54"},{"input":"10\n3 5\n5 8\n10 15\n","output":"15"},{"input":"1\n10 100\n5 51\n2 20\n","output":"20","hidden":True}],
  hints=["每种包装至少要买 ceil(n/num) 包。", "整数上取整可写 (n + num - 1) / num。"],
  explain="对三种包装分别计算费用，取最小值。必须买够至少 n 支，所以包数要上取整。",
  origin="洛谷 P1909 同类 · 买铅笔", source="第03章.pptx · 3.3 选择；3.4 循环（slide 19–38）")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【果园收获】陶陶家的苹果树上有 10 个苹果，高度分别为 100～200 厘米。陶陶有一个 30 厘米高的板凳，她伸手能达到的高度为 max_height + 30。输入 10 个苹果高度，再输入陶陶把手伸直能达到的高度，输出她能摘到的苹果数。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int a[10];\n    for (int i = 0; i < 10; i++) cin >> a[i];\n    int h;\n    cin >> h;\n    // 统计 a[i] <= h + 30 的个数\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int a[10],h,c=0;for(int i=0;i<10;i++)cin>>a[i];cin>>h;for(int i=0;i<10;i++)if(a[i]<=h+30)c++;cout<<c;}\n",
  tests=[{"input":"100 200 150 140 129 134 167 198 200 111\n110\n","output":"5"},{"input":"100 100 100 100 100 100 100 100 100 100\n70\n","output":"10"},{"input":"100 200 150 140 129 134 167 198 200 111\n50\n","output":"0","hidden":True}],
  hints=["可摘到条件：苹果高度 <= 手高 + 30。", "遍历 10 个元素计数。"],
  explain="数组遍历加条件计数，是“筛选满足条件的元素”的基础模型。",
  origin="洛谷 P1046 同类 · 陶陶摘苹果", source="第05章 - 1.pptx · 5.2 一维数组遍历（slide 26）")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【心情记录】津津连续 7 天记录上课时间（小时）。若某天上课时间超过 8 小时，她会不高兴。输出最不高兴的是第几天（1～7）；如果都不超过 8 小时，输出 0。若并列，输出天数更早的一天。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int day = 0, maxExtra = 0;\n    // 读入 7 天的上课时间，找出超过 8 小时且超出最多的一天\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int best=0,extraMax=0;for(int i=1;i<=7;i++){int x;cin>>x;if(x>8&&x-8>extraMax){extraMax=x-8;best=i;}}cout<<best;}\n",
  tests=[{"input":"5 6 7 8 9 10 9\n","output":"6"},{"input":"5 6 7 8 8 8 8\n","output":"0"},{"input":"9 9 7 8 8 8 8\n","output":"1","hidden":True}],
  hints=["只有超过 8 小时才算不高兴。", "用严格大于更新，自动保留最早出现的最不高兴日。"],
  explain="一次遍历记录最大超出量及对应天数；由于只在更大时更新，并列时保留较早天数。",
  origin="洛谷 P1085 同类 · 不高兴的津津", source="第03章.pptx · 3.4 循环与条件（slide 34）；第05章 slide 26")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【阶梯奖励】输入 n，计算 1! + 2! + … + n! 的值（n≤12）。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 一边累乘阶乘，一边累加\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;long long f=1,sum=0;for(int i=1;i<=n;i++){f*=i;sum+=f;}cout<<sum;}\n",
  tests=[{"input":"1\n","output":"1"},{"input":"3\n","output":"9"},{"input":"5\n","output":"153"},{"input":"12\n","output":"522956313","hidden":True}],
  hints=["当前项阶乘可以用上一项的阶乘乘 i 得到。", "n=12 时结果较大，使用 long long。"],
  explain="在同一个循环里维护阶乘项 f 和累加和 sum，避免每一轮从头重算阶乘。",
  origin="原创情境 · 阶乘和", source="第03章.pptx · 3.4 累乘与循环（slide 31–39）")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【分糖果】输入两个正整数 a、b，求它们的最大公约数。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    // 欧几里得算法：反复用余数替换\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int a,b;cin>>a>>b;while(b!=0){int r=a%b;a=b;b=r;}cout<<a;}\n",
  tests=[{"input":"12 18\n","output":"6"},{"input":"7 13\n","output":"1"},{"input":"100 25\n","output":"25","hidden":True}],
  hints=["while (b != 0) { r=a%b; a=b; b=r; }", "循环结束后 a 就是最大公约数。"],
  explain="欧几里得算法反复用除数与余数替换，直到余数为 0；这是循环与整除的综合应用。",
  origin="原创情境 · 最大公约数", source="第03章.pptx · 3.4 while 循环（slide 34）；第02章 slide 19")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【排队分组】输入两个正整数 a、b，求它们的最小公倍数。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    // 最小公倍数 = a / gcd(a,b) * b\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int a,b,x,y;cin>>a>>b;x=a;y=b;while(y!=0){int r=x%y;x=y;y=r;}cout<<a/x*b;}\n",
  tests=[{"input":"12 18\n","output":"36"},{"input":"7 13\n","output":"91"},{"input":"25 100\n","output":"100","hidden":True}],
  hints=["先求 gcd，再算 a/gcd*b，避免先乘溢出。", "a、b 至少为正整数。"],
  explain="两个正整数的最小公倍数 = a / gcd(a,b) × b。先除后乘可降低中间结果大小。",
  origin="原创情境 · 最小公倍数", source="第03章.pptx · 3.4 循环（slide 34）；第02章 slide 19")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【数字倒影】输入一个整数，输出它倒过来读的整数。例如 1230 输出 321，-450 输出 -54。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 用 % 和 / 逐位构造反转数\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;int sign=1;if(n<0){sign=-1;n=-n;}int r=0;while(n>0){r=r*10+n%10;n/=10;}cout<<sign*r;}\n",
  tests=[{"input":"1230\n","output":"321"},{"input":"-450\n","output":"-54"},{"input":"7\n","output":"7"},{"input":"1000\n","output":"1","hidden":True}],
  hints=["先记录符号，把负数转成正数处理。", "每次 r = r*10 + n%10，再 n/=10。"],
  explain="用整数的取余和整除逐位构造反转数，最后补回符号；多余的前导 0 会自然消失。",
  origin="原创情境 · 整数反转", source="第03章.pptx · 3.4 while 循环（slide 34）；第02章 slide 19")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【回文密码】输入一个正整数，判断它是否为回文数（正读反读相同）。是输出 YES，否则输出 NO。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 构造 n 的反转数，与原数比较\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;int x=n,r=0;while(x>0){r=r*10+x%10;x/=10;}cout<<(r==n?\"YES\":\"NO\");}\n",
  tests=[{"input":"121\n","output":"YES"},{"input":"123\n","output":"NO"},{"input":"7\n","output":"YES"},{"input":"1001\n","output":"YES","hidden":True}],
  hints=["用另一个变量 x 拆位，原数 n 保留用于比较。"],
  explain="把整数反转后与原数比较即可判断回文；注意保留原值，不能一边拆位一边直接用 n 比较。",
  origin="力扣 9 同类 · 回文数", source="第03章.pptx · 3.4 while（slide 34）；第02章 slide 19")

P(chapter=3, section="3.4", topicId="3.3", difficulty=3,
  stem="【数字普查】输入 n 和数字 k（0～9），统计 1 到 n 的所有整数中，数字 k 一共出现了多少次。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, k, count = 0;\n    cin >> n >> k;\n    // 枚举 1..n，对每个数拆位统计 k\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,k,c=0;cin>>n>>k;for(int i=1;i<=n;i++){int x=i;while(x>0){if(x%10==k)c++;x/=10;}}cout<<c;}\n",
  tests=[{"input":"100 1\n","output":"21"},{"input":"25 2\n","output":"9"},{"input":"9 0\n","output":"0"},{"input":"1000 0\n","output":"192","hidden":True}],
  hints=["外层枚举 i，内层 while 拆掉 i 的每一位。", "k 可能为 0，不能只统计首位。"],
  explain="枚举 1～n，对每个数用 %10 检查当前位、/=10 继续处理下一位，累加命中次数。",
  origin="洛谷 P1980 同类 · 计数问题", source="第03章.pptx · 3.4 嵌套循环（slide 57）；第02章 slide 19")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【冰雹猜想】从正整数 n 出发：若为偶数就除以 2，若为奇数就乘 3 加 1，反复操作直到变成 1。输出经过的步数（不含初始数，含变成 1 的最后一步）。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    long long n;\n    cin >> n;\n    int steps = 0;\n    // 模拟冰雹序列\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){long long n;cin>>n;int c=0;while(n!=1){if(n%2==0)n/=2;else n=n*3+1;c++;}cout<<c;}\n",
  tests=[{"input":"6\n","output":"8"},{"input":"1\n","output":"0"},{"input":"27\n","output":"111","hidden":True}],
  hints=["用 long long，奇数分支可能让数短暂变大。", "while(n != 1) 中每操作一次 steps++。"],
  explain="按规则模拟序列状态，循环终止于 n==1；注意 1 本身不需要再操作，步数为 0。",
  origin="洛谷 P5727 同类 · 冰雹猜想", source="第03章.pptx · 3.4 while 循环（slide 34）")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【调和级数】输入整数 k，求最小的 n，使得 1 + 1/2 + 1/3 + … + 1/n > k。输出 n。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int k;\n    cin >> k;\n    double sum = 0;\n    int n = 0;\n    // 累加直到 sum > k\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int k,n=0;cin>>k;double s=0;while(s<=k){n++;s+=1.0/n;}cout<<n;}\n",
  tests=[{"input":"1\n","output":"2"},{"input":"2\n","output":"4"},{"input":"3\n","output":"11"},{"input":"10\n","output":"12367","hidden":True}],
  hints=["sum 必须是 double，累加 1.0/n。", "循环条件是 sum <= k。"],
  explain="事件控制循环：不知道循环次数，用浮点累加和与目标 k 比较决定是否继续。",
  origin="洛谷 P1035 同类 · 级数求和", source="第03章.pptx · 3.4 while 与事件控制（slide 34、43）")

P(chapter=3, section="3.4", topicId="3.3", difficulty=2,
  stem="【素数统计】输入 n（2≤n≤10000），输出 1 到 n 之间素数的个数。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, count = 0;\n    cin >> n;\n    // 对每个数判断是否为素数\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,c=0;cin>>n;for(int x=2;x<=n;x++){bool ok=true;for(int i=2;i*i<=x;i++)if(x%i==0){ok=false;break;}if(ok)c++;}cout<<c;}\n",
  tests=[{"input":"10\n","output":"4"},{"input":"2\n","output":"1"},{"input":"100\n","output":"25"},{"input":"1000\n","output":"168","hidden":True}],
  hints=["1 不是素数，从 2 开始。", "试除到 i*i<=x 即可。"],
  explain="外层枚举候选数，内层用试除判断素数；发现因子就用 break 提前结束内层循环。",
  origin="原创情境 · 素数统计", source="第03章.pptx · 3.4 素数判断（slide 53–56）")

P(chapter=3, section="3.4", topicId="3.3", difficulty=3,
  stem="【完数寻宝】如果一个正整数等于它所有真因子（不含自身）之和，则称为完数。输入 n，输出 1 到 n 之间所有完数，按从小到大用空格分隔。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    // 枚举候选数并求因子和\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;bool first=true;for(int x=2;x<=n;x++){int s=1;for(int d=2;d*d<=x;d++)if(x%d==0){s+=d;if(d!=x/d)s+=x/d;}if(x>1&&s==x){if(!first)cout<<\" \";cout<<x;first=false;}}if(first)cout<<\"none\";}\n",
  tests=[{"input":"30\n","output":"6 28"},{"input":"6\n","output":"6"},{"input":"5\n","output":"none"},{"input":"500\n","output":"6 28 496","hidden":True}],
  hints=["1 是每个大于 1 的数的真因子，可把因子和初始化为 1。", "成对因子只加一次，注意 d*d==x 时不要重复加。"],
  explain="利用成对因子枚举到 √x，求所有真因子之和；没有找到时按约定输出 none。",
  origin="原创情境 · 完数", source="第03章.pptx · 3.4 循环与素数/因子（slide 31–56）")

P(chapter=3, section="3.4", topicId="3.3", difficulty=3,
  stem="【水仙花数】水仙花数是指一个三位数，其各位数字的立方和等于它本身。输出所有三位水仙花数，用空格分隔。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    // 枚举 100～999，拆出百、十、个位判断\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){bool first=true;for(int n=100;n<=999;n++){int a=n/100,b=n/10%10,c=n%10;if(a*a*a+b*b*b+c*c*c==n){if(!first)cout<<\" \";cout<<n;first=false;}}}\n",
  tests=[{"input":"","output":"153 370 371 407"}],
  hints=["百位 n/100，十位 n/10%10，个位 n%10。", "题目无输入，直接输出结果。"],
  explain="固定范围枚举，拆出三位数字并验证立方和。输入为空也要能正常运行。",
  origin="原创情境 · 水仙花数", source="第03章.pptx · 3.4 循环枚举（slide 31–38）")

P(chapter=5, section="5.2", topicId="5.2", difficulty=3,
  stem="【连续收益】输入 n 个整数表示连续 n 天的收益（可为负）。求连续子数组的最大和。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, a[1000];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    // 经典 Kadane 算法\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];int best=a[0],cur=a[0];for(int i=1;i<n;i++){cur=(cur>0?cur+a[i]:a[i]);if(cur>best)best=cur;}cout<<best;}\n",
  tests=[{"input":"9\n-2 1 -3 4 -1 2 1 -5 4\n","output":"6"},{"input":"1\n-5\n","output":"-5"},{"input":"5\n1 2 3 4 5\n","output":"15"},{"input":"6\n-2 -3 -1 -4 -5 -2\n","output":"-1","hidden":True}],
  hints=["cur 表示以当前元素结尾的最大子数组和。", "cur 变负时从当前元素重新开始。"],
  explain="Kadane 算法一次遍历：若之前累计和为正就继续累加，否则从当前元素重新开始；best 记录历史最大值。",
  origin="力扣 53 同类 · 最大子数组和", source="第05章 - 1.pptx · 5.2 数组遍历（slide 26）")

P(chapter=5, section="5.2", topicId="5.2", difficulty=3,
  stem="【寻找搭档】输入 n 个整数和目标值 target，找出两个不同下标 i<j，使 a[i]+a[j]==target，输出 i 和 j；若不存在输出 -1。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, target, a[1000];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    cin >> target;\n    // 双重循环查找第一组解\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,t,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];cin>>t;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(a[i]+a[j]==t){cout<<i<<\" \"<<j;return 0;}cout<<-1;}\n",
  tests=[{"input":"4\n2 7 11 15\n9\n","output":"0 1"},{"input":"3\n3 2 4\n6\n","output":"1 2"},{"input":"3\n1 2 3\n100\n","output":"-1","hidden":True}],
  hints=["要求 i<j，内层 j 从 i+1 开始。", "找到后直接 return 0。"],
  explain="用双重循环枚举所有下标对，按 i<j 顺序找到第一组解。数组不大时可接受 O(n²)。",
  origin="力扣 1 同类 · 两数之和", source="第05章 - 1.pptx · 5.2 数组（slide 26）；第03章 slide 57")

P(chapter=5, section="5.2", topicId="5.2", difficulty=3,
  stem="【整理队列】输入 n 个整数，将所有 0 移到数组末尾，同时保持非零元素的相对顺序。输出处理后的数组，用空格分隔。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, a[1000];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    // 双指针或先输出非零再补零\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];int k=0;for(int i=0;i<n;i++)if(a[i]!=0)a[k++]=a[i];while(k<n)a[k++]=0;for(int i=0;i<n;i++){if(i)cout<<\" \";cout<<a[i];}}\n",
  tests=[{"input":"5\n0 1 0 3 12\n","output":"1 3 12 0 0"},{"input":"3\n0 0 1\n","output":"1 0 0"},{"input":"4\n1 2 3 4\n","output":"1 2 3 4","hidden":True}],
  hints=["用一个写指针 k 收集非零元素。", "最后把 k 之后的位置补 0。"],
  explain="双指针原地整理：读指针扫描，写指针只接收非零元素；扫描完后剩余位置置 0。",
  origin="力扣 283 同类 · 移动零", source="第05章 - 1.pptx · 5.2 数组元素移动（slide 28–29）")

P(chapter=5, section="5.2", topicId="5.2", difficulty=3,
  stem="【去重名册】输入一个已按升序排列的整数数组，原地删除重复元素，使每个元素只出现一次。先输出不重复元素的个数 k，再输出前 k 个元素（空格分隔）。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, a[1000];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    // 双指针原地去重\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];if(n==0){cout<<0;return 0;}int k=1;for(int i=1;i<n;i++)if(a[i]!=a[k-1])a[k++]=a[i];cout<<k<<\"\\n\";for(int i=0;i<k;i++){if(i)cout<<\" \";cout<<a[i];}}\n",
  tests=[{"input":"7\n1 1 2 2 3 4 4\n","output":"4\n1 2 3 4"},{"input":"1\n5\n","output":"1\n5"},{"input":"5\n1 2 3 4 5\n","output":"5\n1 2 3 4 5","hidden":True}],
  hints=["数组有序，重复元素一定相邻。", "k 既表示已保留元素个数，也表示下一个写入位置。"],
  explain="有序条件下可用读写双指针原地去重：只把与前一个保留值不同的元素写到 k 位置。",
  origin="力扣 26 同类 · 删除有序数组中的重复项", source="第05章 - 1.pptx · 5.2 数组元素删除（slide 28）")

P(chapter=5, section="5.2", topicId="5.2", difficulty=3,
  stem="【合并成绩单】输入两个已经升序排列的整数数组，将它们合并为一个仍升序的数组并输出。第一行 n，第二行 n 个数，第三行 m，第四行 m 个数。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, m, a[500], b[500], c[1000];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    cin >> m;\n    for (int i = 0; i < m; i++) cin >> b[i];\n    // 双指针合并\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,m,a[500],b[500],c[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];cin>>m;for(int i=0;i<m;i++)cin>>b[i];int i=0,j=0,k=0;while(i<n&&j<m)c[k++]=(a[i]<=b[j]?a[i++]:b[j++]);while(i<n)c[k++]=a[i++];while(j<m)c[k++]=b[j++];for(int x=0;x<k;x++){if(x)cout<<\" \";cout<<c[x];}}\n",
  tests=[{"input":"3\n1 3 5\n3\n2 4 6\n","output":"1 2 3 4 5 6"},{"input":"2\n1 2\n3\n3 4 5\n","output":"1 2 3 4 5"},{"input":"1\n10\n1\n1\n","output":"1 10","hidden":True}],
  hints=["i、j 分别扫描两个数组，比较后写入 c。", "一个数组扫描完后，把另一个剩余元素接上。"],
  explain="归并双指针：每次取两个有序数组当前较小者，最后处理剩余段。",
  origin="力扣 88 同类 · 合并两个有序数组", source="第05章 - 1.pptx · 5.2 数组与归并思想（slide 26–27）")

P(chapter=5, section="5.2", topicId="5.2", difficulty=2,
  stem="【大数加一】用一个整数数组表示一个非负整数（高位在前），在该数基础上加一，输出结果数组。例如 [1,2,9] 输出 1 3 0。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, a[1000];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    // 从末位开始进位\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,a[1001];cin>>n;for(int i=0;i<n;i++)cin>>a[i];for(int i=n-1;i>=0;i--){if(a[i]<9){a[i]++;for(int j=0;j<n;j++){if(j)cout<<\" \";cout<<a[j];}return 0;}a[i]=0;}cout<<1;for(int i=0;i<n;i++)cout<<\" \"<<a[i];}\n",
  tests=[{"input":"3\n1 2 9\n","output":"1 3 0"},{"input":"1\n9\n","output":"1 0"},{"input":"4\n1 2 3 4\n","output":"1 2 3 5","hidden":True}],
  hints=["从最后一位开始，遇到小于 9 的位就加一并结束。", "如果全部是 9，需要额外输出一个 1，再补 n 个 0。"],
  explain="模拟十进制加法：从末尾向前处理进位；若最高位也进位，则结果比原数组多一位。",
  origin="力扣 66 同类 · 加一", source="第05章 - 1.pptx · 5.2 数组（slide 26）")

P(chapter=5, section="5.4", topicId="5.4", difficulty=3,
  stem="【杨辉三角】输入正整数 n，输出杨辉三角的前 n 行。每行数字用空格分隔，行末不输出多余空格。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, a[30][30] = {};\n    cin >> n;\n    // 构造并输出杨辉三角\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,a[30][30]={};cin>>n;for(int i=0;i<n;i++){a[i][0]=a[i][i]=1;for(int j=1;j<i;j++)a[i][j]=a[i-1][j-1]+a[i-1][j];for(int j=0;j<=i;j++){if(j)cout<<\" \";cout<<a[i][j];}cout<<\"\\n\";}}\n",
  tests=[{"input":"5\n","output":"1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1"},{"input":"1\n","output":"1"},{"input":"3\n","output":"1\n1 1\n1 2 1","hidden":True}],
  hints=["每行首尾元素为 1。", "a[i][j] = a[i-1][j-1] + a[i-1][j]。"],
  explain="二维数组按行递推，每个内部元素等于上一行左上方与正上方元素之和。",
  origin="原创情境 · 杨辉三角", source="第05章 - 1.pptx · 5.2 二维数组（slide 82–87）")

P(chapter=5, section="5.4", topicId="5.4", difficulty=3,
  stem="【矩阵转置】输入 n 行 m 列的整数矩阵，输出它的转置（m 行 n 列）。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, m, a[50][50];\n    cin >> n >> m;\n    // 读入并输出转置\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,m,a[50][50];cin>>n>>m;for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>a[i][j];for(int j=0;j<m;j++){for(int i=0;i<n;i++){if(i)cout<<\" \";cout<<a[i][j];}cout<<\"\\n\";}}\n",
  tests=[{"input":"2 3\n1 2 3\n4 5 6\n","output":"1 4\n2 5\n3 6"},{"input":"1 1\n7\n","output":"7"},{"input":"3 2\n1 2\n3 4\n5 6\n","output":"1 3 5\n2 4 6","hidden":True}],
  hints=["转置输出时外层枚举行号 j（原列），内层枚举 i（原行）。", "直接输出 a[i][j]，不必新建数组。"],
  explain="转置矩阵的 (j,i) 元素来自原矩阵的 (i,j)。按新行优先顺序输出即可。",
  origin="原创情境 · 矩阵转置", source="第05章 - 1.pptx · 5.2 矩阵转置（slide 88–92）")

P(chapter=5, section="5.4", topicId="5.4", difficulty=2,
  stem="【对角线检查】输入一个 n×n 矩阵，输出主对角线元素之和与副对角线元素之和，用空格分隔。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, a[50][50];\n    cin >> n;\n    // 读入矩阵并累加两条对角线\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,a[50][50];cin>>n;for(int i=0;i<n;i++)for(int j=0;j<n;j++)cin>>a[i][j];int s1=0,s2=0;for(int i=0;i<n;i++){s1+=a[i][i];s2+=a[i][n-1-i];}cout<<s1<<\" \"<<s2;}\n",
  tests=[{"input":"3\n1 2 3\n4 5 6\n7 8 9\n","output":"15 15"},{"input":"2\n1 2\n3 4\n","output":"5 5"},{"input":"1\n8\n","output":"8 8","hidden":True}],
  hints=["主对角线 a[i][i]，副对角线 a[i][n-1-i]。", "中心元素在两条对角线中都会出现，题目要求两条和分别计算。"],
  explain="一次循环同时累加两条对角线，注意副对角线列下标随 i 递减。",
  origin="原创情境 · 矩阵对角线", source="第05章 - 1.pptx · 5.2 二维数组（slide 86–87）")

P(chapter=5, section="5.3", topicId="5.3", difficulty=2,
  stem="【文本体检】输入一行不含换行的字符串（可能含空格），统计字母、数字、空格和其它字符的个数，输出四个整数，用空格分隔。",
  starter="#include <iostream>\n#include <cctype>\nusing namespace std;\n\nint main() {\n    char s[500];\n    cin.getline(s, 500);\n    // 遍历到 '\\0'，用 cctype 函数分类统计\n    return 0;\n}\n",
  solution="#include <iostream>\n#include <cctype>\nusing namespace std;\nint main(){char s[500];cin.getline(s,500);int a=0,b=0,c=0,d=0;for(int i=0;s[i]!='\\0';i++){unsigned char ch=s[i];if(isalpha(ch))a++;else if(isdigit(ch))b++;else if(ch==' ')c++;else d++;}cout<<a<<\" \"<<b<<\" \"<<c<<\" \"<<d;}\n",
  tests=[{"input":"C++ 2026!\n","output":"1 4 1 3"},{"input":"abc 123\n","output":"3 3 1 0"},{"input":"Hello World\n","output":"10 0 1 0","hidden":True}],
  hints=["用 cin.getline 读取含空格的行。", "cctype 函数参数可先转 unsigned char，避免负字符值问题。"],
  explain="字符串以 '\\0' 结束；遍历并用 isalpha、isdigit 分类。空格和其他字符分别计数。",
  origin="原创情境 · 文本分类统计", source="第05章 - 1.pptx · 5.2 字符数组（slide 56–62）；第04章-01 slide 28")

P(chapter=5, section="5.3", topicId="5.3", difficulty=2,
  stem="【大小写翻转】输入一个不含空格的字符串，把其中大写字母改成小写、小写字母改成大写，其他字符不变，输出处理后的字符串。",
  starter="#include <iostream>\n#include <cctype>\nusing namespace std;\n\nint main() {\n    char s[500];\n    cin >> s;\n    // 遍历并翻转字母大小写\n    return 0;\n}\n",
  solution="#include <iostream>\n#include <cctype>\nusing namespace std;\nint main(){char s[500];cin>>s;for(int i=0;s[i]!='\\0';i++){unsigned char c=s[i];if(isupper(c))s[i]=tolower(c);else if(islower(c))s[i]=toupper(c);}cout<<s;}\n",
  tests=[{"input":"Hello123\n","output":"hELLO123"},{"input":"C++Lab\n","output":"c++lAB"},{"input":"abc\n","output":"ABC","hidden":True}],
  hints=["isupper 判断大写，tolower 转小写；islower/isupper 同理。", "其他字符保持不变。"],
  explain="字符数组可原地修改；利用 cctype 函数检查并转换大小写。",
  origin="原创情境 · 大小写转换", source="第05章 - 1.pptx · 5.2 字符数组与 cctype（slide 59–60）；第04章-01 slide 28")

P(chapter=5, section="5.3", topicId="5.3", difficulty=2,
  stem="【倒着写的留言】输入一个不含空格的字符串，输出它的逆序。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    char s[500];\n    cin >> s;\n    // 双指针交换或倒序输出\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){char s[500];cin>>s;int n=0;while(s[n]!='\\0')n++;for(int i=0;i<n/2;i++){char t=s[i];s[i]=s[n-1-i];s[n-1-i]=t;}cout<<s;}\n",
  tests=[{"input":"abcde\n","output":"edcba"},{"input":"C++\n","output":"++C"},{"input":"a\n","output":"a","hidden":True}],
  hints=["先求长度 len。", "i 从 0 到 len/2-1 交换 s[i] 与 s[len-1-i]。"],
  explain="双指针从两端向中间交换，时间复杂度 O(n)，不需要额外数组。",
  origin="原创情境 · 字符串逆序", source="第05章 - 1.pptx · 5.2 字符串逆序（slide 71–73）")

P(chapter=5, section="5.3", topicId="5.3", difficulty=2,
  stem="【回文留言】输入一个不含空格的字符串，判断它是否是回文串（正读反读相同）。是输出 YES，否则输出 NO。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    char s[500];\n    cin >> s;\n    // 双指针判断回文\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){char s[500];cin>>s;int n=0;while(s[n]!='\\0')n++;bool ok=true;for(int i=0,j=n-1;i<j;i++,j--)if(s[i]!=s[j]){ok=false;break;}cout<<(ok?\"YES\":\"NO\");}\n",
  tests=[{"input":"level\n","output":"YES"},{"input":"abc\n","output":"NO"},{"input":"a\n","output":"YES"},{"input":"abba\n","output":"YES","hidden":True}],
  hints=["i 从头、j 从尾，向中间比较。", "只要有一对字符不同就不是回文。"],
  explain="字符串回文判断与数组双指针完全一致；无需反转整个字符串。",
  origin="原创情境 · 回文串", source="第05章 - 1.pptx · 5.2 字符串与双指针（slide 56–73）")

P(chapter=5, section="5.3", topicId="5.3", difficulty=3,
  stem="【查找关键词】输入主串和子串（均不含空格），输出子串第一次出现的位置（从 0 开始）；找不到输出 -1。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    char s[500], sub[100];\n    cin >> s >> sub;\n    // 朴素子串匹配\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){char s[500],p[100];cin>>s>>p;int n=0,m=0;while(s[n]!='\\0')n++;while(p[m]!='\\0')m++;for(int i=0;i+m<=n;i++){int j=0;while(j<m&&s[i+j]==p[j])j++;if(j==m){cout<<i;return 0;}}cout<<-1;}\n",
  tests=[{"input":"abcabcde\nabc\n","output":"0"},{"input":"hello\nll\n","output":"2"},{"input":"abc\nxyz\n","output":"-1"},{"input":"aaaaa\naa\n","output":"0","hidden":True}],
  hints=["先求两串长度。", "外层 i 只需枚举到 n-m，内层逐字符比较。"],
  explain="朴素匹配：枚举主串起点，逐字符比较；一旦完整匹配就返回起点。",
  origin="原创情境 · 子串查找", source="第05章 - 1.pptx · 5.2 子串查找（slide 67–70）")

P(chapter=5, section="5.3", topicId="5.3", difficulty=3,
  stem="【删除字符】输入一个不含空格的字符串和一个字符，删除字符串中所有该字符后输出结果。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    char s[500], ch;\n    cin >> s >> ch;\n    // 双指针原地保留不等于 ch 的字符\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){char s[500],ch;cin>>s>>ch;int k=0;for(int i=0;s[i]!='\\0';i++)if(s[i]!=ch)s[k++]=s[i];s[k]='\\0';cout<<s;}\n",
  tests=[{"input":"banana\na\n","output":"bnn"},{"input":"hello\nl\n","output":"heo"},{"input":"abc\nz\n","output":"abc","hidden":True}],
  hints=["用 k 记录下一个写入位置。", "复制完所有保留字符后记得补 '\\0'。"],
  explain="原地删除采用读写双指针：读指针扫描原串，写指针只写保留字符，最后补结束标记。",
  origin="原创情境 · 删除指定字符", source="第05章 - 1.pptx · 5.2 字符数组（slide 56–73）")

P(chapter=5, section="5.3", topicId="5.3", difficulty=3,
  stem="【字符串变整数】输入一个只包含数字字符的字符串，把它转换成对应的整数并输出。例如输入 1234 输出 1234。不要使用标准库转换函数。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    char s[100];\n    cin >> s;\n    int n = 0;\n    // 逐位累加：n = n*10 + (s[i]-'0')\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){char s[100];cin>>s;int n=0;for(int i=0;s[i]!='\\0';i++)n=n*10+(s[i]-'0');cout<<n;}\n",
  tests=[{"input":"1234\n","output":"1234"},{"input":"0\n","output":"0"},{"input":"987654321\n","output":"987654321","hidden":True}],
  hints=["字符 '0'～'9' 的编码连续，s[i]-'0' 得到数值。", "初始 n=0，从高位到低位累加。"],
  explain="逐字符把数字字符转成对应数值，再用 n=n*10+d 累加，这是字符串转整数的基本算法。",
  origin="原创情境 · 字符串转整数", source="第05章 - 1.pptx · 5.2 字符串转整数（slide 63–66）")

P(chapter=5, section="5.3", topicId="5.3", difficulty=3,
  stem="【单词计数】输入一行只含字母和空格的文本（末尾无空格），统计其中单词的个数。连续多个空格视为一个分隔。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    char s[500];\n    cin.getline(s, 500);\n    // 统计从空格到非空格的跳变次数\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){char s[500];cin.getline(s,500);int c=0;bool in=false;for(int i=0;s[i]!='\\0';i++){if(s[i]!=' '&&!in){c++;in=true;}else if(s[i]==' ')in=false;}cout<<c;}\n",
  tests=[{"input":"hello world\n","output":"2"},{"input":"one   two  three\n","output":"3"},{"input":"abc\n","output":"1"},{"input":"a b c d\n","output":"4","hidden":True}],
  hints=["用一个 in 标记当前是否在单词内部。", "从空格进入非空格时单词数加一。"],
  explain="不需要 split；一次扫描根据“上一字符是否为空格”判断新单词的开始。",
  origin="原创情境 · 单词计数", source="第05章 - 1.pptx · 5.2 字符数组（slide 56–62）")

P(chapter=5, section="5.3", topicId="5.3", difficulty=4,
  stem="【括号审查】输入一个只包含 (、)、[、] 的字符串，判断括号是否合法匹配。合法输出 YES，否则输出 NO。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    char s[500], stack[500];\n    cin >> s;\n    // 用字符数组模拟栈\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){char s[500],st[500];cin>>s;int top=0;bool ok=true;for(int i=0;s[i]!='\\0';i++){if(s[i]=='('||s[i]=='[')st[top++]=s[i];else{if(top==0){ok=false;break;}char c=st[--top];if((s[i]==')'&&c!='(')||(s[i]==']'&&c!='[')){ok=false;break;}}}if(top!=0)ok=false;cout<<(ok?\"YES\":\"NO\");}\n",
  tests=[{"input":"([])\n","output":"YES"},{"input":"([)]\n","output":"NO"},{"input":"(([]))\n","output":"YES"},{"input":"(\n","output":"NO","hidden":True}],
  hints=["遇到左括号入栈，遇到右括号检查栈顶。", "最后栈必须为空。"],
  explain="用数组和 top 指针模拟栈：左括号入栈，右括号与栈顶配对；中途不匹配或最后栈非空都判 NO。",
  origin="力扣 20 同类 · 有效的括号（数组模拟栈）", source="第05章 - 1.pptx · 5.2 一维数组与栈思想（slide 17–26）")

P(chapter=4, section="4.5", topicId="4.4", difficulty=2,
  stem="【快速幂】用递归函数计算 base 的 exp 次方（exp≥0），结果在 long long 范围内。输入 base 和 exp，输出结果。",
  starter="#include <iostream>\nusing namespace std;\n\nlong long power(long long base, int exp) {\n    // 递归：exp==0 返回 1；偶数拆半，奇数多乘一次\n}\n\nint main() {\n    long long b;\n    int e;\n    cin >> b >> e;\n    cout << power(b, e);\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nlong long power(long long b,int e){if(e==0)return 1;long long h=power(b,e/2);if(e%2==0)return h*h;return h*h*b;}\nint main(){long long b;int e;cin>>b>>e;cout<<power(b,e);}\n",
  tests=[{"input":"2 10\n","output":"1024"},{"input":"3 0\n","output":"1"},{"input":"5 3\n","output":"125","hidden":True}],
  hints=["结束条件 exp==0 返回 1。", "先算一半幂 h，再根据奇偶合成。"],
  explain="快速幂把指数折半递归，偶数结果为 h*h，奇数再乘一次 base，显著减少乘法次数。",
  origin="原创情境 · 递归快速幂", source="第04章-02.pptx · 4.5 递归条件与结束条件（slide 15–16）")

P(chapter=4, section="4.5", topicId="4.4", difficulty=3,
  stem="【汉诺塔记录】输入圆盘数 n（1≤n≤8），按递归策略把 n 个圆盘从 A 柱移到 C 柱，B 为辅助柱。每次移动输出一行：from->to。",
  starter="#include <iostream>\nusing namespace std;\n\nvoid hanoi(int n, char from, char to, char via) {\n    // 先移 n-1 个到辅助柱，再移最大盘，最后移回 n-1 个\n}\n\nint main() {\n    int n;\n    cin >> n;\n    hanoi(n, 'A', 'C', 'B');\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nvoid hanoi(int n,char from,char to,char via){if(n==0)return;hanoi(n-1,from,via,to);cout<<from<<\"->\"<<to<<\"\\n\";hanoi(n-1,via,to,from);}\nint main(){int n;cin>>n;hanoi(n,'A','C','B');}\n",
  tests=[{"input":"2\n","output":"A->B\nA->C\nB->C"},{"input":"1\n","output":"A->C"},{"input":"3\n","output":"A->C\nA->B\nC->B\nA->C\nB->A\nB->C\nA->C","hidden":True}],
  hints=["n==0 时直接返回，作为递归边界。", "注意主问题是从 from 移到 to，借助 via。"],
  explain="汉诺塔的递归分解：先把 n-1 个移到辅助柱，再移动最大盘，最后把 n-1 个移到目标柱。",
  origin="原创情境 · 汉诺塔", source="第04章-02.pptx · 4.5 汉诺塔（slide 16–19）")

P(chapter=4, section="4.3", topicId="4.4", difficulty=3,
  stem="【有序查找】输入 n 个严格递增整数和待查找值 x，用二分查找输出 x 第一次出现的下标；不存在输出 -1。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n, x, a[1000];\n    cin >> n;\n    for (int i = 0; i < n; i++) cin >> a[i];\n    cin >> x;\n    // 二分查找\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n,x,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];cin>>x;int l=0,r=n-1,ans=-1;while(l<=r){int m=(l+r)/2;if(a[m]==x){ans=m;break;}else if(a[m]<x)l=m+1;else r=m-1;}cout<<ans;}\n",
  tests=[{"input":"5\n1 3 5 7 9\n5\n","output":"2"},{"input":"5\n1 3 5 7 9\n4\n","output":"-1"},{"input":"1\n10\n10\n","output":"0","hidden":True}],
  hints=["循环条件 left <= right。", "中点用 (left+right)/2，向查找值所在半边收缩。"],
  explain="二分查找每次比较中点并排除一半区间，查找区间为空时仍未找到则返回 -1。",
  origin="原创情境 · 二分查找", source="第04章-01.pptx · 函数与算法；第03章 slide 56；第05章-1 slide 120–123")

P(chapter=5, section="5.3", topicId="5.5", difficulty=2,
  stem="【成绩单】输入 n 个学生的学号和成绩，输出平均分（保留 1 位小数）以及最高分学生的学号。",
  starter="#include <iostream>\n#include <iomanip>\nusing namespace std;\n\nstruct Student { int no; int score; };\n\nint main() {\n    int n;\n    cin >> n;\n    Student a[100];\n    // 读入并统计\n    return 0;\n}\n",
  solution="#include <iostream>\n#include <iomanip>\nusing namespace std;\nstruct Student{int no;int score;};\nint main(){int n;cin>>n;Student a[100];double sum=0;int best=0;for(int i=0;i<n;i++){cin>>a[i].no>>a[i].score;sum+=a[i].score;if(a[i].score>a[best].score)best=i;}cout<<fixed<<setprecision(1)<<sum/n<<\" \"<<a[best].no;}\n",
  tests=[{"input":"3\n1 80\n2 95\n3 70\n","output":"81.7 2"},{"input":"1\n7 100\n","output":"100.0 7"},{"input":"4\n10 60\n11 60\n12 90\n13 90\n","output":"75.0 12","hidden":True}],
  hints=["sum 用 double，避免整数除法。", "最高分并列时保留最先出现的学生。"],
  explain="结构体数组把学号与成绩绑定；一次遍历求总分和最高分下标。",
  origin="原创情境 · 结构体成绩单", source="第05章 - 1.pptx · 5.3 结构体数组（slide 112–115）")

P(chapter=5, section="5.3", topicId="5.5", difficulty=4,
  stem="【成绩排名】输入 n 个学生的学号和成绩，按成绩从高到低排序；成绩相同按学号从小到大。输出排序后的学号和成绩，每行一个。",
  starter="#include <iostream>\nusing namespace std;\n\nstruct Student { int no; int score; };\n\nint main() {\n    int n;\n    cin >> n;\n    Student a[100];\n    // 读入后排序\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nstruct Student{int no;int score;};\nint main(){int n;cin>>n;Student a[100];for(int i=0;i<n;i++)cin>>a[i].no>>a[i].score;for(int i=0;i<n-1;i++)for(int j=i+1;j<n;j++)if(a[j].score>a[i].score||(a[j].score==a[i].score&&a[j].no<a[i].no)){Student t=a[i];a[i]=a[j];a[j]=t;}for(int i=0;i<n;i++)cout<<a[i].no<<\" \"<<a[i].score<<\"\\n\";}\n",
  tests=[{"input":"4\n1 80\n2 90\n3 80\n4 95\n","output":"4 95\n2 90\n1 80\n3 80"},{"input":"3\n3 70\n1 70\n2 70\n","output":"1 70\n2 70\n3 70"},{"input":"1\n9 60\n","output":"9 60","hidden":True}],
  hints=["比较两条记录：成绩高者优先；成绩相同则学号小者优先。", "选择排序或冒泡排序都可，交换整个结构体变量。"],
  explain="多关键字排序：主关键字为成绩降序，次关键字为学号升序；结构体整体赋值简化交换。",
  origin="原创情境 · 结构体排序", source="第05章 - 1.pptx · 5.3 结构数组与排序（slide 112–116）")

P(chapter=5, section="5.5", topicId="5.8", difficulty=4,
  stem="【链表点名】输入 n 个整数，用头插法建立单链表，然后从头到尾输出链表中的数，用空格分隔。",
  starter="#include <iostream>\nusing namespace std;\n\nstruct Node { int v; Node* next; };\n\nint main() {\n    int n;\n    cin >> n;\n    Node* head = nullptr;\n    // 头插法建表，再遍历输出\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nstruct Node{int v;Node* next;};\nint main(){int n;cin>>n;Node* head=nullptr;for(int i=0;i<n;i++){int x;cin>>x;Node* p=new Node; p->v=x; p->next=head; head=p;}for(Node* p=head;p!=nullptr;p=p->next){if(p!=head)cout<<\" \";cout<<p->v;}while(head!=nullptr){Node* p=head;head=head->next;delete p;}}\n",
  tests=[{"input":"5\n1 2 3 4 5\n","output":"5 4 3 2 1"},{"input":"1\n7\n","output":"7"},{"input":"3\n10 20 30\n","output":"30 20 10","hidden":True}],
  hints=["每次创建新结点 p，让 p->next 指向当前 head，再 head=p。", "输出时注意空格，最后释放链表。"],
  explain="头插法把每个新结点插到表头，因此输出顺序与输入相反；动态结点最后要逐个 delete。",
  origin="原创情境 · 单链表头插法", source="第05章 - 2.pptx · 5.5 单链表头插法（slide 64–67、89–93）")

P(chapter=5, section="5.5", topicId="5.8", difficulty=3,
  stem="【动态成绩统计】输入 n，使用 new int[n] 创建动态数组，读入 n 个成绩，输出总分、最低分和最高分（空格分隔），最后释放数组。",
  starter="#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    int* a = new int[n];\n    // 读入统计，最后 delete[]\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;int* a=new int[n];for(int i=0;i<n;i++)cin>>a[i];long long sum=0;int mn=a[0],mx=a[0];for(int i=0;i<n;i++){sum+=a[i];if(a[i]<mn)mn=a[i];if(a[i]>mx)mx=a[i];}cout<<sum<<\" \"<<mn<<\" \"<<mx;delete[] a;}\n",
  tests=[{"input":"5\n80 95 70 100 60\n","output":"405 60 100"},{"input":"1\n88\n","output":"88 88 88"},{"input":"4\n-1 -5 -3 -9\n","output":"-18 -9 -1","hidden":True}],
  hints=["先读入数组再统计，最大值/最小值初值取 a[0]。", "释放动态数组必须写 delete[] a;。"],
  explain="new[] 按运行时的 n 分配数组，遍历统计后用 delete[] 释放；初值取首元素可正确处理全负成绩。",
  origin="原创情境 · 动态数组", source="第05章 - 2.pptx · 5.5 动态数组（slide 44–47）")

P(chapter=5, section="5.1", topicId="5.1", difficulty=2,
  stem="【日程分类】定义枚举 Weekday {MON=1,TUE,WED,THU,FRI,SAT,SUN}。输入 1～7 的整数，输出 WORKDAY（1～5）或 WEEKEND（6～7）。",
  starter="#include <iostream>\nusing namespace std;\n\nenum Weekday { MON=1, TUE, WED, THU, FRI, SAT, SUN };\n\nint main() {\n    int x;\n    cin >> x;\n    // 转成枚举值并判断\n    return 0;\n}\n",
  solution="#include <iostream>\nusing namespace std;\nenum Weekday{MON=1,TUE,WED,THU,FRI,SAT,SUN};\nint main(){int x;cin>>x;Weekday d=(Weekday)x;if(d>=MON&&d<=FRI)cout<<\"WORKDAY\";else cout<<\"WEEKEND\";}\n",
  tests=[{"input":"1\n","output":"WORKDAY"},{"input":"5\n","output":"WORKDAY"},{"input":"6\n","output":"WEEKEND"},{"input":"7\n","output":"WEEKEND","hidden":True}],
  hints=["显式转换 (Weekday)x 把整数变成枚举值。", "枚举值比较时按对应整数比较。"],
  explain="枚举值可作为整型参与比较；输入先转成 Weekday，再判断是否在 MON～FRI 范围。",
  origin="原创情境 · 枚举日程", source="第05章 - 1.pptx · 5.1 枚举类型（slide 4–16）")

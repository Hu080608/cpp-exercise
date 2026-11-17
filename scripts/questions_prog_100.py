# -*- coding: utf-8 -*-
"""第 3 批：100 道综合/情境编程题，统一使用课程 PPT 1–5 章语言范围。"""
from qcommon import q

SRC = {
    '1.4': '第01章.pptx · C++ 程序结构与基本输入输出（slide 33–37）',
    '2.1': '第02章.pptx · 2.2 基本数据类型（slide 3–10）',
    '2.2': '第02章.pptx · 2.3 常量、变量与初始化（slide 11–17）',
    '2.3': '第02章.pptx · 2.3 输入输出与格式控制（slide 18、37–39）',
    '2.4': '第02章.pptx · 2.4 算术、关系与逻辑运算（slide 19–29）',
    '2.5': '第02章.pptx · 2.4–2.5 类型转换与表达式（slide 21–36）',
    '3.1': '第03章.pptx · 3.1–3.2 语句与顺序结构（slide 10–18）',
    '3.2': '第03章.pptx · 3.3 选择结构（slide 19–30）',
    '3.3': '第03章.pptx · 3.4 循环结构（slide 31–64）',
    '3.4': '第03章.pptx · 3.5 转移语句与程序风格（slide 65–83）',
    '4.1': '第04章-01.pptx · 4.2 函数定义与调用（slide 6–16）',
    '4.2': '第04章-01.pptx · 4.3 变量作用域（slide 17–21）',
    '4.3': '第04章-01.pptx · 4.4 标准库函数（slide 22–28）',
    '4.4': '第04章-02.pptx · 4.5 递归函数（slide 3–31）',
    '4.5': '第04章-3.pptx · 4.6 宏、内联、默认参数（slide 14–36）',
    '4.6': '第04章 - 3-2.pptx · 4.6 重载、Lambda、范围 for、auto（slide 3–50）',
    '4.7': '第04章-3.pptx · 4.6 动态内存（slide 37–45）',
    '5.1': '第05章 - 1.pptx · 5.1 枚举类型（slide 4–16）',
    '5.2': '第05章 - 1.pptx · 5.2 一维数组（slide 17–55）',
    '5.3': '第05章 - 1.pptx · 5.2 字符串与字符数组（slide 56–89）',
    '5.4': '第05章 - 1.pptx · 5.2 二维数组（slide 82–109）',
    '5.5': '第05章 - 1.pptx · 5.3 结构体（slide 100–124）',
    '5.6': '第05章 - 1.pptx · 5.4 联合体（slide 125–138）',
    '5.7': '第05章 - 2.pptx · 5.5 指针与函数指针（slide 3–119）',
    '5.8': '第05章 - 2.pptx · 5.5 动态内存与链表（slide 44–103）',
    '5.9': '第05章 - 2.pptx · 5.6 引用类型（slide 120–141）'
}
SECTION = {'1.4':'1.3','2.1':'2.2','2.2':'2.3','2.3':'2.3','2.4':'2.4','2.5':'2.5',
           '3.1':'3.2','3.2':'3.3','3.3':'3.4','3.4':'3.5','4.1':'4.2','4.2':'4.3',
           '4.3':'4.4','4.4':'4.5','4.5':'4.6','4.6':'4.6','4.7':'4.6','5.1':'5.1',
           '5.2':'5.2','5.3':'5.2','5.4':'5.2','5.5':'5.3','5.6':'5.4','5.7':'5.5',
           '5.8':'5.5','5.9':'5.6'}

def P(topic, diff, stem, origin, sol, tests, hint, explain, extra='', starter_body=None):
    chapter = int(topic.split('.')[0])
    body = starter_body if starter_body is not None else (
        '#include <iostream>\n' + (extra + '\n' if extra else '') + 'using namespace std;\n\nint main() {\n    // ' + hint + '\n    return 0;\n}\n')
    q(chapter=chapter, section=SECTION[topic], topicId=topic, type='programming', difficulty=diff,
      stem=stem, origin=origin, starter=body, solution=sol, tests=tests,
      hints=[hint], explain=explain, source=SRC[topic])

# ============ 入门 / 简单：输入输出、表达式、选择 ============
P('2.3', 1, '【文具结账】输入单价和数量，输出总价。',
  '原创情境 · 文具店', '#include <iostream>\nusing namespace std;\nint main(){int p,q;cin>>p>>q;cout<<p*q;}\n',
  [{'input':'12 3\n','output':'36'},{'input':'5 8\n','output':'40'},{'input':'0 7\n','output':'0','hidden':True}],
  '读入单价 price 和数量 count，输出 price * count。', '总价等于单价乘数量，整数乘法不会丢失信息。')

P('2.4', 1, '【矩形菜地】输入长和宽，输出面积和周长，用空格分隔。',
  '原创情境 · 菜地测量', '#include <iostream>\nusing namespace std;\nint main(){int w,h;cin>>w>>h;cout<<w*h<<" "<<2*(w+h);}\n',
  [{'input':'3 4\n','output':'12 14'},{'input':'5 2\n','output':'10 14'},{'input':'1 1\n','output':'1 4','hidden':True}],
  '面积 = 长 × 宽；周长 = 2 × (长 + 宽)。', '两个公式都使用整数运算，最后按顺序输出。')

P('2.5', 1, '【三角形花圃】输入底和高，输出三角形面积，保留 2 位小数。',
  '原创情境 · 花圃面积', '#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){double b,h;cin>>b>>h;cout<<fixed<<setprecision(2)<<b*h/2;}\n',
  [{'input':'4 3\n','output':'6.00'},{'input':'7 2\n','output':'7.00'},{'input':'2.5 4\n','output':'5.00','hidden':True}],
  '面积 = 底 × 高 ÷ 2。', '使用 double 保存底和高，fixed 与 setprecision(2) 固定两位小数。', extra='#include <iomanip>')

P('2.4', 1, '【梯形田地】输入上底、下底和高，输出面积，保留 1 位小数。',
  '原创情境 · 田地面积', '#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){double a,b,h;cin>>a>>b>>h;cout<<fixed<<setprecision(1)<<(a+b)*h/2;}\n',
  [{'input':'2 4 3\n','output':'9.0'},{'input':'3 5 2\n','output':'8.0'},{'input':'1 1 1\n','output':'1.0','hidden':True}],
  '面积 = (上底 + 下底) × 高 ÷ 2。', '先加括号再乘高、除以 2；输出固定一位小数。', extra='#include <iomanip>')

P('2.4', 1, '【时间拆分】输入总秒数（非负整数），输出「分钟:秒」。',
  '原创情境 · 秒表', '#include <iostream>\nusing namespace std;\nint main(){int t;cin>>t;cout<<t/60<<":"<<t%60;}\n',
  [{'input':'125\n','output':'2:5'},{'input':'59\n','output':'0:59'},{'input':'600\n','output':'10:0','hidden':True}],
  '分钟 = 总秒数 / 60；秒 = 总秒数 % 60。', '整除得到完整分钟数，取余得到剩余秒数。')

P('2.4', 1, '【数字拼图】输入一个三位正整数，输出百位、十位、个位的乘积。',
  '原创情境 · 数字拼图', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;cout<<(n/100)*(n/10%10)*(n%10);}\n',
  [{'input':'123\n','output':'6'},{'input':'507\n','output':'0'},{'input':'999\n','output':'729','hidden':True}],
  '百位 n/100，十位 n/10%10，个位 n%10。', '用 / 和 % 拆出三位数字，再相乘。')

P('3.2', 1, '【温度提示】输入整数温度，大于等于 100 输出 BOILING，否则输出 NORMAL。',
  '原创情境 · 水温提示', '#include <iostream>\nusing namespace std;\nint main(){int t;cin>>t;if(t>=100)cout<<"BOILING";else cout<<"NORMAL";}\n',
  [{'input':'100\n','output':'BOILING'},{'input':'99\n','output':'NORMAL'},{'input':'-5\n','output':'NORMAL','hidden':True}],
  '使用 if 判断温度是否达到 100。', '正好 100 度也属于 BOILING，条件要用 >=。')

P('3.2', 1, '【乘车优惠】输入年龄，6 岁以下输出 FREE，6～18 岁输出 HALF，18 岁以上输出 FULL。',
  '原创情境 · 公交优惠', '#include <iostream>\nusing namespace std;\nint main(){int a;cin>>a;if(a<6)cout<<"FREE";else if(a<=18)cout<<"HALF";else cout<<"FULL";}\n',
  [{'input':'5\n','output':'FREE'},{'input':'18\n','output':'HALF'},{'input':'19\n','output':'FULL'},{'input':'6\n','output':'HALF','hidden':True}],
  '按年龄从小到大用 else-if 分段。', '18 岁包含在 HALF 区间，所以第二段条件是 age <= 18。')

P('2.4', 1, '【找较大值】输入两个整数，输出较大的那个。',
  '原创情境 · 比较大小', '#include <iostream>\nusing namespace std;\nint main(){int a,b;cin>>a>>b;cout<<(a>b?a:b);}\n',
  [{'input':'3 9\n','output':'9'},{'input':'-1 -7\n','output':'-1'},{'input':'5 5\n','output':'5','hidden':True}],
  '使用条件运算符或 if 比较两个数。', 'a > b 时取 a，否则取 b；相等时取 b 仍是同一个值。')

P('2.4', 1, '【找最小值】输入三个整数，输出其中的最小值。',
  '原创情境 · 比较三个数', '#include <iostream>\nusing namespace std;\nint main(){int a,b,c;cin>>a>>b>>c;int m=a;if(b<m)m=b;if(c<m)m=c;cout<<m;}\n',
  [{'input':'3 9 -2\n','output':'-2'},{'input':'5 5 5\n','output':'5'},{'input':'-1 0 -3\n','output':'-3','hidden':True}],
  '先把 a 设为当前最小值，再依次和 b、c 比较。', '用当前最小值 m 逐个比较，适合扩展到更多数。')

P('3.2', 1, '【字符分类】输入一个字符，大写字母输出 UPPER，小写字母输出 LOWER，其他输出 OTHER。',
  '原创情境 · 字符分类', '#include <iostream>\nusing namespace std;\nint main(){char c;cin>>c;if(c>=\'A\'&&c<=\'Z\')cout<<"UPPER";else if(c>=\'a\'&&c<=\'z\')cout<<"LOWER";else cout<<"OTHER";}\n',
  [{'input':'A\n','output':'UPPER'},{'input':'m\n','output':'LOWER'},{'input':'7\n','output':'OTHER','hidden':True}],
  '用字符编码区间判断大写和小写。', 'ASCII 编码中 A–Z 与 a–z 分别连续，可以直接比较字符。')

P('3.2', 1, '【成年判断】输入年龄，18 岁及以上输出 ADULT，否则输出 MINOR。',
  '原创情境 · 年龄判断', '#include <iostream>\nusing namespace std;\nint main(){int a;cin>>a;if(a>=18)cout<<"ADULT";else cout<<"MINOR";}\n',
  [{'input':'18\n','output':'ADULT'},{'input':'17\n','output':'MINOR'},{'input':'0\n','output':'MINOR','hidden':True}],
  '使用 >= 判断年龄是否至少为 18。', '边界值 18 属于成年，条件必须是 age >= 18。')

P('3.2', 2, '【三角形分类】输入三条正整数边，输出 EQUILATERAL（等边）、ISOSCELES（等腰）、SCALENE（一般）或 INVALID（不能构成三角形）。',
  '原创情境 · 几何分类', '#include <iostream>\nusing namespace std;\nint main(){int a,b,c;cin>>a>>b>>c;if(a+b<=c||a+c<=b||b+c<=a)cout<<"INVALID";else if(a==b&&b==c)cout<<"EQUILATERAL";else if(a==b||a==c||b==c)cout<<"ISOSCELES";else cout<<"SCALENE";}\n',
  [{'input':'3 3 3\n','output':'EQUILATERAL'},{'input':'3 3 4\n','output':'ISOSCELES'},{'input':'3 4 5\n','output':'SCALENE'},{'input':'1 2 3\n','output':'INVALID','hidden':True}],
  '先判断能否构成三角形，再依次判断等边、等腰、一般。', '三角形必须满足任意两边之和大于第三边；分类顺序要先判断等边。')

P('2.4', 2, '【象限判断】输入非零平面坐标 x、y，输出点所在象限 Q1、Q2、Q3 或 Q4。',
  '原创情境 · 坐标象限', '#include <iostream>\nusing namespace std;\nint main(){int x,y;cin>>x>>y;if(x>0&&y>0)cout<<"Q1";else if(x<0&&y>0)cout<<"Q2";else if(x<0&&y<0)cout<<"Q3";else cout<<"Q4";}\n',
  [{'input':'2 3\n','output':'Q1'},{'input':'-2 3\n','output':'Q2'},{'input':'-2 -3\n','output':'Q3'},{'input':'2 -3\n','output':'Q4','hidden':True}],
  '根据 x、y 的符号判断象限。', '题目保证 x、y 非零，因此只需判断正负；四个分支互斥。')

P('2.4', 2, '【加班工资】某兼职前 40 小时每小时 20 元，超过 40 小时的部分每小时 30 元。输入工作小时数，输出工资。',
  '原创情境 · 兼职工资', '#include <iostream>\nusing namespace std;\nint main(){int h;cin>>h;if(h<=40)cout<<h*20;else cout<<40*20+(h-40)*30;}\n',
  [{'input':'35\n','output':'700'},{'input':'40\n','output':'800'},{'input':'45\n','output':'950'},{'input':'0\n','output':'0','hidden':True}],
  '前 40 小时按 20 元，超出部分按 30 元。', '分段计费时要先把前 40 小时的工资固定为 800 元，再加上超出部分。')

P('2.5', 2, '【书店折扣】输入购书金额，满 100 元打九折，否则打九五折。输出实付金额，保留 2 位小数。',
  '原创情境 · 书店优惠', '#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){double x;cin>>x;double pay=x>=100?x*0.9:x*0.95;cout<<fixed<<setprecision(2)<<pay;}\n',
  [{'input':'120\n','output':'108.00'},{'input':'80\n','output':'76.00'},{'input':'100\n','output':'90.00','hidden':True}],
  '根据金额是否达到 100 使用不同折扣。', '100 元正好满足满减条件；结果用 fixed 固定两位小数。', extra='#include <iomanip>')

P('3.2', 2, '【快递计费】首重 1 千克收费 10 元，超过 1 千克的部分每千克加收 5 元（不足 1 千克按 1 千克计）。输入整数重量，输出运费。',
  '原创情境 · 快递柜', '#include <iostream>\nusing namespace std;\nint main(){int w;cin>>w;if(w<=1)cout<<10;else cout<<10+(w-1)*5;}\n',
  [{'input':'1\n','output':'10'},{'input':'3\n','output':'20'},{'input':'0\n','output':'10','hidden':True}],
  '首重 1 千克收费 10 元，超过部分每千克 5 元。', '题目规定重量为整数且不足 1 千克按 1 千克计，因此直接对超出整数千克计费。')

P('3.2', 2, '【月份天数】输入年份和月份（1～12），输出该月天数。',
  '原创情境 · 日历查询', '#include <iostream>\nusing namespace std;\nint main(){int y,m;cin>>y>>m;int d;if(m==2)d=(y%400==0||(y%4==0&&y%100!=0))?29:28;else if(m==4||m==6||m==9||m==11)d=30;else d=31;cout<<d;}\n',
  [{'input':'2024 2\n','output':'29'},{'input':'1900 2\n','output':'28'},{'input':'2023 4\n','output':'30'},{'input':'2023 12\n','output':'31','hidden':True}],
  '二月先判断闰年；4、6、9、11 月为 30 天，其余为 31 天。', '把闰年判断嵌套在二月分支，其他月份按大小月分类。')

P('2.5', 2, '【体重指数】输入体重（千克）和身高（米），计算 BMI = 体重 / 身高²，并输出 UNDER（<18.5）、NORMAL（18.5～23.9）或 OVER（≥24）。',
  '原创情境 · 健康记录', '#include <iostream>\nusing namespace std;\nint main(){double w,h;cin>>w>>h;double b=w/(h*h);if(b<18.5)cout<<"UNDER";else if(b<24)cout<<"NORMAL";else cout<<"OVER";}\n',
  [{'input':'50 1.6\n','output':'NORMAL'},{'input':'40 1.7\n','output':'UNDER'},{'input':'90 1.7\n','output':'OVER'},{'input':'60 1.7\n','output':'NORMAL','hidden':True}],
  '先计算 BMI，再按区间输出分类。', '区间判断要注意 18.5 与 24 两个边界；用 else-if 避免重叠。')

P('2.4', 1, '【乘积符号】输入两个整数，输出它们乘积的符号：POSITIVE、NEGATIVE 或 ZERO。',
  '原创情境 · 符号判断', '#include <iostream>\nusing namespace std;\nint main(){int a,b;cin>>a>>b;long long p=(long long)a*b;if(p>0)cout<<"POSITIVE";else if(p<0)cout<<"NEGATIVE";else cout<<"ZERO";}\n',
  [{'input':'2 3\n','output':'POSITIVE'},{'input':'-2 3\n','output':'NEGATIVE'},{'input':'0 9\n','output':'ZERO'},{'input':'-2 -3\n','output':'POSITIVE','hidden':True}],
  '用 long long 保存乘积，避免 a*b 在 int 中溢出。', '根据乘积的正负零输出；乘积可能很大，因此用 long long 暂存。')

P('3.2', 2, '【三数排序】输入三个整数，按从大到小输出，用空格分隔。',
  '原创情境 · 排序三个数', '#include <iostream>\nusing namespace std;\nint main(){int a,b,c;cin>>a>>b>>c;if(a<b){int t=a;a=b;b=t;}if(a<c){int t=a;a=c;c=t;}if(b<c){int t=b;b=c;c=t;}cout<<a<<" "<<b<<" "<<c;}\n',
  [{'input':'3 9 5\n','output':'9 5 3'},{'input':'-1 7 2\n','output':'7 2 -1'},{'input':'5 5 1\n','output':'5 5 1','hidden':True}],
  '用三次两两交换把最大值放到 a、次大值放到 b。', '这相当于对三个变量做冒泡排序，交换时借助临时变量。')

P('3.2', 2, '【数字生肖】输入年份，按 12 年循环输出生肖：鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪。以 2020 年为鼠年。',
  '原创情境 · 生肖查询', '#include <iostream>\nusing namespace std;\nint main(){int y;cin>>y;int k=(y-2020)%12;if(k<0)k+=12;switch(k){case 0:cout<<"鼠";break;case 1:cout<<"牛";break;case 2:cout<<"虎";break;case 3:cout<<"兔";break;case 4:cout<<"龙";break;case 5:cout<<"蛇";break;case 6:cout<<"马";break;case 7:cout<<"羊";break;case 8:cout<<"猴";break;case 9:cout<<"鸡";break;case 10:cout<<"狗";break;default:cout<<"猪";}}\n',
  [{'input':'2020\n','output':'鼠'},{'input':'2021\n','output':'牛'},{'input':'2019\n','output':'猪'},{'input':'2024\n','output':'龙','hidden':True}],
  '用 (year-2020)%12 得到生肖下标，再用 switch 输出。', 'C++ 对负数取余可能为负，先加 12 调整到 0～11。')

P('2.4', 1, '【数字洞】输入两个整数 a、b，输出 (a+b)² - |a-b| 的值。',
  '原创情境 · 数学小游戏', '#include <iostream>\n#include <cmath>\nusing namespace std;\nint main(){int a,b;cin>>a>>b;int s=a+b;cout<<s*s-abs(a-b);}\n',
  [{'input':'2 3\n','output':'24'},{'input':'-1 4\n','output':'4'},{'input':'5 5\n','output':'100','hidden':True}],
  '先求和、求绝对差，再代入公式。', '平方可以写成 s*s；绝对差用 abs 函数。', extra='#include <cmath>')

# ============ 循环与数列 ============
P('3.3', 1, '【偶数求和】输入正整数 n，输出 1 到 n 之间所有偶数的和。',
  '原创情境 · 偶数统计', '#include <iostream>\nusing namespace std;\nint main(){int n,s=0;cin>>n;for(int i=2;i<=n;i+=2)s+=i;cout<<s;}\n',
  [{'input':'10\n','output':'30'},{'input':'5\n','output':'6'},{'input':'1\n','output':'0','hidden':True}],
  'for 循环从 2 开始，每次加 2。', '循环变量只遍历偶数，累加 sum。', starter_body='#include <iostream>\nusing namespace std;\nint main() {\n    int n, sum = 0;\n    cin >> n;\n    // 从 2 开始，每次加 2 累加\n    cout << sum;\n    return 0;\n}\n')

P('3.3', 1, '【奇数求和】输入正整数 n，输出 1 到 n 之间所有奇数的和。',
  '原创情境 · 奇数统计', '#include <iostream>\nusing namespace std;\nint main(){int n,s=0;cin>>n;for(int i=1;i<=n;i+=2)s+=i;cout<<s;}\n',
  [{'input':'10\n','output':'25'},{'input':'1\n','output':'1'},{'input':'2\n','output':'1','hidden':True}],
  'for 循环从 1 开始，每次加 2。', '从 1 开始遍历奇数并累加。')

P('3.3', 2, '【因数个数】输入正整数 n，输出它的正因数个数。',
  '原创情境 · 因数统计', '#include <iostream>\nusing namespace std;\nint main(){int n,c=0;cin>>n;for(int i=1;i<=n;i++)if(n%i==0)c++;cout<<c;}\n',
  [{'input':'12\n','output':'6'},{'input':'7\n','output':'2'},{'input':'1\n','output':'1','hidden':True}],
  '枚举 1 到 n，遇到能整除的数就计数。', 'n % i == 0 表示 i 是 n 的因数；1 和 n 本身也算。')

P('3.3', 1, '【3 的倍数】输入正整数 n，按从小到大输出 1 到 n 中所有 3 的倍数，用空格分隔。',
  '原创情境 · 倍数筛选', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;bool first=true;for(int i=3;i<=n;i+=3){if(!first)cout<<" ";cout<<i;first=false;}}\n',
  [{'input':'10\n','output':'3 6 9'},{'input':'3\n','output':'3'},{'input':'2\n','output':'','hidden':True}],
  '从 3 开始每次加 3；用 first 控制空格。', '如果没有任何倍数，程序不输出内容；用 first 避免行末多余空格。')

P('3.3', 2, '【数位之和】输入一个非负整数，输出它各位数字之和。',
  '原创情境 · 数位和', '#include <iostream>\nusing namespace std;\nint main(){long long n;cin>>n;int s=0;while(n>0){s+=n%10;n/=10;}cout<<s;}\n',
  [{'input':'1234\n','output':'10'},{'input':'0\n','output':'0'},{'input':'987654321\n','output':'45','hidden':True}],
  'while (n > 0) { sum += n % 10; n /= 10; }', '注意 0 本身要输出 0；使用 long long 可处理较大的输入。')

P('3.3', 2, '【数位长度】输入一个正整数，输出它有多少位。',
  '原创情境 · 数字位数', '#include <iostream>\nusing namespace std;\nint main(){long long n;cin>>n;int c=0;while(n>0){c++;n/=10;}cout<<c;}\n',
  [{'input':'1234\n','output':'4'},{'input':'7\n','output':'1'},{'input':'100000\n','output':'6','hidden':True}],
  '每除以 10 一次，位数加一。', '循环直到 n 变为 0，计数器就是位数。')

P('3.3', 2, '【零的个数】输入一个非负整数，统计它十进制表示中数字 0 出现的次数。',
  '原创情境 · 数字统计', '#include <iostream>\nusing namespace std;\nint main(){long long n;cin>>n;if(n==0){cout<<1;return 0;}int c=0;while(n>0){if(n%10==0)c++;n/=10;}cout<<c;}\n',
  [{'input':'10020\n','output':'3'},{'input':'123\n','output':'0'},{'input':'0\n','output':'1','hidden':True}],
  '特判 n==0 后，循环检查每一位并统计 0。', '0 本身的十进制表示有一个 0，需要单独处理。')

P('3.3', 2, '【平方和】输入正整数 n，输出 1² + 2² + … + n²。',
  '原创情境 · 平方和', '#include <iostream>\nusing namespace std;\nint main(){int n;long long s=0;cin>>n;for(int i=1;i<=n;i++)s+=(long long)i*i;cout<<s;}\n',
  [{'input':'3\n','output':'14'},{'input':'5\n','output':'55'},{'input':'100\n','output':'338350','hidden':True}],
  '循环累加 i*i，使用 long long 保存结果。', 'n 较大时平方和可能超过 int 范围，因此使用 long long。')

P('3.3', 2, '【乘法表】输入 n（1≤n≤9），输出 n 的乘法表第 1 到 9 项，用空格分隔。',
  '原创情境 · 乘法表', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;for(int i=1;i<=9;i++){if(i>1)cout<<" ";cout<<n*i;}}\n',
  [{'input':'3\n','output':'3 6 9 12 15 18 21 24 27'},{'input':'1\n','output':'1 2 3 4 5 6 7 8 9'},{'input':'9\n','output':'9 18 27 36 45 54 63 72 81','hidden':True}],
  'i 从 1 到 9，输出 n*i，第一项后加空格。', '注意输出格式：不能有行末多余空格。')

P('3.3', 2, '【星星直角三角形】输入 n，输出 n 行，第 i 行有 i 个 *。',
  '原创情境 · 图案输出', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;for(int i=1;i<=n;i++){for(int j=1;j<=i;j++)cout<<\'*\';cout<<\'\\n\';}}\n',
  [{'input':'3\n','output':'*\n**\n***'},{'input':'1\n','output':'*'},{'input':'4\n','output':'*\n**\n***\n****','hidden':True}],
  '外层控制行，内层输出 i 个星号。', '这是嵌套循环：每行结束后输出换行。')

P('2.4', 2, '【循环幂】输入底数 a 和非负整数 n，输出 aⁿ。',
  '原创情境 · 迭代幂', '#include <iostream>\nusing namespace std;\nint main(){long long a,n,r=1;cin>>a>>n;for(int i=0;i<n;i++)r*=a;cout<<r;}\n',
  [{'input':'5 3\n','output':'125'},{'input':'2 0\n','output':'1'},{'input':'3 4\n','output':'81','hidden':True}],
  '结果初始为 1，循环 n 次乘 a。', 'n=0 时返回 1；用 long long 保存结果，避免中等规模幂溢出。')

P('3.3', 2, '【闰年区间】输入 a、b（a≤b），统计区间 [a,b] 中闰年的个数。',
  '原创情境 · 闰年统计', '#include <iostream>\nusing namespace std;\nint main(){int a,b,c=0;cin>>a>>b;for(int y=a;y<=b;y++)if(y%400==0||(y%4==0&&y%100!=0))c++;cout<<c;}\n',
  [{'input':'2000 2004\n','output':'2'},{'input':'1900 1900\n','output':'0'},{'input':'2000 2000\n','output':'1','hidden':True}],
  '枚举区间内每一年，使用闰年条件计数。', '闰年条件：能被 400 整除，或能被 4 整除且不能被 100 整除。')

P('3.3', 2, '【完全平方数】输入非负整数 n，统计 1 到 n 中有多少个完全平方数。',
  '原创情境 · 平方数', '#include <iostream>\nusing namespace std;\nint main(){int n,c=0;cin>>n;for(int i=1;i*i<=n;i++)c++;cout<<c;}\n',
  [{'input':'20\n','output':'4'},{'input':'1\n','output':'1'},{'input':'0\n','output':'0','hidden':True}],
  '枚举 i，只要 i*i ≤ n 就计数。', 'i 从 1 开始，i*i 不会超过 n；n=0 时计数为 0。')

P('3.3', 2, '【前 n 项 Fibonacci 和】输入 n，输出 Fibonacci 数列前 n 项之和。规定 F1=F2=1。',
  '原创情境 · Fibonacci 求和', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;long long a=1,b=1,s=0;for(int i=1;i<=n;i++){s+=a;long long t=a+b;a=b;b=t;}cout<<s;}\n',
  [{'input':'1\n','output':'1'},{'input':'5\n','output':'12'},{'input':'10\n','output':'143','hidden':True}],
  '滚动维护相邻两项，同时累加当前项。', '用 long long 保存 Fibonacci 项与和，避免较大 n 时溢出。')

P('3.3', 1, '【倒计时】输入非负整数 n，从 n 开始倒序输出到 0，用空格分隔。',
  '原创情境 · 倒计时', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;for(int i=n;i>=0;i--){if(i<n)cout<<" ";cout<<i;}}\n',
  [{'input':'3\n','output':'3 2 1 0'},{'input':'0\n','output':'0'},{'input':'1\n','output':'1 0','hidden':True}],
  '从 n 循环到 0。', '循环变量递减，用 i<n 控制前导空格。')

P('3.3', 2, '【读到 -1 为止】输入若干整数，以 -1 结束，输出这些整数的和（-1 不参与）。',
  '原创情境 · 哨兵输入', '#include <iostream>\nusing namespace std;\nint main(){int x,s=0;cin>>x;while(x!=-1){s+=x;cin>>x;}cout<<s;}\n',
  [{'input':'1 2 3 -1\n','output':'6'},{'input':'-1\n','output':'0'},{'input':'-5 10 -1\n','output':'5','hidden':True}],
  '先读入一个数，循环直到读到 -1。', '循环体内累加当前数，再读取下一个数；-1 是结束标记，不参与求和。')

P('3.3', 2, '【平均分】输入若干整数成绩，以 -1 结束，输出平均分，保留 1 位小数。',
  '原创情境 · 成绩平均', '#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){int x,n=0,s=0;cin>>x;while(x!=-1){s+=x;n++;cin>>x;}if(n==0)cout<<"0.0";else cout<<fixed<<setprecision(1)<<(double)s/n;}\n',
  [{'input':'1 2 3 -1\n','output':'2.0'},{'input':'5 -1\n','output':'5.0'},{'input':'-1\n','output':'0.0','hidden':True}],
  '统计个数与总和，最后用 double 相除。', '输入可能为空，需要特判 n==0，避免除以 0。', extra='#include <iomanip>')

P('3.3', 2, '【最大值扫描】输入若干正整数，以 -1 结束，输出其中的最大值。输入至少有一个正整数。',
  '原创情境 · 扫描最大值', '#include <iostream>\nusing namespace std;\nint main(){int x,m=0;cin>>x;if(x!=-1)m=x;while(x!=-1){if(x>m)m=x;cin>>x;}cout<<m;}\n',
  [{'input':'2 9 4 -1\n','output':'9'},{'input':'5 -1\n','output':'5'},{'input':'1 2 3 -1\n','output':'3','hidden':True}],
  '用一个 m 记录当前最大值。', '输入保证至少有一个正整数，先把第一个数作为初值，再继续扫描。')

P('3.3', 1, '【正数计数】输入若干整数，以 0 结束，统计其中正数的个数。',
  '原创情境 · 正数计数', '#include <iostream>\nusing namespace std;\nint main(){int x,c=0;cin>>x;while(x!=0){if(x>0)c++;cin>>x;}cout<<c;}\n',
  [{'input':'1 -2 3 0\n','output':'2'},{'input':'0\n','output':'0'},{'input':'-1 -2 0\n','output':'0','hidden':True}],
  '循环读取到 0，判断 x > 0 后计数。', '0 是结束标记不参与统计，负数也不是正数。')

P('2.5', 2, '【十进制转二进制】输入非负整数 n，输出它的二进制表示（不输出前导 0）。',
  '原创情境 · 进制转换', '#include <iostream>\nusing namespace std;\nint main(){int n,a[40],k=0;cin>>n;if(n==0){cout<<0;return 0;}while(n>0){a[k++]=n%2;n/=2;}for(int i=k-1;i>=0;i--)cout<<a[i];}\n',
  [{'input':'13\n','output':'1101'},{'input':'0\n','output':'0'},{'input':'1\n','output':'1','hidden':True}],
  '除 2 取余，把余数存入数组，最后逆序输出。', '0 要单独输出；数组保存的是低位到高位的余数。')

P('2.5', 3, '【十进制转十六进制】输入非负整数 n，输出它的大写十六进制表示（不输出前导 0）。',
  '原创情境 · 进制转换', '#include <iostream>\nusing namespace std;\nint main(){int n,a[40],k=0;char h[]="0123456789ABCDEF";cin>>n;if(n==0){cout<<0;return 0;}while(n>0){a[k++]=n%16;n/=16;}for(int i=k-1;i>=0;i--)cout<<h[a[i]];}\n',
  [{'input':'26\n','output':'1A'},{'input':'255\n','output':'FF'},{'input':'0\n','output':'0'},{'input':'4096\n','output':'1000','hidden':True}],
  '除 16 取余，用字符表映射 0～15 到 0～9、A～F。', '余数数组从低位到高位保存，输出时逆序；0 特殊处理。')

P('3.3', 2, '【所有因数】输入正整数 n，按从小到大输出它的全部正因数，用空格分隔。',
  '原创情境 · 因数枚举', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;for(int i=1;i<=n;i++)if(n%i==0){if(i>1)cout<<" ";cout<<i;}}\n',
  [{'input':'12\n','output':'1 2 3 4 6 12'},{'input':'7\n','output':'1 7'},{'input':'1\n','output':'1','hidden':True}],
  '枚举 1 到 n，能整除就输出。', '因为从小到大枚举，输出天然有序；注意空格控制。')

P('3.3', 2, '【因数和】输入正整数 n，输出它所有正因数之和。',
  '原创情境 · 因数和', '#include <iostream>\nusing namespace std;\nint main(){int n;long long s=0;cin>>n;for(int i=1;i<=n;i++)if(n%i==0)s+=i;cout<<s;}\n',
  [{'input':'12\n','output':'28'},{'input':'7\n','output':'8'},{'input':'1\n','output':'1','hidden':True}],
  '枚举因数并累加，包含 1 和 n 本身。', '与因数个数题类似，只是把计数改成累加。')

P('3.3', 3, '【完数统计】输入 n，输出 1 到 n 之间完数的个数。完数等于其所有真因子之和。',
  '原创情境 · 完数', '#include <iostream>\nusing namespace std;\nint main(){int n,c=0;cin>>n;for(int x=2;x<=n;x++){int s=1;for(int d=2;d*d<=x;d++)if(x%d==0){s+=d;if(d!=x/d)s+=x/d;}if(s==x)c++;}cout<<c;}\n',
  [{'input':'30\n','output':'2'},{'input':'5\n','output':'0'},{'input':'1000\n','output':'3','hidden':True}],
  '1 是每个大于 1 的数的真因子；成对枚举因子求和。', '2 和 3 不是完数；30 以内的完数是 6 和 28。')

P('3.3', 3, '【第 n 个素数】输入正整数 n，输出第 n 个素数。',
  '原创情境 · 素数序列', '#include <iostream>\nusing namespace std;\nint main(){int n,c=0,x=2;cin>>n;while(true){bool ok=true;for(int i=2;i*i<=x;i++)if(x%i==0){ok=false;break;}if(ok){c++;if(c==n){cout<<x;return 0;}}x++;}}\n',
  [{'input':'1\n','output':'2'},{'input':'5\n','output':'11'},{'input':'50\n','output':'229','hidden':True}],
  '从 2 开始逐个检查素数，数到第 n 个为止。', '内层试除到 √x 即可；找到第 n 个素数后立即输出并结束。')

P('3.3', 3, '【素数列表】输入 n，按从小到大输出不超过 n 的所有素数，用空格分隔。',
  '原创情境 · 素数筛选', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;bool first=true;for(int x=2;x<=n;x++){bool ok=true;for(int i=2;i*i<=x;i++)if(x%i==0){ok=false;break;}if(ok){if(!first)cout<<" ";cout<<x;first=false;}}}\n',
  [{'input':'20\n','output':'2 3 5 7 11 13 17 19'},{'input':'2\n','output':'2'},{'input':'1\n','output':'','hidden':True}],
  '外层枚举 2～n，内层试除判断素数。', '1 不是素数；用 first 控制空格，没有素数时不输出内容。')

P('3.3', 3, '【孪生素数】输入 n，统计不超过 n 的孪生素数对 (p,p+2) 数量。',
  '原创情境 · 孪生素数', '#include <iostream>\nusing namespace std;\nbool prime(int x){if(x<2)return false;for(int i=2;i*i<=x;i++)if(x%i==0)return false;return true;}\nint main(){int n,c=0;cin>>n;for(int p=2;p+2<=n;p++)if(prime(p)&&prime(p+2))c++;cout<<c;}\n',
  [{'input':'10\n','output':'2'},{'input':'20\n','output':'4'},{'input':'100\n','output':'8','hidden':True}],
  '写一个 prime 函数判断素数，再枚举 p 和 p+2。', '把素数判断封装成函数，外层枚举所有可能的孪生素数对。')

# ============ 一维 / 二维数组 ============
P('5.2', 1, '【班级总分】输入 n 和 n 个整数，输出它们的和。',
  '原创情境 · 数组求和', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];long long s=0;cin>>n;for(int i=0;i<n;i++){cin>>a[i];s+=a[i];}cout<<s;}\n',
  [{'input':'5\n1 2 3 4 5\n','output':'15'},{'input':'1\n-7\n','output':'-7'},{'input':'4\n10 -2 3 -8\n','output':'3','hidden':True}],
  '用数组保存 n 个数，遍历求和。', '数组下标从 0 到 n-1；总和用 long long 更稳妥。', starter_body='#include <iostream>\nusing namespace std;\nint main() {\n    int n, a[1000];\n    cin >> n;\n    // 读入并累加\n    return 0;\n}\n')

P('5.2', 1, '【最大值与最小值】输入 n 个整数，输出最大值和最小值，用空格分隔。',
  '原创情境 · 数组极值', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];int mx=a[0],mn=a[0];for(int i=1;i<n;i++){if(a[i]>mx)mx=a[i];if(a[i]<mn)mn=a[i];}cout<<mx<<" "<<mn;}\n',
  [{'input':'3\n3 9 2\n','output':'9 2'},{'input':'4\n-1 -7 -2 -9\n','output':'-1 -9'},{'input':'1\n5\n','output':'5 5','hidden':True}],
  '最大值与最小值都初始化为第一个元素。', '从第二个元素开始更新；全负数时也能得到正确结果。')

P('5.2', 2, '【高于平均分】输入 n 个整数成绩，输出高于平均分的成绩个数。',
  '原创情境 · 成绩分析', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;double s=0;for(int i=0;i<n;i++){cin>>a[i];s+=a[i];}double avg=s/n;int c=0;for(int i=0;i<n;i++)if(a[i]>avg)c++;cout<<c;}\n',
  [{'input':'4\n1 2 3 4\n','output':'2'},{'input':'3\n10 10 10\n','output':'0'},{'input':'5\n60 70 80 90 100\n','output':'2','hidden':True}],
  '先求平均分，再统计严格大于平均分的元素。', '平均值用 double，避免整数除法；条件是大于而不是大于等于。')

P('5.2', 2, '【第二高分】输入 n（n≥2）个整数，输出按从大到小排序后第二大的元素（允许与最大值相等）。',
  '原创情境 · 第二高分', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];for(int i=0;i<n-1;i++)for(int j=i+1;j<n;j++)if(a[j]>a[i]){int t=a[i];a[i]=a[j];a[j]=t;}cout<<a[1];}\n',
  [{'input':'3\n3 9 2\n','output':'3'},{'input':'3\n5 5 1\n','output':'5'},{'input':'5\n-1 -7 -2 -9 0\n','output':'-1','hidden':True}],
  '先把数组降序排序，再输出下标 1 的元素。', '题目要求“排序后第二大”，不是严格的第二不同值，因此有重复最大值时仍输出该值。')

P('5.2', 2, '【逆序输出】输入 n 个整数，按相反顺序输出，用空格分隔。',
  '原创情境 · 数组逆序', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];for(int i=n-1;i>=0;i--){if(i<n-1)cout<<" ";cout<<a[i];}}\n',
  [{'input':'5\n1 2 3 4 5\n','output':'5 4 3 2 1'},{'input':'3\n-1 0 8\n','output':'8 0 -1'},{'input':'1\n7\n','output':'7','hidden':True}],
  '从下标 n-1 循环到 0 输出。', '不需要交换元素，直接逆序访问即可。')

P('5.2', 3, '【循环左移】输入 n 个整数和 k，把数组循环左移 k 位后输出。',
  '原创情境 · 数组旋转', '#include <iostream>\nusing namespace std;\nint main(){int n,k,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];cin>>k;k%=n;for(int i=0;i<n;i++){if(i)cout<<" ";cout<<a[(i+k)%n];}}\n',
  [{'input':'5\n1 2 3 4 5\n2\n','output':'3 4 5 1 2'},{'input':'4\n10 20 30 40\n4\n','output':'10 20 30 40'},{'input':'3\n7 8 9\n1\n','output':'8 9 7','hidden':True}],
  '左移 k 位后，新数组第 i 个元素来自原数组 (i+k)%n。', '先 k %= n 处理 k 大于等于 n 的情况；循环取模实现环形访问。')

P('5.2', 2, '【升序排列】输入 n 个整数，用冒泡排序按从小到大输出。',
  '原创情境 · 冒泡排序', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];for(int i=0;i<n-1;i++)for(int j=0;j<n-1-i;j++)if(a[j]>a[j+1]){int t=a[j];a[j]=a[j+1];a[j+1]=t;}for(int i=0;i<n;i++){if(i)cout<<" ";cout<<a[i];}}\n',
  [{'input':'5\n5 1 4 2 3\n','output':'1 2 3 4 5'},{'input':'3\n3 2 1\n','output':'1 2 3'},{'input':'1\n9\n','output':'9','hidden':True}],
  '相邻逆序则交换，经过多轮后数组升序。', '外层轮数和内层比较边界要配合，避免访问越界。')

P('5.2', 2, '【出现次数】输入 n 个整数和一个目标值 x，统计 x 在数组中出现的次数。',
  '原创情境 · 频次统计', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000],x,c=0;cin>>n;for(int i=0;i<n;i++)cin>>a[i];cin>>x;for(int i=0;i<n;i++)if(a[i]==x)c++;cout<<c;}\n',
  [{'input':'4\n1 2 2 3\n2\n','output':'2'},{'input':'3\n1 2 3\n9\n','output':'0'},{'input':'5\n7 7 7 7 7\n7\n','output':'5','hidden':True}],
  '遍历数组，遇到等于 x 的元素就累加。', '目标值可能不存在，计数器初值为 0 即可。')

P('5.2', 3, '【不同数字】输入 n 个整数，统计其中不同数值的个数。',
  '原创情境 · 去重统计', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000],c=0;cin>>n;for(int i=0;i<n;i++)cin>>a[i];for(int i=0;i<n;i++){bool seen=false;for(int j=0;j<i;j++)if(a[j]==a[i]){seen=true;break;}if(!seen)c++;}cout<<c;}\n',
  [{'input':'5\n1 2 2 3 1\n','output':'3'},{'input':'4\n-1 0 -1 0\n','output':'2'},{'input':'3\n5 5 5\n','output':'1','hidden':True}],
  '对每个元素检查它前面是否已经出现过。', '第一次出现的元素计数；时间复杂度 O(n²)，但输入规模较小时足够。')

P('5.4', 2, '【矩阵行和】输入 n 行 m 列的整数矩阵，输出每一行元素之和，每行一个。',
  '原创情境 · 矩阵行统计', '#include <iostream>\nusing namespace std;\nint main(){int n,m,a[50][50];cin>>n>>m;for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>a[i][j];for(int i=0;i<n;i++){int s=0;for(int j=0;j<m;j++)s+=a[i][j];cout<<s<<"\\n";}}\n',
  [{'input':'2 3\n1 2 3\n4 5 6\n','output':'6\n15'},{'input':'1 2\n-1 1\n','output':'0'},{'input':'3 1\n2\n4\n6\n','output':'2\n4\n6','hidden':True}],
  '外层枚举行，内层枚举列并累加。', '这是二维数组按行遍历的基本操作。', extra='')

P('5.4', 2, '【矩阵最大值】输入 n 行 m 列整数矩阵，输出矩阵中的最大值。',
  '原创情境 · 矩阵极值', '#include <iostream>\nusing namespace std;\nint main(){int n,m,a[50][50];cin>>n>>m;for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>a[i][j];int mx=a[0][0];for(int i=0;i<n;i++)for(int j=0;j<m;j++)if(a[i][j]>mx)mx=a[i][j];cout<<mx;}\n',
  [{'input':'2 3\n1 2 3\n4 5 6\n','output':'6'},{'input':'2 2\n-5 -1\n-3 -2\n','output':'-1'},{'input':'1 1\n8\n','output':'8','hidden':True}],
  '最大值初值取 a[0][0]，遍历全部元素更新。', '初值不能取 0，否则全负数矩阵会出错。')

# ============ 字符数组与字符串 ============
P('5.3', 1, '【字符串长度】输入一个不含空格的字符串，输出它的长度（不要使用 strlen）。',
  '原创情境 · 字符串长度', '#include <iostream>\nusing namespace std;\nint main(){char s[500];cin>>s;int n=0;while(s[n]!=0)n++;cout<<n;}\n',
  [{'input':'hello\n','output':'5'},{'input':'C++\n','output':'3'},{'input':'a\n','output':'1','hidden':True}],
  '从下标 0 开始，遇到 0 结束标记停止。', 'C 风格字符串以编码为 0 的字符结尾，可以直接写成 s[i] != 0。')

P('5.3', 2, '【元音统计】输入一个不含空格的英文字符串，统计其中元音字母 a、e、i、o、u（不区分大小写）的个数。',
  '原创情境 · 元音统计', '#include <iostream>\n#include <cctype>\nusing namespace std;\nint main(){char s[500];cin>>s;int c=0;for(int i=0;s[i]!=0;i++){char x=tolower(s[i]);if(x==\'a\'||x==\'e\'||x==\'i\'||x==\'o\'||x==\'u\')c++;}cout<<c;}\n',
  [{'input':'education\n','output':'5'},{'input':'AEIOU\n','output':'5'},{'input':'xyz\n','output':'0','hidden':True}],
  '遍历字符，转小写后与五个元音比较。', '使用 ctype 的 tolower 统一大小写，避免写两套判断。', extra='#include <cctype>')

P('5.3', 2, '【字符类型统计】输入一个不含空格的字符串，分别输出大写字母、小写字母、数字字符的个数，用空格分隔。',
  '原创情境 · 字符分类', '#include <iostream>\n#include <cctype>\nusing namespace std;\nint main(){char s[500];cin>>s;int u=0,l=0,d=0;for(int i=0;s[i]!=0;i++){if(isupper((unsigned char)s[i]))u++;else if(islower((unsigned char)s[i]))l++;else if(isdigit((unsigned char)s[i]))d++;}cout<<u<<" "<<l<<" "<<d;}\n',
  [{'input':'Ab3X\n','output':'2 1 1'},{'input':'abc123\n','output':'0 3 3'},{'input':'XYZ\n','output':'3 0 0','hidden':True}],
  '遍历字符，用 isupper、islower、isdigit 分类。', '三个计数器互斥累加；数字和大小写字母分别判断。', extra='#include <cctype>')

P('5.3', 2, '【字符串倒序】输入一个不含空格的字符串，输出逆序后的字符串。',
  '原创情境 · 字符串倒序', '#include <iostream>\nusing namespace std;\nint main(){char s[500];cin>>s;int n=0;while(s[n]!=0)n++;for(int i=n-1;i>=0;i--)cout<<s[i];}\n',
  [{'input':'abcde\n','output':'edcba'},{'input':'C++\n','output':'++C'},{'input':'a\n','output':'a','hidden':True}],
  '先求长度，再从最后一个字符倒着输出。', '也可以双指针交换；这里倒序输出更直接。')

P('5.3', 2, '【回文判断】输入一个不含空格的英文字符串，判断是否为回文串。是输出 YES，否则输出 NO。',
  '原创情境 · 回文串', '#include <iostream>\nusing namespace std;\nint main(){char s[500];cin>>s;int n=0;while(s[n]!=0)n++;bool ok=true;for(int i=0,j=n-1;i<j;i++,j--)if(s[i]!=s[j]){ok=false;break;}cout<<(ok?"YES":"NO");}\n',
  [{'input':'level\n','output':'YES'},{'input':'abc\n','output':'NO'},{'input':'abba\n','output':'YES','hidden':True}],
  '用首尾双指针向中间比较。', '发现任意一对字符不同就立即判定 NO，否则到中间仍相同则为回文。')

P('5.3', 2, '【查找字符】输入一个字符串和一个字符，输出该字符第一次出现的下标；不存在输出 -1。',
  '原创情境 · 字符查找', '#include <iostream>\nusing namespace std;\nint main(){char s[500],c;cin>>s>>c;for(int i=0;s[i]!=0;i++)if(s[i]==c){cout<<i;return 0;}cout<<-1;}\n',
  [{'input':'banana\na\n','output':'1'},{'input':'hello\nz\n','output':'-1'},{'input':'abc\na\n','output':'0','hidden':True}],
  '遍历字符串，找到相同字符就输出下标并结束。', '第一次出现即可返回；循环结束仍没找到则输出 -1。')

P('5.3', 2, '【删除字符】输入一个不含空格的字符串和一个字符，删除字符串中所有该字符并输出。',
  '原创情境 · 删除字符', '#include <iostream>\nusing namespace std;\nint main(){char s[500],c;cin>>s>>c;int k=0;for(int i=0;s[i]!=0;i++)if(s[i]!=c)s[k++]=s[i];s[k]=0;cout<<s;}\n',
  [{'input':'banana\na\n','output':'bnn'},{'input':'hello\nl\n','output':'heo'},{'input':'abc\nz\n','output':'abc','hidden':True}],
  '用读写双指针原地保留不需要删除的字符。', '写指针 k 结束时要在新串末尾补 0。')

P('5.3', 3, '【单词计数】输入一行只含字母和空格的文本，统计单词个数，连续多个空格视为一个分隔。',
  '原创情境 · 单词计数', '#include <iostream>\nusing namespace std;\nint main(){char s[500];cin.getline(s,500);int c=0;bool in=false;for(int i=0;s[i]!=0;i++){if(s[i]!=\' \'&&!in){c++;in=true;}else if(s[i]==\' \')in=false;}cout<<c;}\n',
  [{'input':'hello world\n','output':'2'},{'input':'one   two  three\n','output':'3'},{'input':'abc\n','output':'1'},{'input':'a b c d\n','output':'4','hidden':True}],
  '用 in 标记当前是否在单词内部。', '从空格进入非空格时单词数加一；连续空格不会重复计数。')

P('5.3', 3, '【首字母大写】输入一行英文文本，把每个单词的首字母改成大写，其他字符保持不变。单词之间可能有多个空格。',
  '原创情境 · 标题格式', '#include <iostream>\n#include <cctype>\nusing namespace std;\nint main(){char s[500];cin.getline(s,500);bool start=true;for(int i=0;s[i]!=0;i++){if(s[i]==\' \'){start=true;}else{if(start&&s[i]>=\'a\'&&s[i]<=\'z\')s[i]=s[i]-\'a\'+\'A\';start=false;}}cout<<s;}\n',
  [{'input':'hello world\n','output':'Hello World'},{'input':'  c++  lab\n','output':'  C++  Lab'},{'input':'already UP\n','output':'Already UP','hidden':True}],
  '用 start 标记下一个非空格字符是否为单词首字母。', '遇到空格把 start 置真，遇到非空格按需转大写后把 start 置假。')

P('5.3', 3, '【子串出现次数】输入主串和子串（均不含空格），统计子串在主串中出现的次数，允许重叠。',
  '原创情境 · 文本匹配', '#include <iostream>\nusing namespace std;\nint main(){char s[500],p[100];cin>>s>>p;int n=0,m=0,c=0;while(s[n]!=0)n++;while(p[m]!=0)m++;for(int i=0;i+m<=n;i++){int j=0;while(j<m&&s[i+j]==p[j])j++;if(j==m)c++;}cout<<c;}\n',
  [{'input':'aaaa\naa\n','output':'3'},{'input':'ababa\naba\n','output':'2'},{'input':'abc\nxyz\n','output':'0','hidden':True}],
  '枚举每个起点，逐字符比较子串。', '允许重叠意味着找到一次后起点只前进 1，而不是跳过整个子串。')

P('5.3', 3, '【最长单词】输入一行英文文本，输出其中最长的单词；长度相同时输出最先出现的单词。',
  '原创情境 · 最长单词', '#include <iostream>\nusing namespace std;\nint main(){char s[500],best[500],cur[500];cin.getline(s,500);int bn=0,cn=0;for(int i=0;;i++){if(s[i]!=\' \'&&s[i]!=0){cur[cn++]=s[i];}else{cur[cn]=0;if(cn>bn){bn=cn;for(int j=0;j<=cn;j++)best[j]=cur[j];}if(s[i]==0)break;cn=0;}}cout<<best;}\n',
  [{'input':'I love programming\n','output':'programming'},{'input':'aa bbb cc\n','output':'bbb'},{'input':'one two\n','output':'one','hidden':True}],
  '扫描每个单词，记录当前单词和当前最长单词。', '遇到空格或字符串结束时结算当前单词；只有严格更长才替换，保证并列时保留最早出现的单词。')

P('5.3', 3, '【数字字符串转整数】输入一个只含数字字符的字符串，把它转成整数输出，不使用标准库转换函数。',
  '原创情境 · 字符串转整数', '#include <iostream>\nusing namespace std;\nint main(){char s[100];cin>>s;long long n=0;for(int i=0;s[i]!=0;i++)n=n*10+(s[i]-\'0\');cout<<n;}\n',
  [{'input':'00123\n','output':'123'},{'input':'0\n','output':'0'},{'input':'987654321\n','output':'987654321','hidden':True}],
  '从高位到低位累加：n = n*10 + digit。', '字符 s[i] 减去字符 0 的编码得到数值；前导 0 经过数值累加会自然消失。')

# ============ 函数、递归与算法综合 ============
P('4.4', 2, '【递归求和】编写递归函数 sumTo(n)，返回 1+2+…+n，并输出结果（n≥1）。',
  '原创情境 · 递归求和', '#include <iostream>\nusing namespace std;\nint sumTo(int n){if(n==1)return 1;return n+sumTo(n-1);}\nint main(){int n;cin>>n;cout<<sumTo(n);}\n',
  [{'input':'5\n','output':'15'},{'input':'1\n','output':'1'},{'input':'100\n','output':'5050','hidden':True}],
  '结束条件 n==1，递归式 n+sumTo(n-1)。', '递归把大问题化小；sumTo(100) 仍在 int 范围内。', starter_body='#include <iostream>\nusing namespace std;\n\nint sumTo(int n) {\n    // 结束条件与递归式\n}\n\nint main() {\n    int n;\n    cin >> n;\n    cout << sumTo(n);\n    return 0;\n}\n')

P('4.4', 2, '【递归 Fibonacci】编写递归函数 fib(n)，输出第 n 个 Fibonacci 数（F1=F2=1）。',
  '原创情境 · 递归数列', '#include <iostream>\nusing namespace std;\nint fib(int n){if(n<=2)return 1;return fib(n-1)+fib(n-2);}\nint main(){int n;cin>>n;cout<<fib(n);}\n',
  [{'input':'1\n','output':'1'},{'input':'6\n','output':'8'},{'input':'10\n','output':'55','hidden':True}],
  '结束条件 n≤2 返回 1。', '递归实现直观但会重复计算；题目数据范围较小。')

P('4.4', 2, '【递归最大公约数】编写递归函数 gcd(a,b)，用欧几里得算法求最大公约数。',
  '原创情境 · 递归 gcd', '#include <iostream>\nusing namespace std;\nint gcd(int a,int b){return b==0?a:gcd(b,a%b);}\nint main(){int a,b;cin>>a>>b;cout<<gcd(a,b);}\n',
  [{'input':'12 18\n','output':'6'},{'input':'7 13\n','output':'1'},{'input':'100 25\n','output':'25','hidden':True}],
  '结束条件 b==0，此时 a 就是 gcd。', '递归式 gcd(a,b)=gcd(b,a%b)，每次规模缩小。')

P('4.4', 2, '【递归数位和】编写递归函数 digitSum(n)，求非负整数 n 的各位数字之和。',
  '原创情境 · 递归数位和', '#include <iostream>\nusing namespace std;\nint digitSum(int n){if(n<10)return n;return n%10+digitSum(n/10);}\nint main(){int n;cin>>n;cout<<digitSum(n);}\n',
  [{'input':'1234\n','output':'10'},{'input':'0\n','output':'0'},{'input':'999\n','output':'27','hidden':True}],
  '结束条件 n<10，递归式 n%10 + digitSum(n/10)。', '每次取个位并把 n 除以 10，直到只剩一位。')

P('4.4', 2, '【递归数组最大值】编写递归函数 maxInArray(a, left, right)，返回数组区间最大值。输入 n 和数组，输出最大值。',
  '原创情境 · 递归最大值', '#include <iostream>\nusing namespace std;\nint maxInArray(int a[],int l,int r){if(l==r)return a[l];int m=maxInArray(a,l+1,r);return a[l]>m?a[l]:m;}\nint main(){int n,a[1000];cin>>n;for(int i=0;i<n;i++)cin>>a[i];cout<<maxInArray(a,0,n-1);}\n',
  [{'input':'5\n1 9 2 7 3\n','output':'9'},{'input':'1\n-5\n','output':'-5'},{'input':'4\n-2 -9 -1 -7\n','output':'-1','hidden':True}],
  '区间只剩一个元素时返回它，否则比较首元素和剩余区间的最大值。', '递归处理的数组区间不断缩短，结束条件是 l==r。')

P('5.3', 3, '【递归回文】编写递归函数 isPal(s,left,right)，判断字符串是否为回文。是输出 YES，否则 NO。',
  '原创情境 · 递归回文', '#include <iostream>\nusing namespace std;\nbool isPal(char s[],int l,int r){if(l>=r)return true;if(s[l]!=s[r])return false;return isPal(s,l+1,r-1);}\nint main(){char s[500];cin>>s;int n=0;while(s[n]!=0)n++;cout<<(isPal(s,0,n-1)?"YES":"NO");}\n',
  [{'input':'level\n','output':'YES'},{'input':'abc\n','output':'NO'},{'input':'abba\n','output':'YES','hidden':True}],
  '结束条件 left>=right（空串或单字符）。', '首尾相同则递归检查内层，否则直接返回 false。')

P('4.4', 3, '【汉诺塔步数】输入圆盘数 n，输出按经典递归策略完成汉诺塔所需的最少移动次数。',
  '原创情境 · 汉诺塔计数', '#include <iostream>\nusing namespace std;\nlong long moves(int n){if(n==0)return 0;return 2*moves(n-1)+1;}\nint main(){int n;cin>>n;cout<<moves(n);}\n',
  [{'input':'1\n','output':'1'},{'input':'3\n','output':'7'},{'input':'10\n','output':'1023','hidden':True}],
  '递归式 moves(n)=2*moves(n-1)+1。', '汉诺塔最少移动次数为 2ⁿ−1，n 大时使用 long long。')

P('4.4', 4, '【全排列】输入 n（1≤n≤6），按字典序输出 1～n 的所有全排列，每行一个排列。',
  '原创情境 · 回溯入门', '#include <iostream>\nusing namespace std;\nint n,a[10],used[10];\nvoid dfs(int k){if(k==n){for(int i=0;i<n;i++)cout<<a[i];cout<<"\\n";return;}for(int i=1;i<=n;i++)if(!used[i]){used[i]=1;a[k]=i;dfs(k+1);used[i]=0;}}\nint main(){cin>>n;dfs(0);}\n',
  [{'input':'2\n','output':'12\n21'},{'input':'1\n','output':'1'},{'input':'3\n','output':'123\n132\n213\n231\n312\n321','hidden':True}],
  '用 used 数组标记数字是否已经使用。', '每个位置按 1～n 尝试，递归填满 n 位后输出；回溯时撤销标记。', starter_body='#include <iostream>\nusing namespace std;\nint n, a[10], used[10];\nvoid dfs(int k) {\n    // 回溯搜索\n}\nint main() { cin >> n; dfs(0); return 0; }\n')

# ============ 二维数组与综合算法 ============
P('5.4', 3, '【对称矩阵】输入一个 n×n 整数矩阵，判断它是否关于主对角线对称。是输出 YES，否则输出 NO。',
  '原创情境 · 对称矩阵', '#include <iostream>\nusing namespace std;\nint main(){int n,a[50][50];cin>>n;for(int i=0;i<n;i++)for(int j=0;j<n;j++)cin>>a[i][j];bool ok=true;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(a[i][j]!=a[j][i])ok=false;cout<<(ok?"YES":"NO");}\n',
  [{'input':'3\n1 2 3\n2 4 5\n3 5 6\n','output':'YES'},{'input':'2\n1 2\n3 4\n','output':'NO'},{'input':'1\n7\n','output':'YES','hidden':True}],
  '只需检查主对角线右上与左下对称位置。', '遍历 i<j，比较 a[i][j] 与 a[j][i]；不一致即可判定不对称。')

P('5.4', 4, '【矩阵乘法】输入矩阵 A 的行数 n、列数 m，矩阵 B 的列数 p，再输入 A（n×m）和 B（m×p），输出 A×B。',
  '原创情境 · 矩阵乘法', '#include <iostream>\nusing namespace std;\nint main(){int n,m,p,a[30][30],b[30][30],c[30][30]={};cin>>n>>m>>p;for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>a[i][j];for(int i=0;i<m;i++)for(int j=0;j<p;j++)cin>>b[i][j];for(int i=0;i<n;i++)for(int j=0;j<p;j++)for(int k=0;k<m;k++)c[i][j]+=a[i][k]*b[k][j];for(int i=0;i<n;i++){for(int j=0;j<p;j++){if(j)cout<<" ";cout<<c[i][j];}cout<<"\\n";}}\n',
  [{'input':'2 2 2\n1 2\n3 4\n5 6\n7 8\n','output':'19 22\n43 50'},{'input':'1 2 1\n1 2\n3\n4\n','output':'11'},{'input':'1 1 1\n5\n6\n','output':'30','hidden':True}],
  '结果 C 的 (i,j) = A 第 i 行与 B 第 j 列对应乘积之和。', '三层循环分别枚举行、列和公共维度 m；初始化 C 为 0。')

P('5.4', 2, '【每行最大值】输入 n 行 m 列矩阵，输出每一行的最大值，每行一个。',
  '原创情境 · 行最大值', '#include <iostream>\nusing namespace std;\nint main(){int n,m,a[50][50];cin>>n>>m;for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>a[i][j];for(int i=0;i<n;i++){int mx=a[i][0];for(int j=1;j<m;j++)if(a[i][j]>mx)mx=a[i][j];cout<<mx<<"\\n";}}\n',
  [{'input':'2 3\n1 2 3\n4 5 6\n','output':'3\n6'},{'input':'2 2\n-5 -1\n-3 -2\n','output':'-1\n-2'},{'input':'3 1\n2\n9\n4\n','output':'2\n9\n4','hidden':True}],
  '对每一行把首元素作为最大值，再扫描该行更新。', '二维数组按行访问；最大值初值取本行首元素，处理全负数行。')

P('5.4', 4, '【螺旋输出】输入一个 n×n 矩阵，按顺时针螺旋顺序输出所有元素。',
  '原创情境 · 螺旋矩阵', '#include <iostream>\nusing namespace std;\nint main(){int n,a[50][50];cin>>n;for(int i=0;i<n;i++)for(int j=0;j<n;j++)cin>>a[i][j];int top=0,bottom=n-1,left=0,right=n-1;bool first=true;while(top<=bottom&&left<=right){for(int j=left;j<=right;j++){if(!first)cout<<" ";cout<<a[top][j];first=false;}top++;for(int i=top;i<=bottom;i++){if(!first)cout<<" ";cout<<a[i][right];first=false;}right--;if(top<=bottom){for(int j=right;j>=left;j--){if(!first)cout<<" ";cout<<a[bottom][j];first=false;}bottom--;}if(left<=right){for(int i=bottom;i>=top;i--){if(!first)cout<<" ";cout<<a[i][left];first=false;}left++;}}}\n',
  [{'input':'3\n1 2 3\n4 5 6\n7 8 9\n','output':'1 2 3 6 9 8 7 4 5'},{'input':'1\n7\n','output':'7'},{'input':'2\n1 2\n3 4\n','output':'1 2 4 3','hidden':True}],
  '维护上、下、左、右四个边界，按右、下、左、上循环收缩。', '每进入一个方向都检查是否越界；用 first 控制元素间空格。')

P('3.3', 3, '【质因数分解】输入大于 1 的正整数 n，按因数从小到大输出质因数分解，格式如 60 = 2^2 * 3^1 * 5^1。',
  '原创情境 · 质因数分解', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;cout<<n<<"=";bool first=true;for(int p=2;p*p<=n;p++){int c=0;while(n%p==0){n/=p;c++;}if(c){if(!first)cout<<"*";cout<<p<<"^"<<c;first=false;}}if(n>1){if(!first)cout<<"*";cout<<n<<"^1";}}\n',
  [{'input':'60\n','output':'60=2^2*3^1*5^1'},{'input':'13\n','output':'13=13^1'},{'input':'100\n','output':'100=2^2*5^2','hidden':True}],
  '从 2 开始试除，统计每个质因数的指数。', '循环结束后若 n>1，它本身也是质因数；注意星号和指数的输出格式。')

P('3.3', 4, '【约瑟夫环】n 个小孩围成一圈，编号 0～n-1，从 0 开始报数，报到 m 的人离开，再从下一个人继续。输出最后留下的编号。',
  '原创情境 · 约瑟夫环', '#include <iostream>\nusing namespace std;\nint main(){int n,m,a[1000];cin>>n>>m;for(int i=0;i<n;i++)a[i]=1;int idx=0,left=n;while(left>1){int c=0;while(c<m){if(a[idx])c++;if(c==m)break;idx=(idx+1)%n;}a[idx]=0;left--;do{idx=(idx+1)%n;}while(left>0&&!a[idx]);}cout<<idx;}\n',
  [{'input':'5 3\n','output':'3'},{'input':'6 2\n','output':'4'},{'input':'10 5\n','output':'2','hidden':True}],
  '用数组标记圈内小孩，按报数跳过已离开的人。', '报数到 m 时把当前位置标记离开，再从下一个仍在圈内的人继续；注意人数的变化。')

P('3.3', 4, '【最长递增子序列】输入 n 个整数，输出最长严格递增子序列的长度。',
  '原创情境 · 最长递增子序列', '#include <iostream>\nusing namespace std;\nint main(){int n,a[1000],dp[1000],ans=0;cin>>n;for(int i=0;i<n;i++){cin>>a[i];dp[i]=1;for(int j=0;j<i;j++)if(a[j]<a[i]&&dp[j]+1>dp[i])dp[i]=dp[j]+1;if(dp[i]>ans)ans=dp[i];}cout<<ans;}\n',
  [{'input':'8\n10 9 2 5 3 7 101 18\n','output':'4'},{'input':'5\n1 2 3 4 5\n','output':'5'},{'input':'5\n5 4 3 2 1\n','output':'1','hidden':True}],
  'dp[i] 表示以 a[i] 结尾的最长递增子序列长度。', '对每个 i 枚举前面的 j，若 a[j]<a[i] 则可以接上；时间复杂度 O(n²)。')

P('3.3', 4, '【0-1 背包】输入物品数 n、背包容量 W，以及 n 组重量和价值，求不超过容量的最大总价值。',
  '原创情境 · 背包选择', '#include <iostream>\nusing namespace std;\nint main(){int n,W,w[100],v[100],dp[1000]={};cin>>n>>W;for(int i=0;i<n;i++)cin>>w[i]>>v[i];for(int i=0;i<n;i++)for(int c=W;c>=w[i];c--)if(dp[c-w[i]]+v[i]>dp[c])dp[c]=dp[c-w[i]]+v[i];cout<<dp[W];}\n',
  [{'input':'3 5\n2 3\n3 4\n4 5\n','output':'7'},{'input':'1 10\n5 9\n','output':'9'},{'input':'3 4\n2 3\n3 4\n4 5\n','output':'5','hidden':True}],
  'dp[c] 表示容量 c 下能达到的最大价值，容量必须倒序遍历。', '每件物品只能选一次，所以内层容量从 W 倒着更新，避免重复使用当前物品。')

P('5.3', 4, '【大整数加法】输入两个非负十进制整数（可超过 long long 范围），输出它们的和。',
  '原创情境 · 高精度加法', '#include <iostream>\nusing namespace std;\nint main(){char a[1000],b[1000];int x[1000]={},y[1000]={},z[1001]={};cin>>a>>b;int n=0,m=0;while(a[n]!=0)n++;while(b[m]!=0)m++;for(int i=0;i<n;i++)x[i]=a[n-1-i]-\'0\';for(int i=0;i<m;i++)y[i]=b[m-1-i]-\'0\';int len=n>m?n:m;for(int i=0;i<len;i++){z[i]+=x[i]+y[i];z[i+1]=z[i]/10;z[i]%=10;}if(z[len])cout<<z[len];for(int i=len-1;i>=0;i--)cout<<z[i];}\n',
  [{'input':'999 1\n','output':'1000'},{'input':'123 456\n','output':'579'},{'input':'12345678901234567890 987654321\n','output':'12345678902222222211','hidden':True}],
  '把两个数按低位到高位存入数组，逐位相加并处理进位。', '字符串长度可超过 19 位；结果最高位可能有额外进位，需要单独输出。')

# ============ 结构体、引用、指针与链表 ============
P('5.5', 2, '【两点距离】输入两个点的坐标 (x1,y1)、(x2,y2)，输出两点间距离，保留 2 位小数。',
  '原创情境 · 坐标距离', '#include <iostream>\n#include <iomanip>\n#include <cmath>\nusing namespace std;\nstruct Point{int x,y;};\nint main(){Point a,b;cin>>a.x>>a.y>>b.x>>b.y;double d=sqrt((double)(a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));cout<<fixed<<setprecision(2)<<d;}\n',
  [{'input':'0 0 3 4\n','output':'5.00'},{'input':'1 1 4 5\n','output':'5.00'},{'input':'2 3 2 3\n','output':'0.00','hidden':True}],
  '距离公式：√((x1−x2)²+(y1−y2)²)。', '用 struct 保存点坐标，sqrt 计算平方根，fixed 固定两位小数。', extra='#include <iomanip>\n#include <cmath>')

P('5.5', 2, '【最高分姓名】输入 n 个学生的姓名和成绩，输出成绩最高者的姓名；成绩相同输出最先出现者。',
  '原创情境 · 学生成绩', '#include <iostream>\nusing namespace std;\nstruct Student{char name[30];int score;};\nint main(){int n;cin>>n;Student a[100];for(int i=0;i<n;i++)cin>>a[i].name>>a[i].score;int best=0;for(int i=1;i<n;i++)if(a[i].score>a[best].score)best=i;cout<<a[best].name;}\n',
  [{'input':'3\nLi 80\nWang 95\nZhao 70\n','output':'Wang'},{'input':'2\nA 90\nB 90\n','output':'A'},{'input':'1\nSolo 100\n','output':'Solo','hidden':True}],
  '用结构体数组保存姓名和成绩，记录最高分下标。', '只有严格更高才更新，因此并列时保留最早出现的学生。')

P('5.5', 3, '【图书价格排序】输入 n 本书的书名和价格，按价格从低到高输出书名，每行一个；价格相同按输入顺序。',
  '原创情境 · 书架整理', '#include <iostream>\nusing namespace std;\nstruct Book{char name[40];double price;};\nint main(){int n;cin>>n;Book a[100];for(int i=0;i<n;i++)cin>>a[i].name>>a[i].price;for(int i=0;i<n-1;i++)for(int j=i+1;j<n;j++)if(a[j].price<a[i].price){Book t=a[i];a[i]=a[j];a[j]=t;}for(int i=0;i<n;i++)cout<<a[i].name<<"\\n";}\n',
  [{'input':'3\nC++ 59.8\nMath 30.5\nArt 45\n','output':'Math\nArt\nC++'},{'input':'2\nA 10\nB 10\n','output':'A\nB'},{'input':'1\nSolo 99\n','output':'Solo','hidden':True}],
  '结构体整体赋值可交换两个学生记录。', '选择排序在价格相同时不交换，因此相价书保持原输入顺序。')

P('5.5', 2, '【日期先后】输入两个日期（年、月、日），按 YYYY-MM-DD 输出较早的日期。',
  '原创情境 · 日期比较', '#include <iostream>\nusing namespace std;\nstruct Date{int y,m,d;};\nint main(){Date a,b;cin>>a.y>>a.m>>a.d>>b.y>>b.m>>b.d;bool aFirst=(a.y<b.y)||(a.y==b.y&&a.m<b.m)||(a.y==b.y&&a.m==b.m&&a.d<=b.d);Date e=aFirst?a:b;cout<<e.y<<"-"<<e.m<<"-"<<e.d;}\n',
  [{'input':'2024 5 1 2023 12 31\n','output':'2023-12-31'},{'input':'2024 1 1 2024 1 1\n','output':'2024-1-1'},{'input':'2023 8 9 2024 2 1\n','output':'2023-8-9','hidden':True}],
  '依次比较年、月、日；可以先构造一个布尔变量表示第一个日期是否更早。', '日期相同也输出第一个；结构体可整体赋值。')

P('5.7', 2, '【指针交换】输入两个整数，用指针参数编写 swap 函数交换它们，输出交换后的两个数。',
  '原创情境 · 指针交换', '#include <iostream>\nusing namespace std;\nvoid swp(int* a,int* b){int t=*a;*a=*b;*b=t;}\nint main(){int a,b;cin>>a>>b;swp(&a,&b);cout<<a<<" "<<b;}\n',
  [{'input':'1 2\n','output':'2 1'},{'input':'-5 8\n','output':'8 -5'},{'input':'0 0\n','output':'0 0','hidden':True}],
  '函数参数用 int*，调用时传 &a、&b。', '通过指针间接访问并交换两个变量的值，实参也会被修改。')

P('5.8', 3, '【动态数组逆序】输入 n，用 new int[n] 创建动态数组，读入 n 个数后逆序输出，最后释放数组。',
  '原创情境 · 动态数组', '#include <iostream>\nusing namespace std;\nint main(){int n;cin>>n;int* a=new int[n];for(int i=0;i<n;i++)cin>>a[i];for(int i=n-1;i>=0;i--){if(i<n-1)cout<<" ";cout<<a[i];}delete[] a;}\n',
  [{'input':'5\n1 2 3 4 5\n','output':'5 4 3 2 1'},{'input':'1\n7\n','output':'7'},{'input':'3\n-1 0 8\n','output':'8 0 -1','hidden':True}],
  'new int[n] 分配动态数组，倒序下标输出，最后 delete[]。', '申请与释放必须配对；数组动态空间在程序运行期间由 new 分配。')

P('5.8', 3, '【链表结点数】输入 n 个整数，用头插法建立单链表，输出链表中结点的个数，最后释放链表。',
  '原创情境 · 链表长度', '#include <iostream>\nusing namespace std;\nstruct Node{int v;Node* next;};\nint main(){int n;cin>>n;Node* head=nullptr;for(int i=0;i<n;i++){int x;cin>>x;Node* p=new Node;p->v=x;p->next=head;head=p;}int c=0;for(Node* p=head;p!=nullptr;p=p->next)c++;cout<<c;while(head){Node* p=head;head=head->next;delete p;}}\n',
  [{'input':'5\n1 2 3 4 5\n','output':'5'},{'input':'1\n9\n','output':'1'},{'input':'0\n','output':'0','hidden':True}],
  '头插法建立链表后遍历计数，最后逐个 delete。', 'n=0 时 head 为空，输出 0；遍历链表要沿 next 指针前进。')

P('5.9', 1, '【引用加十】编写函数 void addTen(int& x)，把参数值加 10。输入一个整数，输出调用后的值。',
  '原创情境 · 引用参数', '#include <iostream>\nusing namespace std;\nvoid addTen(int& x){x+=10;}\nint main(){int a;cin>>a;addTen(a);cout<<a;}\n',
  [{'input':'5\n','output':'15'},{'input':'-10\n','output':'0'},{'input':'0\n','output':'10','hidden':True}],
  '形参写成 int& x，调用时直接传变量名。', '引用是实参的别名，函数内修改 x 就是修改 main 中的 a。')

P('4.5', 2, '【默认参数平方】编写函数 long long power(int base, int exp = 2)。只输入一个整数 base，调用 power(base) 输出它的平方。',
  '原创情境 · 默认参数', '#include <iostream>\nusing namespace std;\nlong long power(int base,int exp=2){long long r=1;for(int i=0;i<exp;i++)r*=base;return r;}\nint main(){int a;cin>>a;cout<<power(a);}\n',
  [{'input':'5\n','output':'25'},{'input':'-3\n','output':'9'},{'input':'0\n','output':'0','hidden':True}],
  '函数第二个参数默认值为 2，调用 power(a) 表示 a²。', '默认参数写在函数声明或定义中；调用时省略的实参从右端开始使用默认值。')

P('5.1', 2, '【订单状态】定义枚举 Status {CREATED, PAID, SHIPPED, DONE}。输入 0～3，输出状态名 CREATED、PAID、SHIPPED 或 DONE。',
  '原创情境 · 订单状态', '#include <iostream>\nusing namespace std;\nenum Status{CREATED,PAID,SHIPPED,DONE};\nint main(){int x;cin>>x;Status s=(Status)x;switch(s){case CREATED:cout<<"CREATED";break;case PAID:cout<<"PAID";break;case SHIPPED:cout<<"SHIPPED";break;default:cout<<"DONE";}}\n',
  [{'input':'0\n','output':'CREATED'},{'input':'1\n','output':'PAID'},{'input':'3\n','output':'DONE'},{'input':'2\n','output':'SHIPPED','hidden':True}],
  '把整数显式转换为枚举类型，再用 switch 分派。', '枚举值默认从 0 开始连续递增，switch 的 case 使用枚举常量。')

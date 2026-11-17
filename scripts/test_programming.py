#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用本机 g++ 实际编译运行全部编程题标准解，校验测试用例。"""
import json, os, subprocess, tempfile, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def norm(s):
    return '\n'.join(line.rstrip() for line in s.replace('\r\n','\n').rstrip().split('\n'))

def main():
    qs=[]
    for f in sorted(os.listdir(os.path.join(ROOT,'data','questions'))):
        if f.startswith('ch') and f.endswith('.json'):
            qs += json.load(open(os.path.join(ROOT,'data','questions',f),encoding='utf-8'))['questions']
    progs=[q for q in qs if q['type']=='programming']
    bad=0
    with tempfile.TemporaryDirectory() as td:
        exe=os.path.join(td,'a.exe')
        for q in progs:
            cpp=os.path.join(td,q['id']+'.cpp')
            open(cpp,'w',encoding='utf-8').write(q['solution'])
            r=subprocess.run(['g++','-std=c++17','-O2','-o',exe,cpp],capture_output=True,text=True)
            if r.returncode:
                print('COMPILE FAIL',q['id'],r.stderr[:500]);bad+=1;continue
            for i,t in enumerate(q['tests'],1):
                run=subprocess.run([exe],input=t['input'],capture_output=True,text=True,timeout=5)
                if run.returncode!=0 or norm(run.stdout)!=norm(t['output']):
                    print('TEST FAIL',q['id'],'case',i,'rc',run.returncode,'got',repr(run.stdout),'want',repr(t['output']),'err',run.stderr[:200]);bad+=1
    print('编程题:',len(progs),' 失败:',bad)
    sys.exit(1 if bad else 0)

if __name__=='__main__': main()

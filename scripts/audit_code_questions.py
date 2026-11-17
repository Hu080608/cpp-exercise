#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, subprocess, tempfile
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def norm(s): return s.replace('\r\n','\n').strip()
qs=[]
for f in sorted(os.listdir(os.path.join(ROOT,'data','questions'))):
    if f.startswith('ch') and f.endswith('.json'):
        qs+=json.load(open(os.path.join(ROOT,'data','questions',f),encoding='utf-8'))['questions']
with tempfile.TemporaryDirectory() as td:
    exe=os.path.join(td,'a.exe')
    for q in [x for x in qs if x['type']=='code']:
        cpp=os.path.join(td,q['id']+'.cpp');open(cpp,'w',encoding='utf-8').write('\n'.join(q['code']))
        r=subprocess.run(['g++','-std=c++17','-O2','-o',exe,cpp],capture_output=True,text=True)
        if r.returncode:
            print('SKIP(no compile)',q['id'],q['stem'][:35]);continue
        run=subprocess.run([exe],input='',capture_output=True,text=True,timeout=5)
        got=norm(run.stdout)
        opt=norm(str(q['options'][q['answer']]))
        mark='OK' if got==opt else 'CHECK'
        if mark!='OK': print(mark,q['id'],'got=',repr(got),'opt=',repr(opt),'stem=',q['stem'][:60])

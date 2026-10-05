from rdm import rdm
from time import time
from main import main

t = 0 # <- map Type
loop_limit = 1000000

st = 0
ct,SUM_step,SUM_time,MAX_time = 0,0,0,0
def print_case():
    print("[{}] | {},'{}','{}'".format(ct,t,m,leaf))
def print_info():
    if ct:
        AVG_step,AVG_time= SUM_step // ct,SUM_time / ct        
        print('Average Step :',AVG_step)
        print('Average Time : {}s(dart {}m {}s)'.
              format(round(AVG_time,6), int((AVG_time*250)//60), int((AVG_time*250)%60)))
        print('Maximum Time : {}s(dart {}m {}s)'.
              format(round(MAX_time,6), int((MAX_time*250)//60), int((MAX_time*250)%60)))
        print('Maximum step :',st)
    
ctt = 0
st = 0
while 1:
    m,leaf = rdm(t)
    if ctt - ct == -100000:
        ctt = ct
        print(ct)
    ts = time()
    try:
        res = main(t,m,leaf)
    except:
        print('Failed Sorting')
        print_case()
        break
    te = time() - ts
    if te > MAX_time or len(res) > st:
        if te > MAX_time and len(res) > st:
            print("!!Max!!")
        else:
            print(["!!Maxtime!!","!!Maxstep!!"][len(res)>st])
        if te > MAX_time:
            MAX_time = te
        print_case()
        print_info()
        print("{}step, idle {}s(dart {}m {}s)\n".
        format(len(res), round(te,6), int((te*250)//60), int((te*250)%60)))
    SUM_step += len(res)
    if len(res) > st:
        st = len(res)
    SUM_time += te
    ct += 1
    
print_info()
if ct > loop_limit:
    print('COMPLETED.')

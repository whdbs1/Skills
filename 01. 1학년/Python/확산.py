def spr(n):
    A = '000000000'
    A[n] = '1'
    
    for e in range(5):
        for i, value in enumerate(A):
            if value == '1'+str(e):
                for s in arrow1(i):
                    if A[s] == 0:
                        A[s] = 2+e
def spr2(n):
    li = [0]*9
    li[n] = 1

    for e in range(5):        
        for i in range(9):
            if li[i] == 1+e:
                for a in arrow(i):
                    if li[a] == 0:
                        li[a] = 2+e
    return lst(li)

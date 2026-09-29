def aro(x,y,f,n):
    li=[]
    if n-x*f >= 0:
        li.append(n-x*f)
    if n+x*f < x*y*f:
        li.append(n+x*f)
    if n-x > 0:
        li.append(n-x)    
    if n+x < x*y:
        li.append(n+x)
    if n%x != 0:
       li.append(n-1)
    if n%x != x-1:
        li.append(n+1)

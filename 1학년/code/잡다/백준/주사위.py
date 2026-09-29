a,b,c = map(int,input().split())

if a == b == c:
    print( 10000 + a * 1000)
if a == b:
    print( 1000 + a * 100)
elif a == c:
    print( 100 + a * 100)
elif b == c:
    print( 100 + b * 100)
if a != b != c:
    print(max(a,b,c) * 100)
    

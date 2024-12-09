a,b,c = map(int,input().split())

c1 = a == b == c
c2 = a == b
c3 = a == c
c4 = b == c

if c1:
    print(10000 + a * 1000)
elif c2:
    print(1000 + a * 100)
elif c3:
    print(1000 + a * 100)
elif c4:
    print(1000 + b * 100)
else:
    print(100*max(a,b,c))
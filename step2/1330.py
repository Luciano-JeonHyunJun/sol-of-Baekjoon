A, B = map(int, input().split())

a = A > B

b = A < B

if a:
    print('>')
elif b:
    print('<')
else:
    print('==')
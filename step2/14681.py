x = int(input())
y = int(input())

a = x > 0 and y > 0 #1사분면
b = x < 0 and y > 0 #2사분면
c = x < 0 and y < 0 #3사분면
d = x > 0 and y < 0 #4사분면

if a:
    print('1')
elif b:
    print('2')
elif c:
    print('3')
elif d:
    print('4')

#조건문에서는 , 을 사용하면 tuple로 인식
#두 개를 판단해야하는 경우 and,or을 사용한다.

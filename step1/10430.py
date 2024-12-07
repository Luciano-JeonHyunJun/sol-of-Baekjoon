A, B, C = map(int, input().split())  # 바로 정수로 변환
a = A % C
b = B % C

print((A + B) % C)
print((a + b) % C)
print((A * B) % C)
print((a * b) % C)


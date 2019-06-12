# 사칙연산
print(2 * 3)
print(2 / 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3.0)

# //(몫) **(지수승), %(나머지)
print(2 // 3)
print(2 ** 3)
print(2 % 3)


# 몫과 나머지 동시에
result, last = divmod(2, 3)
print(result, last)

t = divmod(2, 3)
print(t, type(t))

# 연산자 우선순위
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)

print(4 / 2 * 2)

# 결합순서 주의!!!
print(2**3**4)
print(2**(3**4))
print((2**3)**4)
# 튜플 생성

t = ()  # 공튜풀
t = (1,)  # 항목이 하나일 때는 반드시 , 찍어줘라
t = (1, 2, 3)
print(t, type(t))

#
# sequence 지원연산
#

# 인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

# 슬라이싱
print(t[1:3])
print(t[::-1])

# 반복
print(t * 2)

# 연결
print(t + (4,))

# 길이
print(len(t))

# 확인
print(4 not in t)

# tuple은 immutable 이다
# t[0] = 100

# 여러개 값의 대입
x, y, z = 10, 20, 30
print(x, y, z)

# swap
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

#
# 객체함수 : immutable이기 때문에 많지 않DA.
#

t = (20, 30, 10, 20)
print(t.index(20))
print(t.count(20))

# 변환
t = (1, 2, 3, 3)
print(t)

# tuple -> set (중복제거)
s = set(t)
print(s, type(s))

# tuple -> list
ll = list(t)
print(ll, type(ll))

# list -> tuple
t = tuple(ll)
print(t, type)

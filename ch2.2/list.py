# 리스트 생성

ll = [1, 2, 'python']

print(ll, type(ll))

# indexing

print(ll[-3], ll[-2], ll[-1], ll[0], ll[1], ll[2])

# slicing
ll2 = ll[1:3]
print(ll2)
print(ll[:])
print(ll[len(ll)::-1])

# 반복
ll2 = ll * 2
print(ll2)

# 연결
ll3 = ll + [3, 4, 5]
print(ll3)

# 길이
print(len(ll3))

# 확인
print(5 in ll3)

# 삭제
del ll3[0]
print(ll3)

# 길이
print(len(ll3))

# 변경 가능한 시퀸스 (mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

# 슬라이싱을 통한 치환
a = [1, 12, 123, 123]
a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

# 슬라이싱을 통한 삭제
a = [1, 12, 123, 123]
a[1:2] = []
print(a)

a[0:] = []
print(a)

# 슬라이싱을 통한 삽입
a = [1, 12, 123, 123]

# 중간삽입
a[1:1] = ['a']
print(a)

# 마지막 삽입
a[5:] = [12345]
print(a)

# 처음
a[:0] = [0]
print(a)

# 여러 개 삽입
a[2:2] = [-12, -1, 0]
print(a)

#
# 객체 함수
#

a = [1, 12, 123, 1234]

# 삽입
a.insert(1, 'a')
print(a)

# 뒤에삽입
a.append(12345)
print(a)

# 앞에삽입
a.insert(0, 0)
print(a)

# reverse
a.reverse()
print(a)

# 제거
a.remove(12)
print(a)

# 확장
a.extend([-1, -2, -3])
print(a)

# 스택으로 사용하기
stack = []
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

# queue로 사용하기
q = [1, 2]
print(q)
q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q)

# sort() : 내장된 소팅 알고리즘
l3 = [1, 5, 2, 3, 40, 0, 8]
l3.sort()
print(l3)

l3.sort(reverse=True)
print(l3)

l3 = [10, 2, 22, 9, 8, 33, 4]
l3.sort(key=str)
print(l3)

l3 = [10, 2, 22, 9, 8, 33, 4]
l3.sort(key=int)
print(l3)

# cf. 내장(전역) 함수 sorted
l3 = [10, 2, 22, 9, 8, 33, 4]
l4 = sorted(l3)
print(l4)

l3 = [10, 46, 22, 93, 81, 35, 44]


def f(n):
    return n % 10


l4 = sorted(l3, key=f)
print(l4)

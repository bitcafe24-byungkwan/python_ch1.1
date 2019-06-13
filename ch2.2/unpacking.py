# packing : tuple만 가능하다
t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# 에러
# a, b, c = t  : unpacking에서는 왼쪽 변수가 부족한 경우 에러가 발생한다.
# a, b, c, d, e, f = t

# unpacking extended
t = (1, 2, 3, 4, 5)
a, *b = t
print(a, b)

*a, b = t
print(a, b)

a, b, *c = t
print(a, b, c)

a, *b, c = t
print(a, b, c)


# cf. 여러 개 파라미터를 받는 함수
def mysum(*num):
    result = 0
    for n in num:
        result += n
    return result


print(mysum(1, 2))
print(mysum(1, 2, 3))


# c의 printf() 함수 흉내내기
def printf(format_str, *args):
    print(format_str % args)


printf("name: %s, age: %d", "둘리", 10)

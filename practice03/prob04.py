"""
문제4.
구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
프로그램은 정답 여부를 다시 출력합니다.
[출력]

6 x 9 = ?

81	12	32
18	54	4
32	6	32

answer: 54           [입력]

정답                 [출력]
"""
import os
import random

factor_1 = random.randrange(9) + 1
factor_2 = random.randrange(9) + 1

prod = factor_2 * factor_1
print(f"{factor_1} X {factor_2} = ?\n")


answer_set = {prod}

while len(answer_set) < 10:
    answer_set.add((random.randrange(9) + 1) * (random.randrange(9) + 1))

for ii in range(1, 10):
    print("%3d" % answer_set.pop(), end=' ' if ii % 3 else os.linesep)

while 1:
    print()
    if prod == int(input("answer:")):
        print("\n정답")
        break


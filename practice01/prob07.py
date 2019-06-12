"""
문제 7.키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
"""
num_list = []

while len(num_list) != 5:
    n = input('>')

    if n.isdigit() is False:
        print('Error: is not digit')
        continue

    num_list.append(int(n))

print(sum(num_list, 0) / len(num_list))

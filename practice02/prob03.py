"""
문제3. 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
없이 각 단어를 순서대로 출력하세요.
2)각 단어의 빈도수도 함께 출력해 보세요
"""
from collections import Counter

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

mylist = s.upper().replace('.', ' ').replace(',', ' ').replace('\n', ' ').split(' ')
my_set = sorted(set(mylist))
res = Counter(mylist)


for dict_key in my_set:
    if dict_key:
        print("%s:%d" % (dict_key, res[dict_key]))

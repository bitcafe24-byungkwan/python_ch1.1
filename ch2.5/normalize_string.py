# 문자열 데이터를 분석 하기전에 처리함수 만들기
# 1. 공백제거
# 2. 필요 없는 문자 부호 제거
# 3. 대소문자 정리
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_string(strings):
    res = []
    for string in strings:
        res.append(re.sub('[!#?]', '', string).title().strip())

    return res


results = clean_string(states)
print(results)


################################
states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_strings(strings, *funcs):
    res = []
    for string in strings:
        for func in funcs:
            string = func(string)

        res.append(string)
    return res


def remove_special(s):
    return re.sub('[!#?]', '', s)


print(clean_strings(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s)))
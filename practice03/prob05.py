"""
문제5.
선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.
"""


def sel_sort(values):
    list_values = list(values)
    lwst_value = min(list_values)
    lwst_index = list_values.index(lwst_value)
    list_values.pop(lwst_index)
    list_values.append(lwst_value)

    if len(list_values) <= 2:
        return list_values
    else:
        list_values[:len(list_values)-1] = sel_sort(list_values[:len(list_values)-1])
        return list_values


ll = [5, 9, 3, 8, 60, 20, 1]
print(sel_sort(ll))

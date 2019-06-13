"""
문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요
"""
print([x for x in '/usr/local/bin/python'.split('/') if x])

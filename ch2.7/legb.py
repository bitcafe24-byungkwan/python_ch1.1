# 네임 스페이스가 주어지지 않는 변수나 함수는 LEGB 규칙에 따라 찾게 된다.

# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Built-in


b = 300  # Global


def f():
    b = 1

    def g():
        b = 100  # Local
        print(b)
        print(b)
        print(__name__)  # Built-in
    g()


if __name__ == '__main__':
    f()

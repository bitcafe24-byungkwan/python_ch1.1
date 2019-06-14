def func1(a):
    x = 1
    return a + x


def func2(a):
    return a + x


def func3(a):
    global g
    g = 3
    return a + g


x = 2
g = 10
# (L)GB
print(func1(10))

# L(G)B
print(func2(10))
print(g)
print(func3(10))
print(g)

# LG(B)
print(dir('__builtins'))

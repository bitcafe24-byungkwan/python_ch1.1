import dis
import sys

x = (1, 2, 3)
print(compile("sys.getrefcount(x)", '', 'single').co_consts)
print(dis.dis(compile("sys.getrefcount(x)", '', 'single')))
print(sys.getrefcount(x))
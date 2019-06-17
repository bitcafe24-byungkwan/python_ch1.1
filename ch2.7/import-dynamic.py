import sys

sys.path.append('..\\python-modules')
m = __import__('mymath')

print(m.pi)
print(m.add(10, 20))

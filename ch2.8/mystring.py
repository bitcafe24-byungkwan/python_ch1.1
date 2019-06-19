class MyString:
    def __init__(self, s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        return MyString(self.s + other.s)

    def __radd__(self, other):
        return self.s + other

    def __mul__(self, other):
        return self.s * other

    def __str__(self):
        return self.s;

    def __neg__(self):
        return self.s[::-1]


s = MyString('Python Programmer is Good')

t = s / ' '

print(s / ' ')
print(s + MyString('job'))
print(MyString('Python ') * 3)
print(MyString('Hello') + MyString(' ') + MyString('World'))


print(-MyString('Python'))
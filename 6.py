class1 = set(input().split(','))
class1 = {name.strip() for name in class1}
class2 = set(input().split(','))
class2 = {name.strip() for name in class2}
x1 = class1 | class2
print(', '.join(x1))
x2 = class1 - class2
print(', '.join(x2))
x3 = class2 - class1
print(', '.join(x3))
x4 = class1 & class2
print(', '.join(x4))
print(len(','.join(x4)) - len(x4) + 1)
print(', '.join({name for name in x1 if len(name) > 10}))
print(', '.join(sorted(class1 - class2)))

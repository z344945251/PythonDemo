import sys

print(sys.path)

map = {}

map.update(a=1)

print(str(map))

it =  iter(map.values())
n = next(it)
print(n)
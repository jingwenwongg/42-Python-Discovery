#!/usr/bin/env python3

num = [2, 8, 9, 48, 8, 22, -12, 2]

new_set = set()

for i in num:
    if i > 5:
        new_set.add(i + 2)

print(num)
print(new_set)

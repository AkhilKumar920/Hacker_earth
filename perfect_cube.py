from itertools import combinations
from decimal import Decimal


def is_perfect_cube(num):
    cube_root = round(num ** (1 / 3))
    return cube_root ** 3 == num


n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    product = 1
    for j in range(i, n):
        product *= arr[j]
        if is_perfect_cube(product):
            count += 1

print(count)

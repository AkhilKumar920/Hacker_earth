def count_cyclic_shifts(n, k, s):
    target = s * k
    length = len(s)

    for i in range(1, length + 1):
        shifted = s[i:] + s[:i]
        if shifted * k == target:
            return i * k

    return -1


# Input reading
t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    result = count_cyclic_shifts(n, k, s)
    print(result)

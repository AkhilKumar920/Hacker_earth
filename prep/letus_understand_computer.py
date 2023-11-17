def count_valid_divisors(X):
    ans = 0
    for D in range(1, X + 1):
        quotient = X // D
        if len(bin(quotient)) <= len(bin(D)):
            ans += 1
    return ans


# Input reading
T = int(input().strip())

for _ in range(T):
    X = int(input().strip())
    result = count_valid_divisors(X)
    print(result)

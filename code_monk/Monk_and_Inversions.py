def count_inversions(matrix, n):
    inversions = 0

    for i in range(n):
        for j in range(n):
            for p in range(i, n):
                for q in range(j, n):
                    if matrix[i][j] > matrix[p][q]:
                        inversions += 1

    return inversions

# Input reading
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = count_inversions(matrix, n)
    print(result)

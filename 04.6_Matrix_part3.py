# 4.6
# 4.6.1
n, m = input().split()
n, m = int(n), int(m)
matrix = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)

# 4.6.2
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n - j - 1:
            matrix[i][j] = 1
        if (i <= j and i > n - 1 - j) or (i >= j and i > n - 1 - j):
            matrix[i][j] = 2

for row in matrix:
    print(*row)

# 4.6.3
n, m = input().split()
n, m = int(n), int(m)
matrix = [[0] * m for _ in range(n)]
counter = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = counter
        counter = counter + 1
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# 4.6.4
n, m = input().split()
n, m = int(n), int(m)
matrix = [[0] * m for _ in range(n)]
counter = 1

for i in range(m):
    for j in range(n):
        matrix[j][i] = counter
        counter = counter + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# 4.6.5
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n - 1 - j):
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# 4.6.6
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n - 1 - j) or (i < j and i < n - 1 - j) or (i > j and i > n - 1 - j):
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# 4.6.7
# 1
n, m = input().split()
n, m = int(n), int(m)
matrix = []
list = [_ for _ in range(1, m + 1)]

for i in range(n):
    matrix.append(list[i:])
    list.append(list[i])

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# 2
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# 4.6.8
# 1
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
counter = 1

for i in range(n):
    for j in range(m):
        matrix[i][j] = counter
        counter = counter + 1

for i in range(n):
    if i % 2 != 0:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# 2
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# 4.6.9
n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
total = 1

for l in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == l:
                matrix[i][j] = total
                total += 1

for i in range(n):
    print(*matrix[i])

# 4.6.10
n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]
counter = 1
rows_passed, columns_passed = 0, 0
current_row, current_column = 0, 0

for k in range(n * m):
    if counter == n * m + 1:
        break
    direction = k % 4
    if direction == 0:
        for j in range(columns_passed, m - columns_passed):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
        rows_passed += 1
    elif direction == 1:
        for i in range(rows_passed, n - rows_passed + 1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i
        columns_passed += 1
    elif direction == 2:
        for j in range(current_column - 1, columns_passed - 2, -1):
            matrix[current_row][j] = counter
            counter += 1
        current_column = j
    elif direction == 3:
        for i in range(current_row - 1, rows_passed - 1, -1):
            matrix[i][current_column] = counter
            counter += 1
        current_row = i

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

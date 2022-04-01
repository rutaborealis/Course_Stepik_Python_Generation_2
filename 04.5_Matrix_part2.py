# 4.5
# 4.5.1
n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j
        print(str(mult[i][j]).ljust(3), end='')
    print()

# 4.5.2
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    matrix.append([int(num) for num in input().split()])

max = matrix[0][0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
            max_i = i
            max_j = j

print(max_i, max_j)

# 4.5.3
# 1
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
a, b = map(int, input().split())

for i in range(n):
    matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# 2
n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
col1, col2 = map(int, input().split())

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)

# 4.5.4
# 1
n = int(input())
matrix = []
flag = True

for i in range(n):
    matrix.append([int(num) for num in input().split()])

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')

# 2
n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)

# 4.5.5
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

# 4.5.6
# 1
n = int(input())
matrix = [input().split() for _ in range(n)]

matrix.reverse()

for row in matrix:
    print(*row)

# 2
n = int(input())

res = [[int(x) for x in input().split()] for _ in range(n)]

for j in range(n - 1, -1, -1):
    print(*res[j])

# 4.5.7
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

matrix.reverse()

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()

# 4.5.7
n = 8
matrix = [['.'] * n for _ in range(n)]

xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])
matrix[x][y] = 'N'

for i in range(n):
    for j in range(n):
        index = (x - j) * (y - i)
        if index == 2 or index == -2:
            matrix[j][i] = '*'

for row in matrix:
    print(*row)

# 4.5.8
n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(num) for num in input().split()])

checking_sum = sum(matrix[0])
checking_flag = True
checking_list = [num for num in range(1, n ** 2 + 1)]

matrix_list = []
for i in range(n):
    for j in range(n):
        matrix_list.append(matrix[i][j])

for num in checking_list:
    if num not in matrix_list:
        checking_flag = False
        break

if checking_flag:
    for row in matrix:
        if sum(row) != checking_sum:
            checking_flag = False
            break

if checking_flag:
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + matrix[j][i]
        if sum != checking_sum:
            checking_flag = False
            break

if checking_flag:
    sum = 0
    for i in range(n):
        sum = sum + matrix[i][i]
    if sum != checking_sum:
        checking_flag = False

if checking_flag:
    sum = 0
    for i in range(n):
        sum = sum + matrix[n - 1 - i][i]
    if sum != checking_sum:
        checking_flag = False

if checking_flag:
    print('YES')
else:
    print('NO')

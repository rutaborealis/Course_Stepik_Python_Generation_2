# 2.1
# 2.1.1
a, b = int(input()), int(input())
print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep='\n')

# 2.1.2
weight, growth = float(input()), float(input())
result = weight / (growth ** 2)
if 18.5 <= result <= 25:
    print('Оптимальная масса')
elif result < 18.5:
    print('Недостаточная масса')
elif result > 25:
    print('Избыточная масса')

# 2.1.3
# 1
text = input()
price = 60
int_total = (price * len(text) // 100)
remain = (price * len(text) - (int_total * 100))
print(f'{int_total} р. {remain} коп.')

# 2
string = input()
price = 60 * len(string)
print(f'{price // 100} р. {price % 100} коп.')

# 2.1.4
text_list = input().split()
print(len(text_list))

# 2.1.5
year = int(input())
animals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
index = (year + 4) % 12
print(animals[index])

# 2.1.6
# 1
num = input()
if len(num) == 5:
    num_reverse = num[::-1]
elif len(num) == 6:
    num_slice = num[1:]
    num_reverse = num[0] + num_slice[::-1]
num_reverse = int(num_reverse)
print(num_reverse)

# 2
s = input()  # 125000
print(int(s[:-5] + s[-5:][::-1]))

# 2.1.7
# 1
num = int(input())
print(f'{num:,}')

# 2
s = input()
n = []
while len(s) > 0:
    n.append(s[-3:])
    s = s[:-3]
new_n = n[:: -1]
print(*new_n, sep=',')

# 2.1.8
# 1
n = int(input())
k = int(input())
list = [i for i in range(1, n + 1)]
while len(list) != 1:
    for i in range(0, k - 1):
        list.append(list[i])
    del list[0:k]

print(*list)

# 2
n = int(input())
k = int(input())
# list = [i for i in range(1, n + 1)]
winner = 0
for i in range(1, n + 1):
    winner = (winner + k) % i
winner = winner + 1
print(winner)

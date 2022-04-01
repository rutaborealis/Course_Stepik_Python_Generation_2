# 2.2
# 2.2.1
n = int(input())
one = 0
two = 0
three = 0
four = 0

for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    if x == 0 or y == 0:
        continue
    elif x > 0 and y > 0:
        one = one + 1
    elif x < 0 and y > 0:
        two = two + 1
    elif x < 0 and y < 0:
        three = three + 1
    elif x > 0 and y < 0:
        four = four + 1

print(f'Первая четверть: {one}\n'
      f'Вторая четверть: {two}\n'
      f'Третья четверть: {three}\n'
      f'Четвертая четверть: {four}\n')

# 2.2.2
numbers = input().split()
numbers = [int(i) for i in numbers]
count = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count = count + 1

print(count)

# 2.2.3
numbers = input().split()
numbers = [int(i) for i in numbers]

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(*numbers)

# 2.2.4
# 1
numbers = [int(i) for i in input().split()]
numbers = numbers[-1:] + numbers[:-1]
print(*numbers)

# 2
numbers = [int(i) for i in input().split()]

for i in range(1, len(numbers)):
    numbers[0], numbers[i] = numbers[i], numbers[0]

print(*numbers)

# 2.2.5
numbers = [int(i) for i in input().split()]

result = []
for i in numbers:
    if i not in result:
        result.append(i)
    else:
        continue

print(len(result))

# 2.2.6
numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
n = int(input())

result = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            result.append(numbers[i] * numbers[j])

if n in result:
    print('ДА')
else:
    print('НЕТ')

# 2.2.7
a, b = input(), input()

vars = ['камень камень', 'ничья', 'ножницы ножницы', 'ничья',
        'камень ножницы', 'Тимур', 'ножницы камень', 'Руслан',
        'бумага бумага', 'ничья', 'бумага камень', 'Тимур',
        'камень бумага', 'Руслан', 'ножницы бумага', 'Тимур',
        'бумага ножницы', 'Руслан']

print(vars[vars.index(a + ' ' + b) + 1])

# 2.2.8
a, b = input(), input()

vars = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
        'Спок-ящерица': 'Руслан'}

print(vars[(a + '-' + b)])

# 2.2.9
str = input().split('О')
if len(str) != 0:
    print(len(max(str)))
else:
    print('0')

# 2.2.10
# 1
import re

n = int(input())
refrigerators = []
for i in range(n):
    refrigerators.append(input().lower().strip())

for i in refrigerators:
    if re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', i):
        print(refrigerators.index(i) + 1, end=' ')

# 2
n = int(input())
list1 = []
for i in range(n):
    a = input()
    if 'a' in a:
        a = a[a.find('a'):]
        if 'n' in a:
            a = a[a.find('n'):]
            if 't' in a:
                a = a[a.find('t'):]
                if 'o' in a:
                    a = a[a.find('o'):]
                    if 'n' in a:
                        list1.append(i + 1)
print(*list1)

# 2.2.11
# 1
word = input() + ' запретил букву'
alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# print(s.replace('foo', 'grault'))

for i in alpha:
    if (len(word) != 0) and (i in word):
        print(word + ' ' + i)
        word = word.replace(i, '')
        word = ' '.join(word.split())
    elif len(word) == 0:
        break

word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

# 2
for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()

# 4.2
# 4.2.1
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

# 4.2.2
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)

# 4.2.3
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for list in list1:
    if max(list) > maximum:
        maximum = max(list)

print(maximum)

# 4.2.4
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# list1 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]

for list in list1:
    list.reverse()

print(list1)

# 4.2.5
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for list in list1:
    for i in list:
        total = total + i
        counter = counter + 1

print(total / counter)

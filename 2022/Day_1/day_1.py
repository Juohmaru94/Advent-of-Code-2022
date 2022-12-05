with open("day_1_input.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

max_value = 0
count = 0
new_list = []

for item in data:
    if item != '':
        num = int(item)
        count += num
    else:
        new_list.append(count)
        count = 0
    if count > max_value:
        max_value = count

print(f'The answer to question 1 is: {max_value}')
    
a = sum(sorted(new_list)[-3:])

print(f'The answer to question 2 is: {a}')
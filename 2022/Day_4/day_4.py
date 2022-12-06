with open("day_4_input.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

count=0
for i in range(len(data)):
  a = data[i].replace("-"," ").replace(","," ").split(' ')
  if (int(a[0]) >= int(a[2])) and (int(a[1]) <= int(a[3])) or (int(a[0]) <= int(a[2])) and (int(a[1]) >= int(a[3])):
    count += 1

print (f'Solution to question 1 is:{count}')

count_two=0
for i in range(len(data)):
  a = data[i].replace("-"," ").replace(","," ").split(' ')
  if (int(a[2]) <= int(a[0]) <= int(a[3])) or (int(a[2]) <= int(a[1]) <= int(a[3])) or (int(a[0]) <= int(a[2]) <= int(a[1])) or (int(a[0]) <= int(a[3]) <= int(a[1])):
    count_two += 1

print(f'Solution to question 1 is:{count_two}')
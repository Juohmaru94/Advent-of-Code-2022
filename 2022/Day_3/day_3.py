with open("day_3_input.txt") as f:
    data = [i for i in f.read().strip().split("\n")]


for i in range(len(data)):
  firstpart, secondpart = data[i][:len(data[i])//2], data[i][len(data[i])//2:]
  set(firstpart)
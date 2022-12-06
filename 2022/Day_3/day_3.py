with open("day_3_input.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

values_upper = {chr(i): i - 38 for i in range(ord("A"), ord("A") + 26)}
values_lower = {chr(i): i - 96 for i in range(ord("a"), ord("a") + 26)}
values =  {**values_lower, **values_upper}

count = 0

for i in range(len(data)):
  a, b = data[i][:len(data[i])//2], data[i][len(data[i])//2:]
  common = "".join(set(a).intersection(b))

  for letter in common:
    count += values[common]

print(f"The answer to question 1 is: {count}")

def chunks(data, n):
  for i in range(0, len(data), n):
    yield data[i:i + n]
  
dataset = list(chunks(data,3))

new_count = 0

for i in range(len(dataset)):
  same = set.intersection(*map(set,dataset[i]))
  new_count += values[list(same)[0]]
print(f"The answer to question 2 is: {new_count}")
  
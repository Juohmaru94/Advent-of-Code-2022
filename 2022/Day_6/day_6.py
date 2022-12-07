with open("day_6_input.txt") as f:
    data = [i for i in f.read()]
    data.pop()
    data = [*data]

def find_answer():
  for i in range(len(data)):
    check_dataz = data[i:i+4]
    check_data = set(check_dataz)
    if len(check_data) == len(check_dataz):
      return str(''.join(check_dataz))

new_data = str(''.join(data))
print (f"Answer to question 1 is: {new_data.rfind(find_answer()) + 4}")


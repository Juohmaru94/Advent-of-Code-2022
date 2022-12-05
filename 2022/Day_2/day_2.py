with open("day_2_input.txt") as f:
    data = [i for i in f.read().strip().split("\n")]

outcomes = {
  'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2 ,'C Z':6
}

outcomes_two = {
  'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6 ,'C Z':7
}

def counter(result):
  total = 0  
  for games in data:
    total += result[games]

  return total

print(f'Answer for question one is: {counter(outcomes)}')
print(f'Answer for question two is: {counter(outcomes_two)}')
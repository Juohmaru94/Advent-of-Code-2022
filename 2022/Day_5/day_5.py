with open("day_5_input.txt") as f:
    stacked, moves = (i.splitlines() for i in f.read().strip('\n').split("\n\n"))

stacks = {int(number):[] for number in stacked[-1].replace(" ","")}
indexes = [index for index, char in enumerate(stacked[-1]) if char != " "]

for i in stacked[:-1]:
  stack_num = 1
  for j in indexes:
    if i[j] != " ":
      stacks[stack_num].insert(0, i[j])
    stack_num += 1

for move in moves:
  move = move.replace("move","").replace("from","").replace("to","").strip().split()
  move = [int(i) for i in move]
  
  crates = move[0]
  from_stack = move[1]
  to_stack = move[2]

  for crate in range(crates):
    crate_removed = stacks[from_stack].pop()
    stacks[to_stack].append(crate_removed)
    
answer = '' 
for stack in stacks:
 answer += stacks[stack][-1]

print(f'Part 1 answer is: {answer}')
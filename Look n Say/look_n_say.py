import sys
import re

seed = ""

try:
  N = int(sys.argv[1])
  
  if len(sys.argv) > 2:
    seed = str(sys.argv[2])
    
except:
  
  print("usage: look_n_say.py N [--seed]")

  print("\npositional arguments:\n N\t number of iterations.")
  print("\noptional arguments:\n --seed\t starting seed.")
  sys.exit()
  
if seed == "":
  seed = "1"

word = seed

for _ in range(N):
  
  print(word)

  length = len(word)

  current_amount = 0
  current_number = word[0]
  new_word = ""
  
  for number in word:
    
    if number == current_number:
      current_amount += 1
    else:
      new_word += str(current_amount)
      new_word += current_number
      current_number = number
      current_amount = 1
    
  new_word += str(current_amount)
  new_word += current_number

  word = new_word

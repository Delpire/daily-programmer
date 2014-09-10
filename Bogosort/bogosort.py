import random

def scramble(word):
  """Randomly scrambles a string.
  :param word: a plaintext string to randomly scramble.
  """
  
  #Turn the word into a list so we can index to individual chars.
  l = list(word)
  
  for x in range(1000):
    
    #Randomly take two indicies.
    i = random.randrange(0, len(word))
    j = random.randrange(0, len(word))
    
    #Swap the chars at those indicies.
    l[i], l[j] = l[j], l[i]
  
  return ''.join(l)

if __name__ == '__main__':
    
  unsorted_word = str(input("Enter unsorted word: "))
  sorted_word = str(input("Enter sorted word: "))
  
  iterations = 0;
  
  #Bogosort! While the word isn't sorted, scramble the word.
  while(unsorted_word != sorted_word):
    unsorted_word = scramble(unsorted_word)
    iterations += 1
  
  #Print the previously unsorted word, proving its sorted.
  #And print the number of iterations, to show how long it took.
  print(unsorted_word)
  print(iterations)
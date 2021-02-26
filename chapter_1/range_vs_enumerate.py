#print("Hello world")

def fizz_buzz(numbers):
  '''
  Given a list of integers:
  1. Replace all integers that are evenly divisible by 3
  with "fizz"
  2. Replace all integers divisble  by 5 with "buzz"
  3. Replace all integers divisible by both 3 and 5 with
  "fizzbuzz"
  >>> numbers = [45, 22,14,65, 97, 72]
  >>> fizz_buzz(numbers)
  >>> numbers
  ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
  '''

  ''' for i in range(len(numbers)):
    num = numbers[i]
    if  num % 3 ==0 and num % 5 == 0:
      numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
      numbers[i] = 'fizz'
    elif num % 5 == 0:
      numbers[i] = 'buzz'
    
 '''

  for i, num in enumerate(numbers):
    if  num % 3 ==0 and num % 5 == 0:
      numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
      numbers[i] = 'fizz'
    elif num % 5 == 0:
      numbers[i] = 'buzz'

  #return output

#print(fizz_buzz([45, 22, 14, 65, 97, 72])) 

#ipython --no-banner -i range_vs_enumerate.py
#python3 -m doctest range_vs_enumerate.py
#[tup for tup in enumerate([1,2,3], start = 10)]
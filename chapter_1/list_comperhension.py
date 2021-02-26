lst = [1, 2, -5, 4]

def square(x):
  return x * x

map(square, lst)
print(list(map(square, lst)))
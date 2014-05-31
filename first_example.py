x = 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lost = 11

while l[x] != lost:
  print("not this one!")
  x = x + 1

  if x == len(l):
    break
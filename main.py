def readFiles():
  with open('b_little_bit_of_everything.in') as f:
    mylist = [line.rstrip('\n') for line in f]
  a = mylist[1].split(" ")
  b = mylist[2].split(" ")

  print(a)
  print(b)
  counter = 0
  if int(a[0]) < int(b[0]):
      temp = a
      a = b
      b = temp
  counter = int(a[0]) + int(b[0])
  for i, x in enumerate(a):
    if i == 0:
      continue
    for j, x in enumerate(b):
      if j == 0:
        continue
      if a[i]==b[j]:
        counter-=1
  print(counter)
readFiles()
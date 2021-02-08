# def readFiles():
#   with open('C:/Users/Jason/Desktop/Hashcode/b_little_bit_of_everything.in') as f:
#     mylist = [line.rstrip('\n') for line in f]
#
#   firstLine = mylist[0].split(" ")
#   a = mylist[1].split(" ")
#   b = mylist[2].split(" ")
#
#   print(a)
#   print(b)
#   counter = 0
#   if int(a[0]) < int(b[0]):
#       temp = a
#       a = b
#       b = temp
#   counter = int(a[0]) + int(b[0])
#   for i, x in enumerate(a):
#     if i == 0:
#       continue
#     for j, x in enumerate(b):
#       if j == 0:
#         continue
#       if a[i]==b[j]:
#         counter-=1
#   print(counter)
# readFiles()
output = []


def checkServedPizza(checkMostIngredient,servedPizza,mostIngredient,mylist):
  for served in servedPizza:
    if checkMostIngredient == served:
      return False
    if mostIngredient == int(mylist[checkMostIngredient].split(" ")[0]):
      return False

  return True


def loop():
    with open('b_little_bit_of_everything.in') as f:
      mylist = [line.rstrip('\n') for line in f]

    firstLine = mylist[0].split(" ")

    totalPizza = int(firstLine[0])
    p2 = int(firstLine[1])
    p3 = int(firstLine[2])
    p4 = int(firstLine[3])

    # lineCounter = 1
    fixCounter = 1
    # totalPizza+=1
    swap = False
    maxIngredient = 0



    #pizza that are already served (BY ROW)
    servedPizza=[]

    #Store ouput
    maxIngredientLine=[]
    # LOOP 1.0 
    for x in range(2):

        # Line with most ingredient
        mostIngredientLine = -1

        # Number of most ingredient
        mostIngredient = -1

        lineCounter = 1
        checkMostIngredient = 1

        
        # LOOP CHECK IF PIZZA IS SERVED
        for x in range(totalPizza):
          breakBool = False
          for served in servedPizza:
              if x == served:
                breakBool = True

          if x==0 or breakBool == True:
              continue
        
        # FIND MOST INGREDIENT IN FILE
        # LAST 2 VAR
          if mostIngredient < int(mylist[checkMostIngredient].split(" ")[0]) and checkServedPizza(checkMostIngredient,servedPizza,mostIngredient,mylist):
              mostIngredientLine = checkMostIngredient
              mostIngredient = int(mylist[checkMostIngredient].split(" ")[0])
          checkMostIngredient+=1
        # LOOP 1.1
        for x in range(totalPizza):
            fixLine = mylist[mostIngredientLine].split(" ")
            compareLine = mylist[lineCounter].split(" ")
            #swapLine
            if int(fixLine[0]) < int(compareLine[0]):
                temp = fixLine
                fixLine = compareLine
                compareLine = temp
                swap = True
            #calculate total ingredients
            counter = int(fixLine[0]) + int(compareLine[0])

            #calculate diff ingredients for 2 pizza
            for i, x in enumerate(fixLine):
                if i == 0:
                    continue
                for j, x in enumerate(compareLine):
                    if j == 0:
                        continue
                    if fixLine[i]==compareLine[j]:
                        counter-=1
            
            if counter > maxIngredient:
                temp = counter
                counter = maxIngredient
                maxIngredient = temp
                maxLine = fixCounter + lineCounter

          # SWAP LARGER LINES WITH SMALLER LINES
            if swap == True:
                temp = fixLine
                fixLine = compareLine
                compareLine = temp
                swap = False
            lineCounter+=1
      
        maxIngredientLine.append(4)
        maxIngredientLine.append(mostIngredientLine)
        maxIngredientLine.append(maxLine)
        servedPizza.append(mostIngredientLine)
        servedPizza.append(maxLine)
        print(servedPizza)
        p4-=1
        print(maxIngredientLine)
        print(p4)




# def swapLine():
#     if int(fixLine[0]) < int(compareLine[0]):
#         temp = fixLine
#         fixLine = compareLine
#         compareLine = fixLine
#         swap = True

loop()
import sys

with open('Input_Files/e_many_teams.in', 'r') as f:
    content = f.readlines()
    ingredients = []
    noPizza, t2, t3, t4 = [int(x) for x in content[0].split()]
    pizzaList = []
    for x in range(1, noPizza + 1):
        tempContent = content[x]
        seperatedPizzaLineContent = tempContent.split()
        del seperatedPizzaLineContent[0]
        for ingredient in seperatedPizzaLineContent:
            if ingredient not in ingredients:
                ingredients.append(ingredient)
        pizzaList.append(tempContent)
    maxIngredientNumber = len(ingredients)
    lines = [x for x in range(0, noPizza)]

outArr2 = []
outArr3 = []
outArr4 = []


def loop(numberOfPizza):
    selectedIngredient = ""
    for _ in range(numberOfPizza):
        maxLine = -1
        uniqueIngredient = -1
        if selectedIngredient.count(" ") < maxIngredientNumber:
            # In search for the most ingredients
            print("line start by max")
            for pizzaLineNumber, pizzaLineContent in enumerate(pizzaList):
                seperatedPizzaLineContent = pizzaLineContent.split()
                del seperatedPizzaLineContent[0]

                score = 0

                for ingredient in seperatedPizzaLineContent:
                    if selectedIngredient.find(ingredient) == -1:
                        score += 1
                if uniqueIngredient < score:
                    uniqueIngredient = score
                    maxLine = pizzaLineNumber
            exec("outArr" + str(numberOfPizza) + "." +
                 "append(lines[maxLine])")
            a = pizzaList[maxLine].split()
            del a[0]
            for ingredient in a:
              if selectedIngredient.find(ingredient) == -1:
                  selectedIngredient += (ingredient + " ")
            del lines[maxLine]
            del pizzaList[maxLine]
            print("line start by max")
            

        else:
            print("line start by min")
            min = sys.maxsize
            line = -1
            for pizzaLineNumber, pizzaLineContent in enumerate(pizzaList):
                seperatedPizzaLineContent = pizzaLineContent.split()
                if min > int(seperatedPizzaLineContent[0]):
                    min = int(seperatedPizzaLineContent[0])
                    line = pizzaLineNumber
            exec("outArr" + str(numberOfPizza) + "." + "append(lines[line])")
            del lines[line]
            del pizzaList[line]
            print("line done by min")


def assignPizza():
    totalPizza = noPizza
    global t2, t3, t4
    while totalPizza > 0:
      if totalPizza == 4 and t4 > 0:
        loop(4)
        totalPizza = totalPizza - 4
        t4-=1
      elif (totalPizza == 5 or totalPizza == 3) and (t3>0):
        loop(3)
        totalPizza = totalPizza - 3
        t3-=1
      elif (totalPizza == 2 or totalPizza ==4)and (t2 > 0):
        loop(2)
        totalPizza = totalPizza - 2
        t2-=1
      elif (t4>0 and totalPizza >= 4) :
        loop(4)
        totalPizza = totalPizza - 4
        t4-=1
      elif (t3>0 and totalPizza >= 3):
        loop(3)
        totalPizza = totalPizza - 3
        t3-=1
      elif (t2>0 and totalPizza >= 2):
        loop(2)
        totalPizza = totalPizza - 2
        t2-=1
      else:
        break


def printOutput():
    f = open("C:/Users/mohdb/Desktop/google hashcode/e_many_teams.txt", "w")
    f.write(
        str(int((len(outArr4) / 4) + (len(outArr3) / 3) + (len(outArr2) / 2))))
    f.write("\n")
    while len(outArr4) >= 4:
        f.write("4 ")
        for _ in range(4):
            f.write(str(outArr4[0]) + " ")
            outArr4.pop(0)
        f.write("\n")

    while len(outArr3) >= 3:
        f.write("3 ")
        for _ in range(3):
            f.write(str(outArr3[0]) + " ")
            outArr3.pop(0)
        f.write("\n")

    while len(outArr2) >= 2:
        f.write("2 ")
        for _ in range(2):
            f.write(str(outArr2[0]) + " ")
            outArr2.pop(0)
        f.write("\n")

    f.close()


assignPizza()
printOutput()

# loop(4)
# print(outArr2)
# print(outArr3)
# print(outArr4)
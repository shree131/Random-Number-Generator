import random

randList = {}

def generateRand():
    for i in range(10000):
        n = random.randint(-1000, 1000)

        if n in randList:
            randList[n] += 1
        else:
            randList[n] = 1
    count()
            
def count():
    for n in sorted(randList.keys()):
        count = randList[n]
        print(n, "occurs", count, "times")


generateRand()

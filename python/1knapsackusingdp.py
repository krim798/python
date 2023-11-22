import random
import sys
sys.getrecursionlimit()
sys.setrecursionlimit(2000)
#knapsack problem example using dynamic programming
class food(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <'+ str(self.value)+','+str(self.calories)+'>' 
def buildMenu(names, values,calories):
    """names, values, calories lists of same length.
    name a list of strings, values and calories lists of numbers returns list of Foods""" 
    menu=[]
    for i in range(len(values)):
        menu.append(food(names[i], values[i], calories[i]))
    return menu
def buildLargeMenu(numItems, maxVal, maxCost):
      items=[]
      for i in range(numItems):
            items.append(food(str(i),random.randint(1, maxVal),random.randint(1, maxCost)))
      return items  
def fastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)
#Change code to keep track of number of calls
def countingFastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    global numCalls
    numCalls += 1
    
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = countingFastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 countingFastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = countingFastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result
for numItems in (5,10,15,20,25,30,35,40,45,1024):
      items=buildLargeMenu(numItems,90,250)
      testMaxVal(items,750,fastMaxVal,False)

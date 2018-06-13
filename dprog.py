# http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
print("\n Dynamic Programming\n")

print("Recursive coin changes\n")
cntSteps = 0

def recMC(coinValueList,change):
   global cntSteps
   cntSteps = cntSteps + 1
   # print('.', end='')
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

def recDC(coinValueList,change,knownResults):
   global cntSteps
   cntSteps = cntSteps + 1
   print('.', end='')
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins


COIN_1 = 1
COIN_2 = 5
COIN_3 = 10
COIN_4 = 25
COIN_CHANGE = 63

#print("\nMinimum coins [", recMC([COIN_1,COIN_2,COIN_3,COIN_4],COIN_CHANGE), "]  took [", cntSteps, "] steps")
# print("\nMinimum coins [", recDC([COIN_1,COIN_2,COIN_3,COIN_4],COIN_CHANGE,[0]*64), "]  took [", cntSteps, "] steps")

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = COIN_CHANGE
    clist = [COIN_1,COIN_2,COIN_3,21,COIN_4]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()



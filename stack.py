# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

from pythonds.basic.stack import Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

print("")
print("Sum numbers in a list")
numlist = [5,6,7]
print(numlist)
print(sum(numlist))


print("")
print("Reversing text using Stack")
text = "The Quick Brown Fox Jumps Over The Lazy Dog"
print(text)
listtext = list(text)
print(listtext)
revtextlist = []
t=Stack()
revtext = ''
for item in listtext:
    t.push(item)
while t.size():
    #revtextlist.append(t.pop())
    revtext = revtext + str(t.pop())
#print(revtextlist)
#revtext = ''.join(revtextlist)
print(revtext)

print("")
print("Using Stack to check for balanced parentheses")
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker('((()))'))
print(parChecker('(()'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))



print("")
print("Using stack trick 'divideBy2' to convert decimal to binary")
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2     # use modulo '%' to get the remainder, eg rem = 8%3 = 2
        remstack.push(rem)          # get the floor of divide operation, eg ans= 8//3 = 2
        decNumber = decNumber // 2  # therefore, ans*3 + rem = decNumber

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
print("Convert Base10 (decimal) to Base2 (binary): 42d = " + divideBy2(42) + "b")

print('')
print("Convert Base10 (decimal) to other specified Base N, using stack")
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print("Convert Base10 (decimal) to Base2 (binary): 25d = " + baseConverter(25,2) + " (base2)")
print("Convert Base10 (decimal) to Base16 (hex): 25d = " + baseConverter(25,16) + " (base16)")
print("Convert Base10 (decimal) to Base8 (octal): 25d = " + baseConverter(25,8) + " (base8)")
print("Convert Base10 (decimal) to Base16 (hex): 256d = " + baseConverter(256,16) + " (base16)")



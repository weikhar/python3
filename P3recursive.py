# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html

print('\nRecursive in Python')
def listsum1(numList):
	theSum = 0
	for i in numList:
		theSum = theSum + i
	return theSum

def listsum2(numList):
	if len(numList) == 1:
		return numList[0]
	else:
		return numList[0] + listsum2(numList[1:])

print('Summing sequentially gets ', listsum1([1,3,5,7,9]))
print('Summing recursively gets ', listsum2([1,3,5,7,9]))


import timeit
def test1():
    return listsum1([1,3,5,7,9])

def test2():
    return listsum2([1,3,5,7,9])

t1 = timeit.Timer("test1()", "from __main__ import test1")
print('\nSumming sequentially duration = ', t1.timeit(number=1000000), ' ms')

t2 = timeit.Timer("test2()", "from __main__ import test2")
print('Summing recursively duration = ', t2.timeit(number=1000000), ' ms')

# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html
print("Recursively Converting from Integer to String")
def toStr(n,base):
	convertString = "0123456789ABCDEF"
	if n < base:
		return convertString[n]
	else:
		return toStr(n//base,base) + convertString[n%base]  # by concatenation after return from recursive calls, result in proper order
print("Convert 1453dec to hex = ", toStr(1453,16))
# print ('5' + 'A' + 'D') #=  SAD
print("Convert 10dec to bin = ", toStr(10,2))


print("\nReverse a string")

def testEqual(actual, expected):
	if type(expected) == type(1):
		# they're integers, so check if exactly the same
		if actual == expected:
			print('Pass')
			return True
		elif type(expected) == type(1.11):
			# a float is expected, so just check if it's very close, to allow for
			# rounding errors
			if abs(actual-expected) < 0.00001:
				print('Pass')
			return True
	else:
		# check if they are equal
		if actual == expected:
			print('Pass')
			return True
	print('Test Failed: expected ' + str(expected) + ' but got ' + str(actual))
	return False

def reverse(s):
	return s[::-1]

testEqual(reverse("hello"),"olleh")
testEqual(reverse("l"),"l")
testEqual(reverse("follow"),"wollof")
testEqual(reverse(""),"")


print("\nPanlindrome checker")
from string import maketrans

def panlindromeCheck(s):
	#s.translate(None, s.punctuation)
	s.replace(s.punctuation, "")
	s.replace(" ", "")
	return s[::-1]

testEqual(panlindromeCheck("12345"),"54321")
testEqual(panlindromeCheck("kayak122"),"kayak122")
testEqual(panlindromeCheck("kayak"),"kayak")
testEqual(panlindromeCheck("aibohphobia"),"aibohphobia")
testEqual(panlindromeCheck("Live not on evil"),"Live not on evil")
testEqual(panlindromeCheck("Reviled did I live, said I, as evil I did deliver"),"Reviled did I live said I as evil I did deliver")
testEqual(panlindromeCheck("Go hang a salami; I’m a lasagna hog"),"Go hang a salami Im a lasagna hog")
testEqual(panlindromeCheck("Kanakanak "),"Kanakanak ")






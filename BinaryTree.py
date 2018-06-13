# http://interactivepython.org/runestone/static/pythonds/Trees/ListofListsRepresentation.html
print("\nBinary Tree")
def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)							# inserting Left, so pop the 2nd item to 't' (ie 1st item in child row)
    if len(t) > 1:		
        root.insert(1,[newBranch,t,[]])		# if 2nd item is occupied, put it to 3rd place
    else:
        root.insert(1,[newBranch,[],[]])	# if 2nd item is empty, restore to 2nd place
    return root                             # return the updated root

def insertRight(root,newBranch):
    t = root.pop(2)							# inserting Right, so pop the 3rd item to 't' (ie 2nd item in child row)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])		# if 3rd item is occupied, put it to 4th place
    else:
        root.insert(2,[newBranch,[],[]])	# if 3rd item is empty, restore to 3rd place
    return root                             # return the updated root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
print("BinaryTree(3)....", r)
insertLeft(r,4)
print("insertLeft(r,4)..", r)
insertLeft(r,5)
print("insertLeft(r,5)..", r)
insertRight(r,6)
print("insertLeft(r,6)..", r)
insertRight(r,7)
print("insertLeft(r,7)..", r)
l = getLeftChild(r)
# print(l)
print("getLeftChild(r)..", l)

setRootVal(l,90)
# print(r)
print("setRootVal(l,90)..", r)
insertLeft(l,80)
# print(r)
print("insertLeft(l,80)..", r)
print(getRightChild(getRightChild(r)))

print("\nmctree_2")
ttree = BinaryTree('a')
insertLeft(ttree,'b')
insertRight(ttree,'c')
insertLeft(getLeftChild(ttree),'d')
insertLeft(getRightChild(ttree),'e')
insertRight(getRightChild(ttree),'f')
print(ttree)

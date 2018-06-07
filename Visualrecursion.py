# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsintro-VisualizingRecursion.html
print("\nVisualizingRecursion")

# In the previous section we looked at some problems that were easy to solve using recursion; 
# however, it can still be difficult to find a mental model or a way of visualizing what is happening 
# in a recursive function. This can make recursion difficult for people to grasp. 
# In this section we will look at a couple of examples of using recursion to draw some interesting pictures. 
# As you watch these pictures take shape you will get some new insight into the recursive process 
# that may be helpful in cementing your understanding of recursion.

# The tool we will use for our illustrations is Python’s turtle graphics module called turtle. 
# The turtle module is standard with all versions of Python and is very easy to use. 
# The metaphor is quite simple. 
# You can create a turtle and the turtle can move forward, backward, turn left, turn right, etc. 
# The turtle can have its tail up or down. 
# When the turtle’s tail is down and the turtle moves it draws a line as it moves. 
# To increase the artistic value of the turtle you can change the width of the tail as well as the 
# color of the ink the tail is dipped in.

# Here is a simple example to illustrate some turtle graphics basics. 
# We will use the turtle module to draw a spiral recursively. 
# After importing the turtle module we create a turtle. 
# When the turtle is created it also creates a window for itself to draw in. 
# Next we define the drawSpiral function. 
# The base case for this simple function is when the length of the line we want to draw, 
# as given by the len parameter, is reduced to zero or less. 
# If the length of the line is longer than zero we instruct the turtle to go forward by len units and 
# then turn right 90 degrees. 
# The recursive step is when we call drawSpiral again with a reduced length. 
# At the end of ActiveCode 1 you will notice that we call the function myWin.exitonclick(), 
# this is a handy little method of the window that puts the turtle into a wait mode until you click 
# inside the window, after which the program cleans up and exits

import turtle


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

#print("\nTutle recursively draw line")
# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()
#drawSpiral(myTurtle,100)
#myWin.exitonclick()


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

# print("\nTutle recursively draw tree")
#main()

# Homework
# Modify the recursive tree program using one or all of the following ideas:
# Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
# Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
# Modify the angle used in turning the turtle so that at each branch point the angle is selected at 
#   random in some range. For example choose the angle between 15 and 45 degrees. 
#   Play around to see what looks good.
# Modify the branchLen recursively so that instead of always subtracting the same amount you 
#   subtract a random amount in some range.

def star():
    s = turtle.Turtle()
    myWin = turtle.Screen()
    i = 360
    while i > 0:
        s.forward(100)
        s.right(170)
        i = i - 10
    myWin.exitonclick()

# print("\nTutle recursively draw star")
#star()


# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsSierpinskiTriangle.html
# print("\n Sierpinski Triangle")

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def do_sierpinski():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

# do_sierpinski()

#
print("\n Tower of Hanoi")
nDisks = 3
nSteps = 0
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
	global nSteps
	nSteps = nSteps + 1
    print("Step:",nSteps,"- moving disk from",fp,"to",tp)

print("To move {} disks".format(nDisks))
moveTower(nDisks,"A","B","C")

# TODO: show the step count for each move 
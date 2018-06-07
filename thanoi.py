# http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html
print("\n Tower of Hanoi")
nDisks = 8
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
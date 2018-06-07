# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

print("Python Queue")
q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())


print("")
print("Hot Potato simulation using Queue")
from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)
		print("nQ >" + name)

	while simqueue.size() > 1:
		print("")
		print("Q size = " + str(simqueue.size()))
		for i in range(num):
			player = simqueue.dequeue()
			simqueue.enqueue(player)
			print("  nQ player: " + player)
		outplayer = simqueue.dequeue()
		print("  > dQ player: " + outplayer)
	
	return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


# http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html
print("Listing 2 - Printing task")
# main simulation.
# Create a queue of print tasks. 
#   Each task will be given a timestamp upon its arrival. 
#   The queue is empty to start.
# For each second (currentSecond):
#   Does a new print task get created? 
#     If so, add it to the queue with the currentSecond as the timestamp.
#   If the printer is not busy and if a task is waiting,
#   Remove the next task from the print queue and assign it to the printer.
#   Subtract the timestamp from the currentSecond to compute the waiting time for that task.
#   Append the waiting time for that task to a list for later processing.
#   Based on the number of pages in the print task, figure out how much time will be required.
# The printer now does one second of printing if necessary. 
# It also subtracts one second from the time required for that task.
# If the task has completed (ie time required has reached zero), the printer is no longer busy.
# After the simulation is complete, compute the average waiting time from the list of waiting times generated.

class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
		if self.timeRemaining <= 0:
			self.currentTask = None

	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False

	def startNext(self,newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages() * 60/self.pagerate


# Listing 3
import random

class Task:
	def __init__(self,time):
		self.timestamp = time
		self.pages = random.randrange(1,sim_avg_pages+1)	# number of pages 1~20

	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):
		return currenttime - self.timestamp

# Listing 4
def simulation(numSeconds, pagesPerMinute):
	labprinter = Printer(pagesPerMinute)
	printQueue = Queue()
	waitingtimes = []

	for currentSecond in range(numSeconds):
		if newPrintTask():
			task = Task(currentSecond)
			printQueue.enqueue(task)

		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask = printQueue.dequeue()
			waitingtimes.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)

		labprinter.tick()

	averageWait=sum(waitingtimes)/len(waitingtimes)
	print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
	num = random.randrange(1,sim_avg_task_period+1)	#average of 1 task per 180s
	if num == sim_avg_task_period:
		return True
	else:
		return False

# simulation setup
sim_students = 20		# number of students
sim_avg_prt_cnt = 2		# average #prints per student
sim_avg_pages = 20		# average #pages per print
sim_avg_ppm = 10		# average #pages per minute
sim_avg_task_period = (60 * 60) / (sim_students * sim_avg_prt_cnt)
# if 10 students each print twice, then have 20 tasks per hour on average
# therefore: 20 tasks/hour = 20 tasks in 3600s = (avg) 1 task in 180s
# If 20 students, then 40 tasks per hour >> 40/3600 = 1 task in 90s
print ("sim_students		= " + str(sim_students))
print ("sim_avg_prt_cnt		= " + str(sim_avg_prt_cnt))
print ("sim_avg_pages		= " + str(sim_avg_pages))
print ("sim_avg_ppm		= " + str(sim_avg_ppm))
print ("sim_avg_task_period	= " + str(sim_avg_task_period))

# simuluation: 10 tries, for period of 60mins with X ppm
for i in range(10):
	simulation(3600,sim_avg_ppm)


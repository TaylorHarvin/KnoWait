#!\usr\bin\python3
import random
import datetime

#print(random.randrange(10))
#random.randint(1, 10)

maxRecSize = 50
maxNumEmp = 20
maxTotalSpent = 100
monWed = [[0]*13 for i in range(2)]
tueThurs = [[0]*13 for i in range(2)]
friday = [[0]*13 for i in range(2)]


monWed[0] = [0,0,0,15,35,35,45,35,25,15,0,0,0]
monWed[1] = [10,10,10,25,45,45,55,45,35,25,10,10,10]
tueThurs[0] = [0,0,0,10,30,30,40,30,20,10,0,0,0]
tueThurs[1] = [5,5,5,25,40,40,50,40,30,20,5,5,5]
friday[0] = [0,0,0,5,25,25,35,25,15,5,0,0,0]
friday[1] = [5,5,5,15,35,35,45,35,25,15,5,5,5]

MIN_WAIT = 180
EMPL_CONST = 6



class DataPoint:
	timePoint = 0
	numEmployees = 0
	totalSpent = 0
	dayOfWeek = 0
	dayOfYear = 0
	numReceipts = 0


	def __init__(self,tp,currDate):
		self.timePoint = tp
		if(currDate.weekday() == 0 or currDate.weekday() == 2):
			self.numReceipts = random.randint(monWed[0][int((tp/4)-7)], monWed[1][int((tp/4)-7)])
		elif(currDate.weekday() == 1 or currDate.weekday() == 3):
			self.numReceipts = random.randint(tueThurs[0][int((tp/4)-7)], tueThurs[1][int((tp/4)-7)])
		else:
			self.numReceipts = random.randint(friday[0][int((tp/4)-7)], friday[1][int((tp/4)-7)])

		#print(self.numReceipts)
		#print(self.numReceipts);
		self.numEmployees = int(self.numReceipts*0.10) + 2
		self.totalSpent = round(random.uniform(5.0,15.0)*self.numReceipts,2)
		self.dayOfMonth = currDate.day
		self.month = currDate.month
		self.dayOfWeek = currDate.weekday()
		self.waitTime = round(((random.uniform(15.0,30.0)*self.totalSpent) + MIN_WAIT)/self.numEmployees,2)
		#print(self.waitTime)

	def getPrintVersion(self):
		return str(self.timePoint) + "," + str(self.numReceipts) + "," + str(self.numEmployees)+ "," + str(self.totalSpent) \
		+ "," + str(self.dayOfMonth) + "," + str(self.month) + "," + str(self.dayOfWeek) \
		+ "," + str(self.waitTime) + "\n"
		


class DataGen:

	def __init__(self):
		self.data = 0

			






def genTime():
	#return random.randint(28, 76)
	timeRange = [0]*48;

	for i in range(48):
		timeRange[i] = i + 28

	return timeRange

random.seed(0)

timeArray = genTime()

dg = DataGen()

fall2016SemStart = datetime.date(2016,8,22)
fall2016SemEnd = datetime.date(2016,12,10)


f = open('FallData','w+')



for i in range((fall2016SemEnd-fall2016SemStart).days-1):
	currDate = fall2016SemStart + datetime.timedelta(i)
	for i in range(28,77):
		dp = DataPoint(i,currDate)
		#print(dp.getPrintVersion())
		f.write(dp.getPrintVersion())

f.close()

import time
import datetime
#from dateutil.rrule import rrule, DAILY

fall2016SemStart = datetime.date(2016,8,22);
fall2016SemEnd = datetime.date(2016,12,10);


def changeDate():
    currDate = fall2016SemStart
    isWeekDay = 0
    '''a = date(2009, 5, 30)
    b = date(2009, 6, 9)
    for dt in rrule(DAILY, dtstart=a, until=b):
        print (dt.strftime("%Y-%m-%d"))'''
    for i in range((fall2016SemEnd-fall2016SemStart).days-1):
        #print (datetime.date.today() + datetime.timedelta(i))
        currDate = fall2016SemStart + datetime.timedelta(i)
        if(currDate.weekday() < 5):
            isWeekDay = True;
        else:
            isWeekDay = False;
        print (currDate,isWeekDay)
        

def GenerateTestInput():
    print("test")


changeDate()

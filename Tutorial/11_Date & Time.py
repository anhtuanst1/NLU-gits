from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
	''' Get today's date from datetime class '''
	today=datetime.now()		# ngay gio hien tai
	print today, "\n"

	today = date.today()
	print "Date: ", today
	print "Components:\n\t day: %d \t month: %d \t year: %d\n" %(today.day, today.month, today.year)


	''' Get the current time '''
	t = datetime.time(datetime.now())
	print "Time: ", t
	print "Components:\n\t hour: %d \t min: %d \t second: %d \t microsecond: %d\n" %(t.hour,t.minute,t.second,t.microsecond)


	''' Days start at 0 for monday '''
	wd = date.weekday(today)
	# wd	  0			1		   2		  3			4		  5			6
	days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
	print "Today is day number %d" % wd
	print "which is a " + days[wd], "\n"


	''' Times and dates '''
	now = datetime.now()  # get the current date and time
	# %c - local date and time, %x-local's date, %X- local's time
	print "date_time: ", now.strftime("%c")
	print "date: ", now.strftime("%x")
	print "time: ", now.strftime("%X"), "\n"

	''' Time Formatting '''
	# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
	print "12H - ", now.strftime("%I:%M:%S %p")  # 12-Hour:Minute:Second:AM
	print "24H - ", now.strftime("%H:%M"), "\n"  # 24-Hour:Minute


	# khoi tao 1 timedelta
	print timedelta(days=365, hours=8, minutes=15)
	print "today is:\t\t" + str(datetime.now())	# print today's date
	# print today's date one year from now
	print "+ 1 year from now it will be:\t" + str(datetime.now() + timedelta(days=365))
	# create a timedelta that uses more than one argument
	print "+ 1 week and 4 days it will be:\t" + str(datetime.now() + timedelta(weeks=1, days=4))

	# How many days until New Year's Day?
	today = date.today()  # get todays date
	nyd = date(today.year, 1, 1)  # get New Year Day for the same year
	print "\nnyd:\t", nyd
	print "today:\t", today
	# use date comparison to see if New Year Day has already gone for this year
	# if it has, use the replace() function to get the date for next year
	if nyd < today:
		print "today - nyd = ", (today - nyd).days
		print "New Year day is already went by %d days ago" % ((today - nyd).days)


if __name__== "__main__":
    main()
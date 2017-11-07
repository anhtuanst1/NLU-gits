import calendar

''' Tao lich '''
c= calendar.TextCalendar(calendar.SUNDAY)		# 'calendar.SUNDAY' bat dau tu ngay cn
str= c.formatmonth(2017,10,0,0)					# .formatmonth(<year>,<month>,<width>,<height>)
print "calendar:\n", str

''' Tao lich dinh dang HTML '''
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2017, 10)
print "\nHTML:\n", str

''' Cac ngay trong thang '''
for i in enumerate(c.itermonthdays(2017,10)):
	print i

print "\n"
''' In cac thang trong 1 nam , cac thu trong 1 tuan '''
for name in calendar.month_name:
	print name
print "\n"
for day in calendar.day_name:
	print day

''' Tim thu 2 dau tien trong thang '''
print "\n"
for month in range(1,13):
	# Cac tuan trong 12 thang
	mycal = calendar.monthcalendar(2017, month)
	print "Thang %d \n " %month, mycal
	# Thu 2 dau tien trong thang la ngay ?
	week1 = mycal[1]
	week2 = mycal[2]
	if week1[calendar.MONDAY] != 0:
		auditday = week1[calendar.MONDAY]
	else:
		auditday = week2[calendar.MONDAY]
	print "%s %2d\n" %(calendar.month_name[month], auditday)
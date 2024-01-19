#Gerating a Calculator
import calendar
y = int(input("Enter the year: "))
m = 1
print("\n*******CALENDAR*******")
cal = calendar.TextCalendar(calendar.SUNDAY)
#TextCalendar class is created and calendar.
#SUNDAY means that you want to start displaying the calendar from sunday.

i = 1
while i<=12:
    cal.prmonth(y,i)
    i+=1
#prmonth()


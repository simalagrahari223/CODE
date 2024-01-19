#Calendar program
import calendar
st=input("Do you want to start the program: ")
while (st.upper()=="YES"):
    year=int(input("Enter the year you want to show:"))
    month=int(input("Enter the month no. you want to show:"))
    x= calendar.month(year,month)
    print(x)














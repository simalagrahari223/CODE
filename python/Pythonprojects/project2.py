#Project 2
#Meneu Driven Program

print("Starting Python Program....")
start=input("You want to start program write 'Yes' or 'NO'= ")
while start.upper()=="YES"or "Y":
    print("\n")
    print("***************MENU DRIVEN PROGRAM*****************")
    print("NOTE=THIS CODE VAILD FOR TWO NUMBERS ONLY.")
    print("1.Addition")
    print("2.Substration")
    print("3.Division")
    print("4.Multiplication")
    print("5.SquareRoot")
    print("6.Reverse Digit Program")
    print("7.Factorial Program")
    print("8.Sum Of Digit")
    print("9.Armstrong Number")
    print("10.Palindrome Number")
    print("11.Decimal to Binary")
    print("12.Def Triangle")
    print("13.Code to Square number")
    print("14.Code to find square root of any number")
    print("15.Code to cube number")
    print("16.Code to find cube root of any number")
    print("17.Len program")
    print("18.Upper program")
    print("19.Capitalize program")
    print("20.Code to reverse string")
    print("21.Code to find upper case,")
    print("   lower case, digit case and")
    print("   total alphabets in the string")
    print("25.Program to find tax using lambda function or anonymous function")
    print("\n")
    
    choice=int(input("Enter your choice from above:"))
    rev=0
    
    if choice==1:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c=a+b
        print("Addition is:",c)
        break
        
    if choice==2:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        if a>b:
            c=a-b
            print("Substration is:",c)
            break
        if b>a:
            c=b-a
            print("Substration is:",c)
            break
        else:
            print("Substration is:","0")
            break
        
    if choice==3:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c=a/b
        print("Division is:",c)
        break
    
    if choice==4:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c=a*b
        print("Multiplication is:",c)
        break
    
    if choice==5:
        num=int(input("Enter the no. you want squareroot:"))
        num1=num**(1/2)
        print("SquareRoot of",num,"is:",num1)
        break
    
    if choice==6:  # code to reverse digit
        num= int(input(" Enter the number :"))
        while num>0:
            rem= num%10
            rev= rev*10+rem
            num= num //10
        print("Your reverse digit :", rev)
        break
    
    if choice==7:  # Factorial code
         fact=1
         num=int(input("Enter any number:"))
         while num>0:
            fact=fact*num
            num=num-1
         print("Factorial of given number is : ",fact)
         break
     
    if choice==8: # sum code
         sum=0
         num=int(input("Enter any digits number:"))
         while num>0:
            rem= num%10
            sum=sum+rem
            num=num//10
         print("Sum of digits:", sum)
         break
     
    if choice==9:# Armstrong number code
        num= int(input("Enter any 3-digit number:"))
        sum=0
        f= num
        while (f>0):
            a= f%10
            f= f//10
            sum= sum+(a**3)
            if (sum==num):
                print(num,"is armstrong number.")
            else:
                print(num,"is not armstrong number.")
                
    if choice==10:# Palindrome number code
        org= int(input("Enter the number:"))
        num= org
        rev=0
        while num>0:
            digit= num%10
            rev= rev*10+digit
            num= num//10
            if org== rev:
                print("Palindrome")
            else:
                print("Not palindrome")
                
    if choice==11: # Code to convert in binary
        n= int(input("Enter any number to convert in binary:"))
        a= 0
        m= 0
        c= 1
        while n>0:
            n=  n//2
            a= n%2
            m= m+(a*c)
            c= c*10
        print(m)
        
    if choice==12: # Code to print triangle
        def triangle():
            print('*')
            print('**')
            print('***')
            print('****')
            print('*****')
            print('******')
            print('*******')
        triangle()
        
    if choice==13:
        num=int(input("Enter any number:"))
        print(" Your number  square is:", num**2)
        
    if choice==14:
        num=int(input("Enter any number:"))
        print("Your number square root is:",int(num**0.5))
    
    if choice==15:
        num=int(input("Enter any number:"))
        print(" Your number cube  is:", num**3)
        
    if choice ==16:
        num=int(input("Enter any number:"))
        print(" Your number cube root  is:",int( num**0.34) )
    
    if choice ==17:
        name= input("Enter anything from here:")
        print("length is:",len(name))
        
    if choice ==18:
        str1=input("Enter your name:")
        print( str1.upper())
        
    if choice ==19:
        str=input("Enter your name:")
        print( str.capitalize())
        
    if choice ==20:
        str=input("Enter any string:") #Code to reverse string
        for i in range(-1,-len(str)-1,-1):
            print(str[i], end='')
            
    if choice ==21:
        str= input("Enter any string:")
        l=0
        u=0
        d=0
        total=0
        length= len (str)
        for i in range(length):
            if str[i].islower():
                l+=1
            if str[i].isupper():
                u+=1
            if str[i].isdigit():
                d+=1
            if str[i].isalpha():
                total+=1
        print("String in lower case are:",l)
        print("String in upper case are:",u)
        print("Total digits are:",d)
        print("Total alphabets are:",total)

    if choice==22:
        import keyword
        print(keyword.kwlist)

    if choice==23:
        list1=["ram","vishal","harsh","simal"]
        for i in list1:
            if len(i)==5:
                print(i)
                
    if choice==24:
        list1=[]
        n= int(input("Enter the limit of the element :"))
        for i  in range (n):
            a=input("Enter the element :")
            list1.append(a)
        print(list1)
    
    if choice==25:
        tax = lambda salary: salary * 20/100
        salary = int(input("Please Enter your salary: "))
        print("Tax to be paid is:",tax(salary))
    else:
        print("Invaild Choice")




                  
                        












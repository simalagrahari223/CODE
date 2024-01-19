#Project 1
#Python program to make a "faulty calculator".
#Design a calculator which will correctly solve all the problems except "+" ,"-" ,"/" and "*".

while True:
    print("Choices Are Listed Below:")
    print("1.Addition")
    print("2.Substration")
    print("3.Division")
    print("4.Multiplication")
    print("5.SquareRoot")
    print("6.To Check Armstrong Number")
    print("7.To Check Palindrome Number")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c=a+b+3
        print("Addition is:",c)
        break
        
    if choice==2:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        if a>b:
            c=a-b-2
            print("Substration is:",c)
            break
        if b>a:
            c=b-a+1
            print("Substration is:",c)
            break
        else:
            print("Substration is:","1")
            break
        
    if choice==3:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c=a/b-2
        print("Division is:",c)
        break
    
    if choice==4:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c=a*b*2
        print("Multiplication is:",c)
        break
    
    if choice==5:
        num=int(input("Enter the no. you want squareroot:"))
        num1=num**(1/2)
        print("SquareRoot of",num,"is:",num1)
        break
    
    if choice==6:# Armstrong number code
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
                
    if choice==7:# Palindrome number code
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
    else:
        print("You choose invaild choice.")
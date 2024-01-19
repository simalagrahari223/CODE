#Stack Program

#Program 1- WAP to implementation of list as stack
stack=[]
c='y'
while (c.upper()=='Y'):
    print("\n")
    print("1:PUSH")
    print("2:POP")
    print("3:DISPLAY")
    choice=int(input("Enter your choice:"))
    if choice==1:
        elem=input("Enter Any Number:")
        stack.append(elem)
        print("Successfully Append")
    
    elif choice==2:
        if len(stack)==0:
            print("Empty stack")
        else:
            print("Deleted Element is :",stack.pop())
    elif choice==3:
        l=len(stack)
        for i in range(l-1,-1,-1):
            print(stack[i])
    
    else:
        print("Invaild Choice")
    
    c=input("You want to continue Yes:Y and No:N -:")       
        
        
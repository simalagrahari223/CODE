# Project 4
# Printing Pattern

print("~ Welcome To Printing Pattern Program ~")
i= int(input("Enter the limit of '*' you have to print: "))
Boolean= int(input("Take number as '0' or '1': "))
while True:
    if Boolean== 0:
        print("`Boolean is false`")
        while i>=0:     
            j= 1
            while j<=i: 
                print("*", end=' ')
                j=j+1   
            print()
            i=i-1        
        
    elif Boolean== 1:
        print("`Boolean is True`")
        n=i
        for k in range(n):
            for l in range(k+1):
                print("*", end=' ')
            print()    

    else:
        print("`Out of the question`")























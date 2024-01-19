#Project 3
#Guess The Number.
#Guess the no from 1 to 100.

num=35
print("\n")
print("\t"*5 ,"<--Welcome To Guess The Number Program-->")
print("Instructions~")
print("1.You have 3 chance to guess the correct number")
print("2.You have to guess the num form 1 to 100")
print("Starting Program...")
l=3
for i in range(l):
    guessNum=int(input("Guess the Number: "))
    if num>guessNum:
        print("Little Bit Closer...")
        print("Increse the number, Come on you guess it.")
        l=l-1
        print("Number of guesses left =",l)
            
    elif num<guessNum:
        print("Little Bit Closer...")
        print("Reduce the number, Come on you guess it.")
        l=l-1
        print("Number of guesses left =",l)
        
    elif num==guessNum:
        print("*Wow!,You Found It*",)
        print("*You Win*") 
        break
    
    else: 
        print("Please enter the number from 1 to 100.")
            
print("Number of guesses left = 0")
print("/Game Over/")
        



















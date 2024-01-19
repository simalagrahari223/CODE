#Recursion Programs
#Recursion is one of the most powerful tools used in a programming language. It is a function calling itself again and again.

#program1
def recurSum(n):
    if n>1:
        return n
    else:
        return(n + recurSum(n-1)) 
    
#program2
def power(x,n):
    if n==0:
        return 1
    else:
        return (x * power(x,n-1))

#program3
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

#program3
def fact(n):
    if n== 1:
        return n
    else:
        return n * fact(n-1)















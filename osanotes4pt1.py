#recursion
#what is recursion- method that calls itselt in python
#calculate factorial
# examply 4! = 1 * 2 * 3 * 4
#loop to calculate the factorial of a number

def loop_factorial(n):
    
    #initializer
    factorial = 1

    for number in range(1, n+1):
        factorial = factorial * number
    return factorial

def recur_fact(n):
    #base case
    if n == 0:
        
        #n! =1
        return 1

    #recursive case
    else:
        return recur_fact(n-1) * n
    
#the fibonacci series sequence
#give a positive integer n
# your function should return n-th number in the sequence
def fib(n):
    f0 = 0
    f1 = 1
    #while loop version
    while(True):
         fib = f0 + f1
         f0 = f1
         f1 = fib
         
    return fib

def fib(n):
    f0 = 0
    f1 = 1

    #for loop version
    for term in range(3,n+1):

        fib = f0 + f1
        f0 = f1
        f1 = fib
    return fib

def recur_fib(n):

    #base cases
    if n ==1:
        return 0
    elif n==2:
        return 1
    else: return recur_fib(n-1) + recur_fib(n-2)

#class problem 1 recursive function that calculares teh sum of numbers
#problem 2 two function accepts two arguments into parallel
#x and y hold positive nonzero intergers.the function should return the value
#of x times y
#problem 3 recurseive fucntion that finds the largest element in a list

#problem 1 sum = 1+2+3+4+5
def loop_sum(n):
    total = 0

    for number in range(1,n+1):
        total = total = number

    return total

ans = loop_sum(100)

#problem 1 recursive version
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return recursive_sum(n-1) + n
ans2 = recursive_sum(100)

#problem 2
def loop_multi(x,y):
    #initial value
    ans = 0

    #for loop for times in the range
    for times in range(x):
        
        ans += y
        
    return ans

#problem 2 recursion
def recursion_multi(x,y):

    #loop
    if x == 0:
        return y
    else:
        return recursive_multi(x-1,y) + y

#problem three recursive
numbers = [1,30,50,70,80,103,-56,67]

   
        
        



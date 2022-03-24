#osa notes 5
#factorial

#loop to calculate the factorial of a number
def loop_factorial(n):
    #initial number
    factorial = 1

    #for loop for runs
    for number in range(1,n+1):
        
        #this makes it so when one number is in it multiplies then ups the next
        #number/iteration
       factorial = factorial * number
    return factorial

#define the name of the function
def recur_fact(n):
    #set the conditonal statment equal to 0 for base and should return 1
    #factorial rule return 1
    
    if n == 0:
        return 1 #rule
    
    #Then return and call the funciton by calling it also recursive case
    else:
        return recur_fact(n-1) * n

#fibonacci sequence is a series of numbers where a number is found by adding up two numbers before it
#starting up with 0 an 1, the sequence goes 0,1,2,3,5,8,12,21,34, and so forth
#the written rule is expression x(n) = xn-1 + xn-2

#fibinancci sequence
# given a positive integer n
#your function should return n-th number in the sequence

def loop_fib(n):

    f0 = 0
    f1 = 1
    while(True):
        fib = f0 + f1
        f0 = f1
        f1 = fib

    return fib

#another form of the sequence
def loop_fib1(n):

    f0 = 0
    f1 = 1
    for term in range(3,n+1):
        fib = f0 + f1
        f0 = f1
        f1 = fib

    return fib

#iterative solution
def recur_fib(n):

    #conditonal statement
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recur_fib(n-1) + recur_fib(n-2)

#write recursion function calculating the sum of number 1 through 100
#starts at the bottom with nothing hence the for loop
def sum_num(n):
    
    #first initialize with variable starting at 0
    total = 0

    #use a for loop for each iteration
    for num in range(1,n+1):
        total = total + num

    #return statement for the end
    return total

ans = sum_num(100)

#recursion verion
#write recursion function calculating the sum of number 1 through 100
def sum_num2(n):
    #no initializer just condiontal statement
    #the first if should return 0 since were starting backwards reducing the number
    if n == 0:
        return 0
    else:
        return sum_num(n-1) + n
    
ans2 = sum_num2(100)

#problem 2write the recursive function that accepts two arguements into the parameters x and y. assume x and y hold positive integer,
#the function should return the value of x times y. multiplication can be performed as repeated addition as follows:
#4*5 = 5+5+5+5

def argue_multi(x,y):
    #initializer
    ans = 0

    #loop
    for times in range(x):
        ans += y
    return ans

#the recursion verion of the problem
def argue_multi2(x,y):
    #conditional statement
    if x == 1:
        return y
    else:
        return argue_multi(x-1,y)+y

## x = []
##>>> x = list()
##>>> type(x)
##<class 'list'>
##>>> x = [3,2,1,3,4,1,6]
##>>> x = list('abcdefg')
##>>> x
##['a', 'b', 'c', 'd', 'e', 'f', 'g']
##>>> len(x)
##7
##>>> x.append("x")
##>>> x.count('b')
##1
##>>> x.extend('123')
##>>> x
##['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', '1', '2', '3']
##>>> x.append('c')
##>>> x
##['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', '1', '2', '3', 'c']
##>>> x.index('c')
##2
##>>> x.insert(4,'apple')
##>>> x
##['a', 'b', 'c', 'd', 'apple', 'e', 'f', 'g', 'x', '1', '2', '3', 'c']
##>>> x.pop()
##'c'
##>>> y = [1,2,3,4,5,6,7,8,9]
##>>> y.remove(3)
##>>> y
##[1, 2, 4, 5, 6, 7, 8, 9]
##>>> y.sort()
##>>> y
##[1, 2, 4, 5, 6, 7, 8, 9]
##>>> x = list("bajfebfeidwoqfwberow")
##>>> x
##['b', 'a', 'j', 'f', 'e', 'b', 'f', 'e', 'i', 'd', 'w', 'o', 'q', 'f', 'w', 'b', 'e', 'r', 'o', 'w']
##>>> 

#size() returns the number of elements in a list


    
    
    


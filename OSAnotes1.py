#identifier
#what is an indentifier?
#everything can name
#naming rules?
#My_Student_Record
#myStudentRecord

# this program
#x = 10

#""""
#this program
#calculates
#the sum of three
#numbers
#""""

# int(100.99)
# this above should kick out 100
# since these are numbers it requires int or float

#int('100')
#this above should kick out 100.0

#float(100)
#this above should kick out 100.0

#float("100.99")
#100.99

#int("apple")
#this does not kick out anything

# str(100)
# this kicks out = '100'

# str(100.99)
# this kicks out = '100.99'

#bool(0)
# this kicks out = False

#bool(1)
# this kicks out = True

# bool(0.0)
# this kicks out = False

# bool(1.0)
# this kicks out = True

#bool("1")
# True

#bool("0")
# True

#bool("")
#False

#bool("asdfghjl")
#True

#bool([1,2,3,4,5,6])
#True

#bool([])
#False

if( 3 > 5):
    print("1")
    print("2")
    print("3")

if(10 > 5):
    #statement
    #statement
    #statement
    print("true")
else:
    #statement
    #statement
    #statement
    print("false")

#problem 1 get five numbers and dins the negative ones
a,b,c,d,e = 1,-1,2,-2,3

if(a<0):
    print(a)
if(b < 0):
    print(b)
if(c < 0):
    print(c)
if(d < 0):
    print(d)
if(e < 0):
    print(e)

Max = -float('inf')
if a > Max:
    Max = a
elif b > Max:
    Max = b
elif c > Max:
    Max = c
elif d > Max:
    Max = d
elif e > Max:
    Max = e

x = 6
while x < 10:
    print(x)
    x += 2

#initial value
x = 0
#conditonal statement
while True:
    print(x)
    x += 1
    if x >= 10:
        break

#for loop
for x in "abcedfghi":
    print(x)

for x in [1,2,3,4,5]:
    print(x)

for x in range(1,10):
    print(x)

for x in [1,2,3,4,5]:
    if x == 3:
        break
    print(x)
    #break will stop and terminate the program and the rest 
    
for x in [1,2,3,4,5]:
    if x == 3:
        continue
    print(x)

#functions
def display_info():
    
    print("alex")
    print("emily")
    
display_info()

a = "apple"
#new fucntion
def function1():
    global x
    x = 10#inside the function this is a local variable
    print(x)
    
fucntion1()
print(a)

def function2():
    y = 20 #local variable in function2
    def function3():
        nonlocal y 
        y = "banana"#local variable in function3
        print(y)
    function3()
    print(y)
        
function2()

#functions with parameters/local variables a,b,c
def calc_sum(a,b,c):
    print(a+B+c)

calc_sum(10,20,30)

def test9(a,b,c,d,e):
    print(a+b+c+d+e)

    return a,b,c,d,e

test(e=1,b=2,c=3,a=4,d=5)

test(1,2,d=3,e=5,c=4)

#import the random
import random
from random import randint
from random as r
x = r.randint(1,20)

def calculate_sum(x,y):

    return x + y

s = calculate_sum(10,20)



    
    
    
    
    


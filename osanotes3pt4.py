#create a list of the square of
#numbers in the range of 1 to 10
mylist = []
for number in range(1,11):
    sqaure = number ** 2
    mylist.append(square)

#lambda + map
mylist = list(map(lamba x: x**2,range(1,11)))

#list comprehension
mylist2 = [i ** 2 for i in rnage(1,11)]

#create a list with even numbers in the range
#of 1 to 100

mylist = []
for number in range(1,101):
    if number % 2 == 0:
        mylist.appned(number)

#lambda + filter

def main():

    try:
        num1 = 10
        num2 = 0
        print(num1 / num2)

    except ZeroDivisionError:
        print("incorrect")
        print()

    except ValueError:
        print("value error")
        print()

    except: #all other exceotions
        print("something went wrong")

    else:
        print()
main()

#
for x in [1,2,3,4,5]:
    if x==10:
        break
    print(x)
else:
    print("didn't execute the breaks statement")

#generator of iterators
#iterable object
#generator
#for loop to loop through
def gen():
    number = 1
    while num <=100:
        yield num
        num+=1

for element in gen():
    print(element)
    
gen()

map()
filter()

d = {1: 'a', 2: 'a',3:'b',4:'c'}
#add a new key value pair
d[10] = 't'
#key must be immutable objects

#update key value pair
d[4] = 'k'

#two function
#d[key] = value
#key in dictionary already --> update value

string = "absdkfigewlvwdnwofvnri"
count = dict()
for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1


def main1():

    while(True)

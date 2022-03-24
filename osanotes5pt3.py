#Torian Dawkins

#methods for a stack
#size() returns the number of elements in a stack
#is_empty() returns a boolean indication wheather the stack is empty
#top() returns the top element of the stack, without removing it or null if the stack is empty
#push(e) adds element e to the top of the stack
#pop() removes and returns the top element from the stack or null if the stack is empty

#implemention

#stack method   -----    linked list method
#size()        function    size()
#is_empty()                is_empty()
#top()                     first()
#push(e)                   add_first(e)
#pop()                     remove_first()

#look at code and refer to the notes above
#this creates a stack 
from linkedlist2 import LinkedList

#create the class
class LinkedStack:

    def __init__(self):

        #Underlying linked list data structure
        #This brings the mthods from another set of code(linkedlist2) in to use
        #Their function
        self.__stack = LinkedList()

    #implement method
    #size() returns the number of elements in a stack
    def size(self):
        return self.__stack.size()

    #is_empty() returns a boolean indication wheather the stack is empty
    def is_empty(self):
        return self.__stack.is_empty()
    
    #top() returns the top element of the stack, without removing it or null if the stack is empty
    def top(self):
        return self.__stack.first()
    
    #push(e) adds element e to the top of the stack
    def push(self,e):
        self.__stack.add_first(e)

    #pop() removes and returns the top element from the stack or null if the stack is empty
    def pop(self):
        return self.__stack.remove_first()
    
    #create a string method of this
    def __str__(self):
        return self.__stack.__str__()

#test of stack
#create a instance of the stack
#create a variable then equal it to the class name 
linked_stack = LinkedStack()

for i in range(1,5):
    linked_stack.push(i)
    print(linked_stack)

#video left off is 00:35:06
#list in python = array list in java = vector in c++
#dynamic array
#

for i in range(5):
    print("remove element",linked_stack.pop())
    print(linked_stack)

#creating a stack using a list
class liststack:

    def __init__(self):
        #underlying data structure is a list

        self.__stack = list()

        #return the length of the list 
        def size(self):
            return len(self.__stack)

        #if the list is empty and has nothing 
        def is_empty(self):
            return len(self.__stack) == 0

        def top(self):
            if self.is_empty():
                return None
            return self.__stack[-1]

        def push(self,e):
            self.__stack.append(e)

        def pop(self):
            if self.is_empty():
                return None
            return self.__stack.pop()

        def __str__(self):
            print(self.__stack)
            ans = "("
            for e in range(len(self.__stack),-1,-1):
                ans += str(e) + ','
            ans = ans.rstrip(', ')
            ans += ")"
            return str(self.__stack()

list_stack = liststack()

for i in [1,2,3,4,5,6,7]:
    list_stack.push(i)
#video 1:03:30
        
    
    

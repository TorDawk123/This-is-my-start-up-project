#osanotes5pt4

#dequeue(): removes and returns the first element from the queue or null if the queue is empty
#size() returns the number of elements in a queue
#is_empty() returns a boolean indicating whether the queue is empty
#first() returns the first element of the queue, without removing it or null if the queue is empty
#enqueue(e) adds element e to the back of queue
#dequeue() removes and returns the first element from the queue or null if the queue is empty

#queue method   function   linked list method
# size()                   size()
#is_empty()                is_empty()
#first()                   first()
#enqueue(e)                add_last(e)
#dequeue()                 remove_first()

#loook at these notes above to see what each functions purpose is
#this creates a queue

from linkedlist2 import LinkedList

class LinkedQueue:

    def __init__(self):
        
        #the data structure
        #this is what brings them together from the linked list
        self.__queue = LinkedList()

    #creating methods and implementing them
    #returns the number of elements
    def size(self):
        return self.__queue.size()

    def is_empty(self):
        return self.__queue.is_empty()
    
    #returns the first element of the queue, without removing it or null if the queue is empty
    def first(self):
        return self.__queue.first()

    #adds element e to the back of the queue 
    def enqueue(self,e):
        return self.__queue.add_last(e)
        
    #dequeue removes and returns first element from the queue or null if the
    #queue is empty
    def dequeue(self):
        return self.__queue.remove_first()


#creating the queue using a list
#01:24:30
class linkedqueue:

    def __init__(self):

        #underlying data structure is a list
        self.__queue = list()

        #return the length of a list
        def size(self):
            return len(self.__queue)

        #if the list is empty
        def is_empty(self):
            return len(self.__queue) == 0

        #first
        def first(self):
            if self.is_empty():
                return None
            return self.__queue[0]

        #append
        def enqueue(e):
            self.__queue.append(e)

        def dequeue():
            if self.is_empty():
                return None
            return self.__queue.pop()

        

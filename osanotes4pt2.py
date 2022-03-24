#osa notes pt2

class Node:

    def __init__(self, element=None):

        #element
        self.__element = element

        #reference node
        self.__next = None

    #get/set method
    def get_element(self):
        return self.__element

    def set_element(self,element):
        self.__element = element

    #get and set of next
    def get_next(self):
        return self.__next

    def set_next(self,next):
        self.__next = next

class linkedlist:

    def __init__(self):

        #head
        self.__head = None

        #tail
        self.__tail = None

        #keep track of size of length lst
        self.__size = 0

    #how to implement the size?
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.__size == 0:
            return None
        return self.__head.get_element()

    def last(self):
        if self.__size == 0:
            return None
        return self.__tail.get_element()
    
    def add_first(self,element):
        #create a node
        newest = Node()
        #insert element into this node
        newest.set_elemtn(element)

        #have newest point at head
        newest.set_next(self.__head)

        #update the head
        self.__head = newest

        #handle if link list is empty, tail=newest
        if self.__size == 0:
            self.__tail = newest

        #update the size
        self.__size += 1
        return

    def add_last(self):
        return

    def remove_first(self):
        return

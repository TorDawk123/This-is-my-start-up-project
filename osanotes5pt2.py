#osanotes5pt2
#singly linked list

class Node:

    def __init__(self,element=None):
        
        #two data attributes
        #elements
        self.__element = element

        #reference to next node
        self.__next = None

        self.__prev = None

    #get method and set method for element
    def get_element(self):
        return self.__element

    def set_element(self,element):
        self.__element = element

    #get method and set method for next
    def get_next(self):
        return self.__next

    def set_next(self,nxt):
        self.__next = nxt
    #get and set method for perv
    def get_prev(self):
        return self.__prev

    def set_prev(self,prv):
        self.__prev = prv

#create a node
node1 = Node(10)
node2 = Node()
node3 = Node(100)

#single linked list 
#how to link them together
#node1 ---> node2
#node2 is node1.get_next()
#node3 is node2.get_next()
#node3 is node1.get_next().get_next()
node1.set_next(node2)

#how to link node1 --> node2 --> node3
node2.set_next(node3)

#next class to link them together
class linkedlist:

    def __init__(self):

        #head
        self.__head = None
        
        #tail
        self.__tail = None

        #size
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.__head is None:#return none
            return None
        return self.__head.get_element()

    def last(self):
        if self.__tail is None:
            return None
        return self.__tail.get_element()

    def add_first(self,e):
        
        #create a node
        newest = Node()

        #insert element into this node
        newest.set_element(e)

        #have newest point at head
        newest.set_next(self.__head)

        #update the head,update the size
        self.__head = newest

        #handle special case,if empty,tail = newest
        if self.__size == 0:
            self.__tail = self.__head
        self.__size += 1
        
        return

    def add_last(self,e):

        #create a node
        newest = Node()

        #set element to e
        newest.set_element(e)

        #have this node point to None
        newest.set_next(None)

        #special case,if empty, head is also tail
        if self.__size == 0:
            self.__head = newest
        else:
            self.__tail.set_next(newest)

        #update the tail
        self.__tail = newest

        #update size
        self.__size += 1
        

    def remove_first(self):
        #special case, if empty,remove nothing
        if self.__size == 0:
            return self.__head

        #get the head elements
        ans = self.__head.get_element()

        #the second node becomes the new head
        self.__head = slef.__head.get_next()

        #update the size
        self._size -= 1

        #if size becomes 0, this is also the tail
        if self.__size == 0:
            self.__tail == None
        return ans

    def __str__(self):

        #traverse the linked list
        ans = '('
        cursor = self.__head
        while cursor:
            
            ans += str(cursor.get_element()) + ' , '

            cursor = cursor.get_next()

        ans = ans.rstrip(' , ')
        ans += ')'

    def __iter__(self):
        
        #traverse the linked list
        cursor = self.__head
        while cursor is not None:
            yield cursor.get_element()
            cursor = cursor.get_next()

    #exercise add method that contain specified element, false otherwise
    def contains(self,e):
        #traverse the linked list
        #compare each element with e
        # if we can find a match,return true
        cursor = self.__head
        while cursor is not None:
            if cursor.get_element() == e:
                return True
            cursor = cursor.get_next()
        return False

    def get_head(self):
        if self.__size == 0:
            return None
        return self.__head
        

    def get_tail(self):
        if self.__size == 0:
            return None
        return self.__tail

    def set_head(self,n):
        # if the list is empty
        if self__size == 0:
            self.__head = n
            self.__tail = n
            self.__size += 1
        else:
            #have n point at the next node of the head
            next_head = self.__head.get_next()
            n.set_next(next_head)
            #get the old head
            #make it point at itself
            old_head = self.__head
            old_head.set_next(old_head)
            
            #update the head
            self.__head = n

    def add_after(self,e,p):
        #special case if p is the tail
        # = add_last(e)
        if p is self.__tail(e):
            self.add_last(e)
            return
        #create a node
        new_node = node(e)

        #find the next node of p: s
        s = p.get_next()

        #have p point at new node
        p.set_next(new_node)

        #have the new node point at s
        new_node.set_next(s)

        #update the size
        self.__size += 1

    def add_before(self,e,s):
        #special case:if s is the head
        # = add_first
        if s is self.__head:
            self.add_first(e)
            return
        #regular case
        #create a node
        new_node = Node(e)

        #find the previous node of s:p
        cursor = self.__head
        while cursor.get_next() is not s:
            cursor = cursor.get_next()
        #when the cursor stops
        p = cursor
        #make p point at new node
        p.set_next(new_node)
        
        #have new node point at s
        new_node.set_next(s)
        
        #update the size
        self.__size += 1

    #example hw problem 3
    #minute mark 1:19:35
    def remove(self,n):
        pass

    def swap_head_tail(self):
        pass
#s = 'a'---> 'c' --> 'd'
def join(s):
    for letter is s:


    
        



if __name__ == '__main__':
    #create a linked list
    
    linked_list = linkedlist()

    for number in range(6):
        linked_list.add_first(number)
        #print(linked_list)
    for number in range(6,11):
        linked_list.add_last(number)
        #print(linked_list)
    flag1 = linked_list.contains(7)
    flag2 = linked_list.contains(20)

    #create a node
    node1 = Node(100)
    node1.set_element(100)
    linked_list.set_head(node1)
    print(linked_list)
    #expected result (5,4,3,2,1,0)
    
##    for i in range(10):
##        linked_list.add_first(i)
##        linked_list.add_last(i)
##        print(linked_list)
##
##    for e in linked_list:
##        print(e)
##
##    for i in range(11):
##        linked_list.remove_first()
##        print(linked_list)
##
##    for i in range(5):
##        linked_list.add_last(i)
##        print(linked_list)
##    print(linked_list.size())
        
            

    

    
        

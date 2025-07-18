# In this problem, you will implement two classes according to the specification below: one Container class and one Queue class (a subclass of Container).     

# Our Container class will initialize an empty list. 
# The two methods we will have are to calculate the size of the list and to add an element. 
# The second method will be inherited by the subclass. 
# We now want to create a subclass so that we can add more functionality – the ability to remove elements from the list. 
# A Queue will add elements to the list in the same way, but will behave differently when removing an element.

# A queue is a first-in, first-out data structure. Think of a store checkout queue. 
# The customer who has been in the line the longest gets the next available cashier. 
# When implementing your Queue class, you will have to think about which end of your list contains the element that has been in the list the longest. 
# This is the element you will want to remove and return.

class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self.myList.append(elem)

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        if(self.size() > 0):
            return self.myList.pop(0)
        else:
            return None

#TESTS
c = Container()
q = Queue()

print(c.size())
print(q.size())

c.add(1)
c.add(2)
c.add(3)

q.add(4)
q.add(5)
q.add(6)

print('c size' ,c.size())
print('q size' ,q.size())

print('c list' ,c.myList)
print('q list' ,q.myList)

print('q removal',q.remove())
print('q list' ,q.myList)       
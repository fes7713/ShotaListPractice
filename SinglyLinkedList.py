from List import List
from Node import Node


class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.size = 0
        return

    # Create new node: done
    # Search for the last node
    # Change the next node of the last node to the created node
    def add(self, data):
        #cretae new node
        self.new_node = Node(data)
        #if head != none: which means not empty, new_node become as head
        if self.head is None:
            self.head = self.new_node
        # Search for the last node
        #last_node = self.head
        # Change the next node of the last node to the created node
       # last_node = next(self.head)
        return

    # Insert data to the index
    # Create new node and insert to the middle of the nodes
    def insert(self, index, data):
        if self.head is None:
            self.head = Node(index, data, None)
        return

    # Search for data in array and remove node
    def remove(self, data):
        return

    # Return true when size is zero
    # Otherwise false
    def isEmpty(self)-> bool:
        if self.head == None:
            return True

        return False

    # Return current size
    def size(self)-> int:
        return len(int(self.size))

    # Return array that represents the list
    def toArray(self):
        return self.head

    # Print inside of array
    # Call toArray inside this function to print it
    # No need to change it
    def print(self):
        print(self.toArray())
        return



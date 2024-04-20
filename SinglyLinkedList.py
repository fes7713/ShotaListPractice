from List import List


class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.size = 0
        return

    # Create new node: if self.head is none, create new node
    # Search for the last node
    # Change the next node of the last node to the created node
    def add(self, data):
        #create new node
        node = Node(data, None)

        # List is empty
        if self.head is None:
            self.head = node
            self.size = self.size + 1
            return

        current_node = self.head
        while True:
            if current_node.getNextNode() is None:
    #intput new node
                current_node.changeNextNode(node)
                break
            current_node = current_node.changeNextNode

        return
    #for commit
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



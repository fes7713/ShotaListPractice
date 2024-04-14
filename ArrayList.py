from List import List


class ArrayList(List):
    def __int__(self):
        super.__init__()
        self.array = []
        self.size = 0
        return

    # Add data to array
    def add(self, data):
        return

    # Insert data to the index
    # Make sure to shift datas
    def insert(self, index, data):
        return

    # Search for data in array and remove data
    # Make sure to shift all the gaps
    def remove(self, data):
        return

    # Return true when size is zero
    # Otherwise false
    def isEmpty(self)-> bool:
        return False

    # Return current size
    def size(self)-> int:
        return 0

    # Return array that represents the list
    def toArray(self):
        return []

    # Print inside of array
    # Call toArray inside this function to print it
    # No need to change it
    def print(self):
        print(self.toArray())
        return



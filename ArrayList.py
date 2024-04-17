from List import List


class ArrayList(List):
    def __init__(self):
        self.array = []
        self.size = 0
        return

    # Add data to array
    def add(self, data):
        self.array.append(data)
        return

    # Insert data to the index
    # Make sure to shift datas
    def insert(self, index, data):
        # if index < 0 or index > self.size:
        #     print("Error size")

        # else:
        #     self.array.insert(index, data)
        #     self.size +=1
        # for i in range(self.size - 1, index, -1):
        #     self.array[i] = self.array[i - 1]
        # self.array[index] = data


        return self.size

    # Search for data in array and remove data
    # Make sure to shift all the gaps
    def remove(self, data):
        self.array.remove(data)

        return

    # Return true when size is zero
    # Otherwise false
    def isEmpty(self)-> bool:
        return len(self.array) == 0

    # Return current size
    def size(self)-> int:

        return len(self.size)

    # Return array that represents the list
    def toArray(self):
        return self.array

    # Print inside of array
    # Call toArray inside this function to print it
    # No need to change it
    def print(self):
        print(self.toArray())
        return



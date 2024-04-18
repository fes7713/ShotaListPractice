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
        self.array.insert(index, data)
        # else:
        #     self.array.insert(index, data)
        #     self.size +=1
        save_value = self.array[-1]

        # 配列の後ろから2番目の要素から順に後ろの要素に値をコピー
        for i in range(len(self.array) - 2, -1, -1):
            self.array[i]

        # 一時的に保存した値を配列の先頭に挿入
        self.array[-1] = save_value

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



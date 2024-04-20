class Node():
    def __init__(self, data: object, next_node: object) -> object:
        self.next_node = next_node
        self.data = data

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.next_node

    def changeNextNode(self, node):
        self.next_node = node
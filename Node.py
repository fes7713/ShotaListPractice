class Node():
    def __init__(self, data: object, next_node: object) -> object:
        self.next_node = next_node
        self.data = data


        node_head = None
        node_a = next_node
        node_b = next_node
        node_c = next_node
        node_d = next_node
        node_e = next_node
        node_f = next_node

        head = node_a
        node_a.changeNextNode = node_b
        node_b.changeNextNode = node_c
        node_d.changeNextNode = node_e
        node_e.changeNextNode = node_f
        node_f.changeNextNode = None

        node_result = head
        while True:
            if node_result.changeNextNode is None:
                break
            node_result = node_result.changeNextNode
        #for i in range(2):
        #    result = result.changeNextNode

        #return result



    def getData(self):
        return None

    def getNextNode(self):
        return None

    def changeNextNode(self, node):
        return
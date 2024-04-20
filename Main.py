from ArrayList import ArrayList
from List import List
from SinglyLinkedList import SinglyLinkedList


def test_array_list():
    arrayList: List = ArrayList()
    # True
    print(arrayList.isEmpty())

    arrayList.add(1)
    # False
    print(arrayList.isEmpty())
    arrayList.add(2)
    arrayList.add(3)
    arrayList.add(4)
    arrayList.add(5)
    arrayList.add(6)

    # [1, 2, 3, 4, 5, 6]
    arrayList.print()

    # 6
    print(arrayList.getSize())

    arrayList.remove(3)
    arrayList.remove(4)

    # [1, 2, 5, 6]
    arrayList.print()

    arrayList.insert(1, 7)

    # [1, 7, 2, 5, 6]
    arrayList.print()


def test_linked_list():
    linkedList: List = SinglyLinkedList()
    # True
    print(linkedList.isEmpty())

    linkedList.add(1)
    # False
    print(linkedList.isEmpty())
    linkedList.add(2)
    linkedList.add(3)
    linkedList.add(4)
    linkedList.add(5)
    linkedList.add(6)

    # [1, 2, 3, 4, 5, 6]
    linkedList.print()

    print(linkedList.getNode(2).getData())
    # 6
    print(linkedList.getSize())

    linkedList.remove(3)
    linkedList.remove(4)

    # [1, 2, 5, 6]
    linkedList.print()

    linkedList.insert(1, 7)

    # [1, 7, 2, 5, 6]
    linkedList.print()


if __name__ == "__main__":
    print("=== Array List ====")
    test_array_list()
    print("\n\n=== Linked List ====")
    test_linked_list()
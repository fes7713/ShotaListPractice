import unittest

from SinglyLinkedList import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def test_isEmpty(self):
        list = SinglyLinkedList()
        self.assertEqual(True, list.isEmpty())  # add assertion here
        list.add(1)
        self.assertEqual(False, list.isEmpty())  # add assertion here
        list.remove(1)
        self.assertEqual(True, list.isEmpty())  # add assertion here

    def test_add(self):
        self.assertEqual(True, False)  # add assertion here

    def test_insert(self):
        self.assertEqual(True, False)  # add assertion here

    def test_remove(self):
        self.assertEqual(True, False)  # add assertion here

    def test_size(self):
        self.assertEqual(True, False)  # add assertion here

    def test_toArray(self):
        self.assertEqual(True, False)  # add assertion here

    def test_print(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

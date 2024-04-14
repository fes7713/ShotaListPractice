import unittest

from ArrayList import ArrayList


class MyTestCase(unittest.TestCase):
    def test_isEmpty(self):
        list = ArrayList()
        self.assertEqual(True, list.isEmpty())  # add assertion here
        list.add(1)
        self.assertEqual(False, list.isEmpty())  # add assertion here
        list.remove(1)
        self.assertEqual(True, list.isEmpty())  # add assertion here


if __name__ == '__main__':
    unittest.main()

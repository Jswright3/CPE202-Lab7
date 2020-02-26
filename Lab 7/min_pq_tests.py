"""CPE202
John Wright
Lab 7
"""
import unittest
from min_pq import MinPQ

class MyTest(unittest.TestCase):
    def test_insert(self):
        heap = MinPQ()
        self.assertTrue(heap.is_empty())
        heap.insert(5)
        self.assertEqual(heap.min(), 5)
        heap.insert(2)
        self.assertEqual(heap.min(), 2)
        self.assertEqual(heap.size(), 2)
        heap.insert(6)
        self.assertFalse(heap.is_empty())
        heap.insert(3)
        self.assertEqual(heap.min(), 2)
        heap.insert(1)
        self.assertEqual(heap.min(), 1)
        self.assertEqual(heap.arr, [1, 2, 6, 5, 3])
        self.assertEqual(heap.size(), 5)

    def test_del_min(self):
        heap = MinPQ()
        self.assertTrue(heap.is_empty())
        heap.insert(1)
        heap.insert(5)
        self.assertFalse(heap.is_empty())
        heap.insert(3)
        self.assertEqual(heap.del_min(), 1)
        heap.insert(4)
        heap.insert(2)
        self.assertEqual(heap.del_min(), 2)
        self.assertEqual(heap.num_items, 3)
if __name__ == '__main__':
   unittest.main()

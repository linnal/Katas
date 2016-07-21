import unittest
import LinkedQueue as lq

class TestCeaserChiper(unittest.TestCase):

    def test_init(self):
        queue = lq.LinkedQueue()
        self.assertEqual(queue.to_string(), "")

    def test_enqueue(self):
        queue = lq.LinkedQueue()
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual( queue.to_string(), "2 3 " )

    def test_dequeue(self):
    	queue = lq.LinkedQueue()
    	queue.enqueue(2)
    	queue.enqueue(3)
    	node = queue.dequeue()
    	self.assertEqual(node.value, 2)
    	self.assertEqual(queue.to_string(), "3 ")
    	node = queue.dequeue()
    	self.assertEqual(node.value, 3)
    	self.assertEqual(queue.to_string(), "")
    	self.assertRaises( Exception, queue.dequeue)

if __name__ == '__main__':
    unittest.main()

import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

   # def test2(self):
    #    expected = "failure"
     #   self.assertEqual(expected, task.firstrun())

    def test__circlearea(self):
        R1 = 0
        R2 = 2
        R3 = 100
        R4 = -5
        R5 = 10000
        # test1
        expected = 0
        self.assertEqual(expected, task.circlearea(R1))
        # test2
        expected = 4 * math.pi
        self.assertEqual(expected, task.circlearea(R2))
        # test3
        expected = 10000 * math.pi
        self.assertEqual(expected, task.circlearea(R3))
        # test4
        expected = "Invalid value for radius"
        self.assertEqual(expected, task.circlearea(R4))
        # test5
        expected = 10000**2 * math.pi
        self.assertEqual(expected, task.circlearea(R5))


if __name__ == '__main__':
    unittest.main()

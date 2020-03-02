import unittest
import task
import math
import datetime

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


    def test_firstlast(self):
        list1 = []
        list2 = [1, 2, 5, 7]
        list3 = ["help", "get", "me"]
        list4 = ['', '%', '$']
        list5 = [1, 2, 3, 4, 5, 6, 55, 7, 8, 9, -55]

        # test1
        expecteda = "The list is empty"
        self.assertEqual(expecteda, task.firstlast(list1))
        # test2
        expecteda = 1
        expectedb = 7
        returned1, returned2 = task.firstlast(list2)
        self.assertEqual(expecteda,  returned1)
        self.assertEqual(expectedb, returned2)
        # test3
        expecteda = "help"
        expectedb = "me"
        returned1, returned2 = task.firstlast(list3)
        self.assertEqual(expecteda, returned1)
        self.assertEqual(expectedb, returned2)
        # test4
        expecteda = ''
        expectedb = '$'
        returned1, returned2 = task.firstlast(list4)
        self.assertEqual(expecteda, returned1)
        self.assertEqual(expectedb, returned2)
        # test5
        expecteda = 1
        expectedb = -55
        returned1, returned2 = task.firstlast(list5)
        self.assertEqual(expecteda, returned1)
        self.assertEqual(expectedb, returned2)


    def test_datediff(self):
        # test 1
        date1 = datetime.date(2020, 5, 30)
        date2 = datetime.date(1990, 5, 30)
        expected = 10958
        self.assertEqual(expected, task.datediff(date1, date2))
        # test2
        date3 = datetime.date(2020, 5, 30)
        date4 = datetime.date(2020, 5, 30)
        expected = 0
        self.assertEqual(expected, task.datediff(date3, date4))
        # test3
        date5 = datetime.date(1200, 7, 21)
        date6 = datetime.date(2020, 5, 30)
        expected = 299447
        self.assertEqual(expected, task.datediff(date5, date6))

if __name__ == '__main__':
    unittest.main()

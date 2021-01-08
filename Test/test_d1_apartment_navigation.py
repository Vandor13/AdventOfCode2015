from unittest import TestCase
from d1_apartment_navigation import navigate


class Test1(TestCase):
    def test_navigate_1(self):
        result = navigate("(())")
        self.assertEqual(result, 0, msg="Test1: Expected 0, got {}".format(result))
        result = navigate("()()")
        self.assertEqual(result, 0, msg="Test2: Expected 0, got {}".format(result))
        result = navigate("(((")
        self.assertEqual(result, 3, msg="Test3: Expected 3, got {}".format(result))
        result = navigate("(()(()(")
        self.assertEqual(result, 3, msg="Test4: Expected 3, got {}".format(result))
        result = navigate("))(((((")
        self.assertEqual(result, 3, msg="Test5: Expected 3, got {}".format(result))
        result = navigate("())")
        self.assertEqual(result, -1, msg="Test6: Expected -1, got {}".format(result))
        result = navigate("))(")
        self.assertEqual(result, -1, msg="Test7: Expected -1, got {}".format(result))
        result = navigate(")))")
        self.assertEqual(result, -3, msg="Test8: Expected -3, got {}".format(result))
        result = navigate(")())())")
        self.assertEqual(result, -3, msg="Test9: Expected -3, got {}".format(result))









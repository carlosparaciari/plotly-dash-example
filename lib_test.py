from lib import increase, decrease
import unittest


class TestIncreaseDecrease(unittest.TestCase):

    def test_increse(self):
        self.assertEqual(increase(2), 3)

    def test_isupper(self):
        self.assertEqual(decrease(2), 1)

    def test_exception(self):

        with self.assertRaises(TypeError):
            increase('a')


if __name__ == '__main__':
    unittest.main()

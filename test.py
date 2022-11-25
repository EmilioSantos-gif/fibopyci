import unittest

import fibonacci as f


class ftest(unittest.TestCase):
    def test(self):
        self.assertEquals(f.fibonacci_of(5), 5)
        self.assertEquals(f.fibonacci_of(6), 8)
        self.assertEquals(f.fibonacci_of(7), 13)
        self.assertEquals(f.fibonacci_of(8), 21)
        #self.assertEquals(f.fibonacci_of(9), 20, "Test failed")


if __name__ == "__main__":
    unittest.main()

import unittest

import fibonacci as f


class ftest(unittest.TestCase):
    def test(self):
        self.assertEquals(f.fibonacci_of(5), 5)
        self.assertEquals(f.fibonacci_of(6), 8)
        self.assertEquals(f.fibonacci_of(7), 13)
        self.assertEquals(f.fibonacci_of(8), 21)
        

if __name__ == "__main__":
    unittest.main()

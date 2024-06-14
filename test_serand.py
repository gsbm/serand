import unittest
from serand import SecureRandom

class TestSecureRandom(unittest.TestCase):

    def setUp(self):
        self.random = SecureRandom()
        self.random.seed()

    def test_randbytes(self):
        result = self.random.randbytes(16)
        self.assertEqual(len(result), 16)
        self.assertIsInstance(result, bytes)

    def test_getrandbits(self):
        result = self.random.getrandbits(32)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 2**32)

    def test_randint(self):
        result = self.random.randint(10, 100)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 10)
        self.assertLessEqual(result, 100)

    def test_choice(self):
        seq = [1, 2, 3, 4, 5]
        result = self.random.choice(seq)
        self.assertIn(result, seq)

    def test_shuffle(self):
        seq = [1, 2, 3, 4, 5]
        original = seq[:]
        self.random.shuffle(seq)
        self.assertNotEqual(seq, original)
        self.assertCountEqual(seq, original)

    def test_sample(self):
        seq = [1, 2, 3, 4, 5]
        result = self.random.sample(seq, 3)
        self.assertEqual(len(result), 3)
        for item in result:
            self.assertIn(item, seq)

    def test_binomialvariate(self):
        result = self.random.binomialvariate(10, 0.5)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 10)

    def test_random(self):
        result = self.random.random()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)
        self.assertLess(result, 1.0)

    def test_uniform(self):
        result = self.random.uniform(0, 10)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 10.0)

    def test_triangular(self):
        result = self.random.triangular(0, 10, 5)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 10.0)

    def test_betavariate(self):
        result = self.random.betavariate(2, 5)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 1.0)

    def test_expovariate(self):
        result = self.random.expovariate(1.5)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)

    def test_gammavariate(self):
        result = self.random.gammavariate(2, 3)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)

    def test_gauss(self):
        result = self.random.gauss(0, 1)
        self.assertIsInstance(result, float)

    def test_lognormvariate(self):
        result = self.random.lognormvariate(0, 1)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)

    def test_normalvariate(self):
        result = self.random.normalvariate(0, 1)
        self.assertIsInstance(result, float)

    def test_vonmisesvariate(self):
        result = self.random.vonmisesvariate(0, 4)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)
        self.assertLessEqual(result, 2 * 3.141592653589793)

    def test_paretovariate(self):
        result = self.random.paretovariate(2)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 1.0)

    def test_weibullvariate(self):
        result = self.random.weibullvariate(1, 1.5)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()

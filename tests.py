import unittest
import transducers

class BasicTest(unittest.TestCase):
	arr = [0,1,2,3,4,5]
	comparr = [45,74,85,96]

	def test_map_filter(self):
		data = transducers.TMap(lambda x: x + 1)
		fil = transducers.TFilter(lambda x: x % 2 == 0)
		comp = transducers.Compose(data, fil)
		self.assertEqual(transducers.transducer([], comp, [0,1,2,3,4,5]), [2,4,6])


if __name__ == '__main__':
	unittest.main()
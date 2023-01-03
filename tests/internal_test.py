import unittest
from src.persian_localizations import get_triplets, get_quadruplets

class TestTripletsGeneration(unittest.TestCase):
	def runTest(self):
		num = 12345678909876543210
		triplets = get_triplets(num)
		self.assertEqual(triplets, [12, 345, 678, 909, 876, 543, 210], 'Triplets are not generated correctly')

class TestQuadrupletsGeneration(unittest.TestCase):
	def runTest(self):
		num = 12345678909876543210
		quint = get_quadruplets(num)
		self.assertEqual(quint, [[0,12, 345, 678], [909, 876, 543, 210]], 'Quintuplets are not generated correctly')

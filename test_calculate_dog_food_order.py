import unittest
from calculate_dog_food_order import DogShelter

class TestCalculateDogFoodOrder(unittest.TestCase):
    def setUp(self):
        self.shelter = DogShelter()

    def test_no_dogs(self):
        self.shelter.set_dog_counts(0, 0, 0)
        self.shelter.set_remaining_food(10)
        result = self.shelter.calculate_dog_food_order()
        self.assertEqual(result, 0.0)

    def test_single_size_dogs(self):
        self.shelter.set_dog_counts(5, 0, 0)
        self.shelter.set_remaining_food(15)
        result = self.shelter.calculate_dog_food_order()
        self.assertEqual(result, 45.0)

    def test_multiple_sizes_dogs(self):
        self.shelter.set_dog_counts(3, 1, 4)
        self.shelter.set_remaining_food(15)
        result = self.shelter.calculate_dog_food_order()
        self.assertEqual(result, 186.0)

    def test_large_remaining_food(self):
        self.shelter.set_dog_counts(2, 3, 2)
        self.shelter.set_remaining_food(100)
        result = self.shelter.calculate_dog_food_order()
        self.assertEqual(result, 50.0)

    def test_small_remaining_food(self):
        self.shelter.set_dog_counts(2, 2, 2)
        self.shelter.set_remaining_food(5)
        result = self.shelter.calculate_dog_food_order()
        self.assertEqual(result, 31.2)

if __name__ == '__main__':
    unittest.main()

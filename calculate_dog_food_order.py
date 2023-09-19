class DogShelter:
    def __init__(self):
        self.small_dogs = 0
        self.medium_dogs = 0
        self.large_dogs = 0
        self.remaining_food = 0

    def set_dog_counts(self, small_dogs, medium_dogs, large_dogs):
        """Set the number of dogs in each size category."""
        self.small_dogs = small_dogs
        self.medium_dogs = medium_dogs
        self.large_dogs = large_dogs

    def set_remaining_food(self, remaining_food):
        """Set the remaining food from last month."""
        self.remaining_food = remaining_food

    def calculate_dog_food_order(self):
        """Calculate the amount of dog food to order for the next month."""
        # Food requirements per dog size
        food_per_small_dog = 10
        food_per_medium_dog = 20
        food_per_large_dog = 30

        # Calculate the total food needed for each dog size
        total_food_small = self.small_dogs * food_per_small_dog
        total_food_medium = self.medium_dogs * food_per_medium_dog
        total_food_large = self.large_dogs * food_per_large_dog

        # Calculate the total food needed for all dogs
        total_food_needed = total_food_small + total_food_medium + total_food_large

        # Add 20% more food for safety
        total_food_needed += 0.2 * total_food_needed

        # Calculate the total food required, considering remaining food
        food_required = total_food_needed - self.remaining_food

        return food_required


# Example usage:
if __name__ == '__main__':
    shelter = DogShelter()
    shelter.set_dog_counts(3, 1, 4)
    shelter.set_remaining_food(15)
    food_to_order = shelter.calculate_dog_food_order()
    print(f"The amount of dog food to order is {food_to_order} lb.")

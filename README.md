# MosaicDogFood
For Mosaic take home- provides instructions on how to run the tests for the `calculate_dog_food_order` function using `unittest` in Python:

Directory Structure:

```
dog_shelter_food_calculator/
├── calculate_dog_food_order.py
├── test_calculate_dog_food_order.py
├── QUESTIONS.md
└── README.md and LICENSE
```

# Dog Food Calculator

This Python project provides a function `calculate_dog_food_order` to calculate the amount of dog food required for a dog shelter based on the number of dogs and the remaining food from the previous month.

## Requirements

- Python 3.x (https://www.python.org/downloads/)

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/p-disha/demo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dog-food-calculator
   ```

3. Install any necessary dependencies (in this case, we only need Python):

   ```bash
   # No additional dependencies required
   ```
## Running the Program

 Open the calculate_dog_food_order.py file in a code editor.

 Adjust the input values in the example usage section, such as the number of small, medium, and large dogs, and the remaining food from the previous month.

 Run the program:

   ```bash

   python calculate_dog_food_order.py
   ```

The program will calculate and display the amount of dog food to order for the next month.


## Running the Tests

You can run the unit tests for the `calculate_dog_food_order` function by following these steps:

1. Open a terminal window in the project directory if you haven't already.

2. Run the following command to execute the tests:

   ```bash
   python -m unittest test_calculate_dog_food_order.py
   ```

   This command will discover and run all the test methods defined in the `test_calculate_dog_food_order.py` file.

3. After running the tests, you will see the test results displayed in the terminal. Passes will be marked with "." and failures with "F."

   Example output:
   
   ```bash
   .....
   ----------------------------------------------------------------------
   Ran 5 tests in 0.001s

   OK
   ```

   If all the tests pass, you should see an "OK" message at the end.

## Adding More Tests

If you want to add more test cases or modify existing ones, you can do so by editing the `test_calculate_dog_food_order.py` file. Simply follow the structure of the existing test methods to create new ones.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides clear instructions on how to clone the repository, install dependencies (none in this case), and run the tests using `unittest`. It also mentions how to add more tests if needed.

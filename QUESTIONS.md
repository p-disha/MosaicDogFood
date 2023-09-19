# Questions and Notes on Acceptance Criteria

This document contains questions, clarifications, and notes related to the acceptance criteria (AC) for the Dog Food Calculator project.

## AC 1: Create a Runnable Function

**Question:** Does the function need to handle negative values for the number of dogs or remaining food?

**Note:** It's important to specify how the function should behave when given invalid inputs.

### Input Constraints

1. **Input Constraints:** Can you provide more details on the constraints for the input values? Are there any minimum or maximum limits for the number of dogs or the remaining food from last month? Should I assume that the input values for the number of dogs and remaining food are always non-negative integers, or do I need to handle other data types or negative values? Can the input values be provided by the user while runing the file as arguments?

### Buffer Percentage

2. **Buffer Percentage:** Is the 20% buffer percentage a fixed requirement, or should it be a parameter that can be adjusted?

### Output Type

3. **Output Type:** What is the expected data type for the calculated food order (e.g., integer, float)? Should the result be rounded to a specific number of decimal places? How should I handle scenarios where the calculated food order results in a fractional value? Should I round it to the nearest integer or handle it differently?

### Unit of Measurement

4. **Unit of Measurement:** Is the unit of measurement for the dog food in pounds (lb.), or should I support other units?
   
### Error Handling

5. **Error Handling:** How should I handle exceptional cases, such as missing input values or invalid input types? Can you provide more examples of input data and the expected results for those examples to ensure that I have a clear understanding of the expected behavior of the function? How should the function handle errors or exceptions? Should it raise exceptions, return error codes, or provide detailed error messages?

### Negative Values

## AC 2: Food Requirements per Dog Size

**Question:** Are there any additional dog sizes besides small, medium, and large that we should consider?

**Note:** The AC mentions three sizes, but it's good to confirm there are no additional sizes.

## AC 3: Always Order at Least 20% More

**Question:** Is there a maximum limit for the amount to order? Should we cap the order at a certain value?

**Note:** The AC specifies ordering 20% more but doesn't mention if there's a limit.

## AC 4: GitHub Project

**Question:** Are there any specific naming conventions or folder structures you prefer for the GitHub project?

**Note:** It's helpful to establish naming and organizational conventions for consistency.

## AC 5: Unit Tests

**Question:** Should we include additional edge cases or scenarios in the unit tests beyond the provided examples?

**Note:** Expanding the test coverage can help ensure the function's robustness.

**Input Validation:** What kind of input validation or error checking should be included in the unit tests to ensure the function behaves as expected when given invalid inputs?

**Floating-Point Calculations:** How should we test the function's behavior when it performs floating-point calculations? Should we use a specific precision for comparison?

## General Notes

Please provide feedback and clarification on any of the above questions or notes to ensure that the project meets your requirements effectively.

I have aken the following calculation assumptions:
At the end of the month, you have:

    3 small dogs, which require 3 * 10 = 30 lb. of food.
    1 medium dog, which requires 1 * 20 = 20 lb. of food.
    4 large dogs, which require 4 * 30 = 120 lb. of food.
    15 lb. of leftover food supply from last month.

Total food required = 30 lb. (small dogs) + 20 lb. (medium dog) + 120 lb. (large dogs) = 170 lb.

Add a 20% buffer to this total:

20% of 170 lb. = 0.2 * 170 = 34 lb.

Finally, add this buffer to the total food required:

Total food to order = 170 lb. (required) + 34 lb. (buffer) -15lb (food from previous month) = 204 lb-15 lb= 189 lb. So total is coming out to be 189 lb with my assumption of subtracting leftover food from the previous month. 


from functools import reduce


numbers = [1, 2, 3, 4, 5]

# Map example: Calculate squares of the numbers. Output: [1, 4, 9, 16, 25].
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# reduce takes a function and applies it to the elements of the list (or iterable) in a pairwise manner.
# x is a sum of prev iteration , and y next list element. The lambda function computes 1 + 4 = 5, 5 + 9 = 14 ..
sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)
print("Sum of squares:", sum_of_squares)
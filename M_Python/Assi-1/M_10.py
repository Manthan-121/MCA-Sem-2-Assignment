numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(10)]
largest_odd = max((num for num in numbers if num % 2 != 0), default=None)
print(f"The largest odd number is: {largest_odd}" if largest_odd is not None else "No odd numbers found.")

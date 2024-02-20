n = int(input("Enter the number of values: "))
numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(n)]
average = sum(numbers) / n
print(f"The average of the {n} numbers is: {average}")

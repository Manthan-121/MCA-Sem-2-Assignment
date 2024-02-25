n=int(input('Enter the value of n : '))
numbers=[]
for i in range(n):
    num=float(input(f'Enter number {i+1} : '))
    numbers.append(num)
print(numbers)


# Initialize counters
positive_count = 0
negative_count = 0
zero_count = 0
odd_count = 0
even_count = 0
total_sum = 0

# Calculate counts and sum
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    total_sum += num

# Calculate average
average = total_sum / n

# Print the results
print("Number of positive numbers:", positive_count)
print("Number of negative numbers:", negative_count)
print("Number of zeros:", zero_count)
print("Number of odd numbers:", odd_count)
print("Number of even numbers:", even_count)
print("Average of all numbers:", average)

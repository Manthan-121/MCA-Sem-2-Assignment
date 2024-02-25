# Input
input_string = input("Enter a string: ")

# Initialize a dictionary to store digit occurrences
digit_count = {str(i): 0 for i in range(10)}

# Count occurrences of each digit
for char in input_string:
    if char.isdigit():
        digit_count[char] += 1

# Display the results
for digit, count in digit_count.items():
    if count > 0:
        print(f"{digit}: {count} time{'s' if count > 1 else ''}")

num = int(input("Enter a number: "))
order = len(str(num))
is_armstrong = num == sum(int(digit) ** order for digit in str(num))
print(f"{num} is{' an' if is_armstrong else ' not an'} Armstrong number.")

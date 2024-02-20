number = int(input("Enter the number for the multiplication table: "))
print(f"Multiplication Table for {number}:\n" + "\n".join([f"{number} * {i} = {number*i}" for i in range(1, 11)]))
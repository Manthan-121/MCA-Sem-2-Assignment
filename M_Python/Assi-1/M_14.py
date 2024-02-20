input_string = input("Enter a string: ")
vowel_count = sum(1 for char in input_string if char.lower() in 'aeiou')
print(f"Number of vowels: {vowel_count}")

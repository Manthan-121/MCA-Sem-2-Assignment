s = input("Enter a string: ")
vowels = sum(1 for char in s if char.lower() in 'aeiou')
length = sum(1 for _ in s)
reverse = s[::-1]
find, replace = input("Enter substring to find: "), input("Enter substring to replace with: ")
modified = s.replace(find, replace)
print(f"a) Vowel count: {vowels}\nb) String length: {length}\nc) Reversed string: {reverse}\nd) After find and replace: {modified}")

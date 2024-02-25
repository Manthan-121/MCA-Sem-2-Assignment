list1=['apple', 'pineapple', 'cherry', 'pysics','banana']

print('#Add/Remove an item to/from a list.')
list1.insert(1,2)
list1.append('animal')
print(list1)
list1.remove(2)
print(list1)

print('#Get the number of elements in the list.')

print('Number of elements in the list are : ',len(list1))
print('#Access elements of the list using the index.')
print(list1[1:3])

#sort list
list1.sort()
print(list1)

#reverce list
list1.reverse()
print(list1)
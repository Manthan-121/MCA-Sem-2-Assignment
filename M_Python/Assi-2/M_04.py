#create a Tuple 
tuple1=(1,2,3,4,"apple","pineapple","cherry",-1,10.25,'A')
#Print Tuple
print(tuple1)
print(type(tuple1))

#Convert tuple into list
list1=list(tuple1)
print('List :',list1)
print(type(list1))

#Remove from list
list1.remove('pineapple')
print(list1)

#covert list into tuple
tuple2=tuple(tuple1)
print('Type : ',type(tuple2))
#Coverted tuple print
print('Tuple Items : ',tuple1[2:])
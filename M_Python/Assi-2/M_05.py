#create dict
mydict={"company":"hyundai",
         "model":"creta",
         "year":2010
}
#print Dict...Items
print(mydict)

#only key
for y in mydict.keys():
   print(y)
 #only values 
for x in mydict.values():
   print(x)
#both
for z in mydict:
   print(mydict.items())

print(mydict["company"])
print(mydict["model"])
print(mydict['year'])


#Add Items using update() 
mydict.update({"color" : "Blue"})
print(mydict)
#Add Items 
mydict["speed"]=500
print(mydict)
#Remove Item
mydict.pop("speed")
print(mydict)


#Check whether a key exists in a dictionary. 
if 'model' in mydict:
    print("model Key Exsist in mydict")
else :
    print('Color Not Exist in my dict') 

if 'brand' in mydict:
        print('Year Exist in my dict') 
else :
    print('Brand Not Exist in my dict') 

# Iterate through a dictionary
for key, value in mydict.items():
    print(key, "->", value)

#Concatenate
mydict2 = {"a": 1, "b": 2, "c": 3}
mydict.update(mydict2)
print(mydict)
mydict2.update(mydict)
print(mydict2)

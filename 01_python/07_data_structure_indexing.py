#list(data structure)

#Lists are ordered collections that can contain elements of different data types.

#mutatable

food=["fruit","vegetables","yogurt","egs","milk"]  #datatype is string 
#index   0        1            2      3      4     #data structur is List
print(food[3])#call elements using index 

print(food)

print(food[-1])

print(food[-2])

food[1]="biryani" #updating elements using the index of food

print(food)

#==========================================================

#Tuple

#Tuples are similar to lists but are immutable, meaning their contents cannot be changed after creation.

coordinates = (4.32,9.34)# immutable
print(coordinates)
print(coordinates[1])

#==============================================================

#Sets

#Sets are unordered collections of unique elements.

#set(data structure)(mutatable)

food_1 ={"fruit","vegetables","yogurt","egs","milk"}
print(food_1)
food_1.add("samosa")
print(food_1)

#=============================================================
#dictionary(key-value pair)(data structure)

#Dictionaries are mutable and allow fast lookups based on keys.

car ={"bran":"ford","model":"mustang","year":1996}
print(car)
car['year']=2001
print(car)
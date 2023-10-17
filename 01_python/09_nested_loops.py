# #nested loop 
# #loop within a loop is called nested loop
# #nested for loop
colors =["red","green","yellow"]
items =["book","pen","copy"]

# for color in colors:
for item in items:
    for color in colors:
        print(color,item)
        print(item,color)
        

#nested while loop

i=0
while i<3:
    j=0
    while j<3:
        print(i,j)
        j+=1
    i+=1
    
#for loop inside while loop

i = 1
while i<4:
    for j in range(3): #range is a function #0,1,2
        print(i,j)
    i+=1 #i=i+1
    
#while loop inside for loop

i = 1
for i in range(4):
    while i<3:
        print(i,j)
        i+=1
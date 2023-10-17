#control flow statements
#three types
# 1. Conditional statements 2. for loops 3. while loops

# 1. Conditional statements <,>,==,!=
x=-5

if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
elif x==0:
    print("x is equal to zero")
else:
    print("x is negative")

#=====================================================

# 2. for loops
# `for loop` is used to `iterate` over a sequence of items  list, tuple, string, or other iterable objects. 
menu=["fruit","vegetables","yogurt","egs","milk"]

for items_in_menu in menu:
    print(items_in_menu)

#==========================================================
    
# 3. While loop

i=1
while i<10:
    print(i)
    i += 1 #adding 1 in "i" and then saving the result in i again

#==========================================================
    
# # break
for letters in "Python":
    if letters == "h":
        break #controled statement in loops beaks the execution on the condition 
    print(letters)

#==========================================================

#continue    
for letters in "Python":
    if letters == "h":
        continue #controled statement in loops skips the execution on the condition 
    print(letters)
    
#==========================================================

#pass

for letters in "Python":
    if letters == "h":
        pass #controled statement in loops no interuption on the condition 
    print(letters)
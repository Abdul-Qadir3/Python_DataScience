#functions
#functions is a block of code which only runs when it is called.
#we can pass data,parameters into a function
#function can return data as result
#function defined using def

def greeting():#function defined
    print("Hello World")#passing data to the body of function
greeting()#calling function output

#==========================================================

def aoa():
    print("Assalam-o-Alaikum")
aoa()

#==========================================================

def aoa_1(name):#using parameters
    print(f"Assalam-o-Alaikum, {name}!")
aoa_1("Abdul Qadir")

#==========================================================

def aoa_(name="default value"):#default parameter
    print(f"Assalam-o-Alaikum, {name}!")
aoa_("Asif Khan")
aoa_()

#===========================================================

#return values

# def square(number):
#     return number*number
# print(square(9))

#Or

def square(number):
    return number*number
result =square(9)
print(result)

#========================================================

#recursion function

def factorial(n):# function with condition
    if n==1:
        return 1
    else:
        return n*factorial(n-1)# product of all positive integers from "1" to "n"
print(factorial(4))

#============================================================

#lambda function(one line function)

x = lambda a: a+10 # "x" is function name "a" is a parameter of the function "a+10" is the body of the function
print(x(5))

y = lambda a: a/10
print(y(19))

z =lambda a, b: a*b #with two parameters
print(z(2,7))#limitation #restrictive function

#============================================================

# 10 function for practice with def and 10 function with lambda
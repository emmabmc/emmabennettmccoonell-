# File: homework1.py
# --- Variables and Data types ---
a = 10
print(a)
print(type(a)) #a is an integer, whole number with no decimals
b = 1.5
print(b)
print(type(b)) #b is a float, number with decimals
c = 3j
print(c)
print(type(c)) #c is a complex number, has a real and imaginary number
d = "hello"
print(d)
print(type(d)) #d is a string, a sequence of characters
e = [1, 2, 3]
print(e)
print(type(e)) #e is a list, an ordered collection of items 
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictionary, a collection of key-value pairs
g = (1, 2)
print(g)
print(type(g)) #g is a tuple, an ordered collection of items that cannot be changed
h = ["apple", "banana", "cherry"]  
print(h)
print(type(h)) #h is a list, an ordered collection of items 
i = True
print(i)
print(type(i)) #i is a boolean, can only be True or False
j = None
print(j)
print(type(j)) #j is a NoneType, represents the absence of a value  
k = [True, "blue", 12]  
print(k)
print(type(k)) #k is a list, an ordered collection of items
l = str(14)
print(l)
print(type(l)) #l is a string, a sequence of characters
m = 1e4
print(m)
print(type(m)) #m is a float, number with decimals
'''
1) 9 different types
2) float, string, list, NoneType, boolean, tuple, dictionary, complex, integer
3) b & m, d & l, e & h & k
4) data type l is a string, its not an integer because str() is used to convert a variable to string
5) range is another data type in python

'''
n = range(5, 10)
print(n)
print(type(n)) #n is a range, represents a sequence of numbers

# --- Boolean ---
print(10 > 9) #True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print(10 <= 9) #False, 10 is not less than or equal to 9
bool("abc") #True, non-empty string is True
bool(["apple", "cherry", "banana"])#True, non-empty list is True
bool[True] #True, True is True
bool(False) #False, False is False
bool(0) #False, 0 is False
bool("") #False, empty string is False
bool(" ") #True, non-empty string is True
bool(()) #False, empty tuple is False
bool([]) #False, empty list is False
bool({}) #False, empty dictionary is False
bool(True and False) #False, True and False is False
bool(True and True) #True, True and True is True
bool(False and False) #False, False and False is False
bool(True or False) #True, True or False is True
bool(False or False) #False, False or False is False
bool(not False) #True, not False is True
bool(not True) #False, not True is False
'''
1) anything that is not empty or zero is True while anything that is empty or zero is False
2) the expressions in lines 66-68, I would assume that the brackets make the expression not empty but I was wrong
3) in like 81, it's true because I previously declared a to equal 10, so a equals 10
4) in line 82, it's false because I previously declare b to equal 1.5, so it is false that b equals 2.5
'''
bool(a = 10)
bool(b = 2.5)

# --- Operators ---
# 3.3.1. Arithmetic Operators
print(10 + 5) #15, + preforms addition
print(10 - 5) #5, - preforms subtraction
print(2 * 4) #8, * preforms multiplication
print(6 / 3) #2.0, / preforms division
print(5 % 2) #1, % preforms modulus, returns the remainder of a division
print(3 ** 2) #9, ** preforms exponentiation, raises a number to the power of another number
print(15 // 2) #7, // preforms floor division, returns the largest integer less than or equal to the result of a division

#3.3.2. Comparison Operators
print(5==2) #False, == checks if two values are equal
print(10 != 10) #False, != checks if two values are not equal
print(2 < 5) #True, < checks if the left value is less than the right value
print(12 > 5) #True, > checks if the left value is greater than the right value
print(5 <= 6) #True, <= checks if the left value is less than or equal to the right value
print(1 >= 10) #False, >= checks if the left value is greater than or equal to the right value  

#3.3.3 Assignment Operators
x = 5
x += 5
x -= 4
x *= 3

#3.3.4 Logical Operators
#and evaluates both statements and returns True if both are True, otherwise returns False
bool(x == 5 and a == 10) 
bool(x == 4 and a == 10)
#or evaluates both statements and returns True if at least one is True, otherwise returns False
bool(x == 5 or a == 10)
bool(x == 4 or a == 5)
#not evaluates a statement and returns True if the statement is False, otherwise returns False
bool(not(x == 4))   
bool(not(a == 10))

#1) / divides two numbers and returns a float, // divides two numbers and returns the largest integer less than or equal to the result of a division
#2) % returns the remainder of a division, // divides two numbers and returns the largest integer less than or equal to the result of a division
#3) I would use % 
5 % 2 #returns the reminder which is 1
#assignment variables assign a value to a varriable 

# --- Strings ---
my_string = "hello"
print(my_string) #prints hello
print(my_string[0]) #prints h, the first character of the string
print(my_string[1]) #prints e, the second character of the string
print(my_string[2]) #prints l, the third character of the string
print(my_string[3]) #prints l, the fourth character of the string
print(my_string[4]) #prints o, the fifth character of the string    
print(my_string[-1]) #prints o, the last character of the string
print(my_string[1:3]) #prints el, the second and third characters of the string
print(my_string[0:5:2]) #prints hlo, every second character from the first to the fifth character of the string
len(my_string) #returns 5, the length of the string
my_string + "goodbye" #returns hellogoodbye, concatenates the two strings
my_string * 7 #returns hellohellohellohellohellohellohello, repeats the string 7 times

#3.4.1 questions 
#1) slicing means to extract a portion of a string or creating a substring, line 134 and 135 slicing the string or creates a substring

name = "Oski"
print("Hello, my name is " + name) #prints Hello, my name is Oski, combines the string with the variable name
name = "Oski"
print(f"Hello, my name is {name}") #prints Hello, my name is Oski, combines the string with the variable name. f tells python to evaluate what is in the curly braces. 


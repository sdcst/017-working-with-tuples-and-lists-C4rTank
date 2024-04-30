#!python3

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""

c = 'Cat'
f = 'Fish'
d = 'Dog'
b = 'Bear'
t = 'Turtle'

animals = [c, f, d, b, t]
animals.sort()

num = input("Please input a number: ")
    
try:
    num = int(num)
    picked = animals[num]
    print("The animal at that index is", picked)
except:
    print("That is not a number!")
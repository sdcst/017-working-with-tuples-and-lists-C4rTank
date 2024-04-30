#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""


a = int(input("Please input a positive integer: "))
if a == -1:
    a = 0
b = int(input("Please input a positive integer: "))
if b == -1:
    b = 0
c = int(input("Please input a positive integer: "))
if c == -1:
    c = 0
d = int(input("Please input a positive integer: "))
if d == -1:
    d = 0
e = int(input("Please input a positive integer: "))
if e == -1:
    e = 0
f = int(input("Please input a positive integer: "))
if f == -1:
    f = 0
g = int(input("Please input a positive integer: "))
if g == -1:
    g = 0
h = int(input("Please input a positive integer: "))
if h == -1:
    h = 0
i = int(input("Please input a positive integer: "))
if i == -1:
    i = 0
j = int(input("Please input a positive integer: "))
if j == -1:
    j = 0

List = [a,b,c,d,e,f,g,h,i,j]
List.remove(0)
print(List)
List.sort()

print("The largest number you entered is",List[-1])

#done
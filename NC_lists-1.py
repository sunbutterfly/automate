"""

Let's do some looping, slicing and assignment! You might also need some tuple unpacking!

>>> a_string
'Hello'
>>> a_list
[5, 6, 7, 8, 9]


Create a function that takes two "loopable" things and prints them out together:

>>> smoosh(a_list, a_string)
5 H
6 e
7 l
8 l
9 o

What if you wanted to make the characters of the string be members of
the list? Create the following variables from the a_string and a_list
variables:

>>> a
[5, 6, 7, 8, 9, 'H', 'e', 'l', 'l', 'o']
>>> b
[5, 'Hello', 6, 7, 8, 9]
>>> c # insert the letters replacing the 1th-2th  positions
[5, 'H', 'e', 'l', 'l', 'o', 8, 9]

"""

a_string = 'Hello'  ## b
a_list = [5,6,7,8,9]  ## a


def smoosh(a,b):
    for i, letter in enumerate(b):
        print(a[i],letter)

smoosh(a_list, a_string)

a = a_list + list(a_string)

b = a_list.copy()
#b = list(a_list)
b.insert(1, a_string)

c = a_list[0:1] +list(a_string) + a_list[3:]

print(c)

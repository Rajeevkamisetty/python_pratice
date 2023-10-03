#mathematical operator
#addition
a = input("value of a is")
b = input("value of b is")
print(int(a) + int(b))

#subration
a = input("value of a is")
b = input("value of b is")
print(int(a) - int(b))

#multiplication
a = input("value of a is")
b = input("value of b is")
print(int(a) * int(b))

#division
a = input("value of a is")
b = input("value of b is")
print(int(a) / int(b))

#module
a = input("value of a is")
b = input("value of b is")
print(int(a) % int(b))

#floor division
a = input("value of a is")
b = input("value of b is")
print(int(a) // int(b))

# equal
a = input("value of a is")
b = input("value of b is")
print(int(a) == int(b))

# greaterthan or equal
a = input("value of a is")
b = input("value of b is")
print(int(a) >= int(b))

# lessthan or equal
a = input("value of a is")
b = input("value of b is")
print(int(a) <= int(b))

#and operator
a = input("value of a is")
b = input("value of b is")
print(int(a) & int(b))

#or operator
a = input("value of a is")
b = input("value of b is")
print(int(a) | int(b))

#xor operator
a = input("value of a is")
b = input("value of b is")
print(int(a) ^ int(b))

#is operator
a = input("value of a is")
b = input("value of b is")
print(int(a) is int(b))

#is not operator
a = input("value of a is")
b = input("value of b is")
print(int(a) is not int(b))

#string concadation
#operator overloading
name = input("enter your name")
surname = input("enter your surname")
fullname = (name + surname)
print(fullname)

#f'string operator
fullname = f"{name} {surname}"
print(fullname)

#string join methods
fullname = (name, surname)
print(" ".join(fullname))

#string division
#splict
email = input("enter your email")
print(email.split("@"))

#splict by lines
email = input("enter your email")
print(email.splitlines("@"))

# partation
email = input("enter your email")
print(email.partition("@"))

#rpartation
email = input("enter your email")
print(email.rpartition("@"))

#capitalize
a = input("enter a value")
print(a.capitalize())

#title
a = input("enter a value")
print(a.title())

#upper
a = input("enter a value")
print(a.upper())

#lower
a = input("enter a value")
print(a.lower())

#case fold
a = input("enter a value")
print(a.casefold())

#swap case
a = input("enter a value")
print(a.swapcase())

#isnumeric
d = input("value of d")
print(d.isnumeric())

#is alnum
print(d.isalnum())

#is decimal
print(d.isdecimal())

#is digit
print(d.isdigit())

#is asscii
print(d.isascii())

#is upper
print(d.isupper())

#is lower
print(d.islower())

#is space
print(d.isspace())

#isidentifier
print(d.isidentifier())

#isprintable
print(d.isprintable())

#is title
print(d.istitle())

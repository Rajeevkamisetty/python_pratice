# fibanoci series
n = 10
a = 1
b = 0
i = 1
while i <= n:
    print(b)
    a = a + b
    b = a - b
    i += 1

# swap two numbers using temp variable
a = 3
b = 4
tempfile = a
a = b
b = tempfile
print(a, b)

# swap two numbers without temp variable
a = 54
b = 5459
a = a + b
b = a - b
a = a - b
print(a, b)
# other method
a = 54
b = 5459
a = a * b
b = a / b
a = a / b
print(int(a), int(b))

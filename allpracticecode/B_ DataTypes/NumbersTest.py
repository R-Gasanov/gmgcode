# We will now be looking at Numbers, and the various types

#There are 3 basic types

# Integer, a basic whole number
x = 1
# Float, a number that is a decimal
y = 17.7
# Complex a number with multiple featurs that involves with symbols and letters
z = 1j

# You can of course convert each number to a different number type depending on what you want

a = float(x)

b = int(y)

c = complex(x)

# From looking we are conerting these number depending on what statement (number type we want)

print (f'{x} Is the original, {a} is now changed')
print (type(a))
# Now the usage of the statement 'type', it allows us to see what datatype it is
print (f'{y} Is the original, {b} is now changed')
print (type(b))

print (f'{z} Is the original, {c} is now changed')
print (type(c))

# With out test running we can at the end see how it will look and operate
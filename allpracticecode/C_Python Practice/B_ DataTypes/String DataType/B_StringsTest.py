# Now we will look at the more interersting things you can do with strings

# We are going to see what strings in python are

# In basic principle stings in python are represented as arrays of bytes with the use of unicode
print ('#######################')
# We will be looking a some basic ways to interact with strings now
x = 'Good morning'
# We've assigned a string variable above
print (x[2])
# Every single string letter is assigned a numericle value

# The numbers begin from 0 up depending on how large the string is
print ('#######################')
# So in this case, 2 will be the 2nd 0,

print (f"""So essentially what your seeing above is the third represented letter.
How do we know its not the 2nd O? Well as explained in the comments,
each number is represented numerically from 0 onwards.
So G will equal to 0 and o will equal to 1 and etc.
So if we checked the 3rd numerical position,
we would get {x[3]}, as you can see its d, meaning that it is infact the 2nd 0.
Which overall denotes that the system starts with 0 and onwards.""")

# The next thing we can look for is traversing through a string
print ('#######################')
# We will be needing a for loop for this
for y in x:
    print (y)
    # What we are doing here, is we are going through each letter in the x string
print ('####################')
# The input will be provided in y, which we can see represents every letter and space

# This might be a long way to count the general length of the string, so theres a short-cut in python
print (len(x))
# The len command allows us to see the length in an integer value specifically
print ('Above as you can see is the length of the string, giving an integer number.')

# Now lets try and use the values within the tuples, through accessing them first
numbers = (7,6,8,4,9)
print (numbers[3])
# Since a tuple is organised through a serious of numbers from 0+, we know the 3rd index position is 4
print (numbers[-2])
# We can even use negative numbers to represent the list within a backwards format
print (numbers[1:3])
# Now here we are reviewing the contents through the index, but this time we are looking inbetween this index and the other
print ('####################')
# There are even more opportunities with this specific command, lets take a look
print (f'These are the first three numbers {numbers[:3]}')
# Now as you can see with this specific line up of the colon, its going from the 4th value, and backwards
print ('####################')
# Meaning that it will present as the values behind the 4th value but not the 4th value specifically
print (f'These are last two left numbers {numbers[2:]}')
# As you can see it works both ways, it all depends on where the colon situates itself overall.
print ('####################')
# Whats intersting is that this can also be applied to negative indexes as well.
print (numbers[-4:-1])
# The possibilities are endless, we can use this in terms of more than just tuples
print ('####################')
# From this point on we can also use the same system when looking numbers ahead or behind, which can be rather useful
print (f'These are the first three numbers {numbers[:-2]}')
# As you can see we are using these
print (f'These are last two left numbers {numbers[-2:]}')
# Now lets get more complex with this coding and make something more dyanimic
print ('####################')
# Lets start here with if statements and specific conditions
numbers_two = (4,5,6,1,65,7,6)
# We're stating a tuple here, as you can see above
if (numbers_two[-3]) == 65 and (numbers_two[2]) == 6:
    print (f' As you can see we have the 3rd last number is {numbers_two[-3]}, and the 3rd number is {numbers_two[2]}')
else:
    ('It appears we may not have number 65 as our 3rd last number or our 2nd number is not 6.')


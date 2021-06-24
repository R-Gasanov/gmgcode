# When creating a said tuple, we usually do indeed assign values to it, since it cannot change afterwards. This is called packing
cities = ('london','copenhagen','minsk')
# We are just looking into the principles of said tuples. Getting a bit better of an understand to their dynamics
print (cities)
# We can extract these values within the tuple which is technically called unpacking
print ('####################')
# This is how we would hypothetically do it
(Big_Ben, Rosenborg_Castle, Minsk_Hotel) = cities
# What we've done is essentially assign each of these variables within the index format that its aligned to with the cities
print (Big_Ben)
print (Rosenborg_Castle)
print (Minsk_Hotel)
# As you can see we've assigned them and print them to their linked site
print ('####################')
# We can be more specific when unpackaging specific components of the tuple, for an example using an asterisk '*'
colours = ('green','purple','red','blue','yellow')
# Heres how we do it below, with the new tuple we are using above
(green, purple, *primary_colours) = colours
# What essentially the asterisk does, is since there are 5 values within the tuple, and we are only extracting three, we use the asterisk
print (green)
print (purple)
print (primary_colours)
# So the asterisk will use the remaining values convert them into the list so that they too can be unpackaged
print ('####################')
# Whats intersting is that we can continue adding additional things we would like to extract after the asterisk
vegtables = ('cucumber','carrot','swiss chard','garlic','zuccini')
(*vegies, fruit) = vegtables
# Python understand that another variable after the asterisk, will be assigned with the the last value, and the more there are, the more assigned
print (vegies)
print (fruit)


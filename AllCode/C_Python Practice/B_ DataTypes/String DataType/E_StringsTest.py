# Not only can we ask for specific parts of the string, we can modify on how we percieve them as well
x = (' Good_Morning ')
# Now what we can do with this its change its case from upper to lower, here are the following commands
print (x.upper())
# The one above is upper
print (x.lower())
# The next one is lower

# As you can see the different, we changes the caps with upper and lower
print ('#######################')
# Now we can even replace certain letters with other with the command 'replace()'
print (x.replace('G', 'F'))
# We can even clean up the string, if its provdied with excess whitespace that is not even required
print ('#######################')
# This will remove the whitespaces that are from the beggining and the end
print (x.strip())
# We can even split the string itself to represent a list
print ('#######################')
# We are splitting from the specific symbol of _, in which Good and Morning will be shown seperatley
print (x.split('_'))

print ('#######################')
# Now we will even look into how we can combine two different strings into one as well (Concatenate)
y = ('Good')
# We've created seperate strings for the following to be connected
z = ('Morning')
# As shown below, both strings will be literally added each other and will be represented by a new variable (s)
s = y + z

print (s)
# Although the issue is that theres no space, so we can also add the in between
print ('#######################')
# So we will be properly formatting when the variables are finally updated
v = y + (' ') + z

print (v)




# Now lets look into looping through the tuple, which will be most intersting indeed
country = ('Canada','Mexico','Slovenia','Croatia')
# We'll be using a for loop, which will go through the tuple
for x in country:
    print (x)
    # Whats done here specifically is we are printing what the for loop went through, which is the values within the tuple
print ('####################')
# Whats intersting is that we can even loop over the index as well
for index in range(len(country)):
    print (country[index])
    # What we are doing is essentially going to output the same thing but, we are going through every single index position which is the values
print ('####################')
# We can even look at looking at how long the tuple is with the length of the tuple itself via the (len) command
index = 0
while index < len(country):
    print (country[index])
    index = index + 1
    # This is how we do it through a while loop, which is just the small amount that we can look into for the potential future of loops in tuples

# Now we will be looking at passing a list as an argument throught the function
print ('#######################')
# So lets make our function!
def my_function(movies):
    # As per usual we will iterate through the list
    for x in movies:
        print (x)
# Now lets provide us with the list
horror = ['Scream', 'Friday the 13th', 'Jigsaw', 'Conjuring']
# We've created the list now we will simply call upon the function
my_function(horror)
# As you can tell we siphon the list through the function and provie us with the intel through it
print ('#######################')
# To let functions provide certain values back, you can use the given command (function) to do so
def my_function(y):
    return 2 * y
# This kind of acts like a print command but simply returns the value once its done its course
print(my_function(2))
# Although whats interersting with is that, you can use this value for various other things, so its similar to a variable you wish to edit
print (my_function(8))
# You can do it consistently as well which is very useful
print ('#######################')
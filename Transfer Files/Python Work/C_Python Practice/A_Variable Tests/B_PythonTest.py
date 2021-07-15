# Now I will be experimenting with Global variables

text = 'food'
# A variable is created here for me
def myfunc(): #With the creation of a function, the region is specified only for me
    text = 'water'
    print (text)
myfunc()
# Although the variable within myfunction which is (local) it only prints that specifically
print (text)
# The last print command, oddly does not work for some odd reason


# Need to evaluate on this specifically
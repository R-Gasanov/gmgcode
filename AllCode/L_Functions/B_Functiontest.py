# Functions are very useful and can help greatly organise code and seperate important pieces from one another
def my_function(*colours):
    # You might wandering what does that (*) do? If you don't how many arguments you'll pass
    print ('My favorite colour is ' + colours[1])
    # Since we don't have a specific requirement of the amount of arguments we can provide as many or as little as we want!
my_function('blue','green','black','red')
# So in the end all we needed was too arguments, but since we had more avaliable and provided the (*) it worked out successfully in the end
print ('#######################')
# Now we will be looking at keyword arguments, as of which allows us to send arguments with a key value syntax
def my_function(colour1, colour2, colour3):
    print ('My favorite colour is ' + colour2)
# What we will be doing is assigining the keys with the arguments, heres how we do it below
my_function(colour1 = 'blue', colour2 ='green', colour3 = 'yellow')
# As you can see it only used the one of the arguments that we specified out of the three using the keyword
print ('#######################')
# Again if we don't know how many keyword arguments there are we would instead add two (*)
def my_function(**country):
    print ('The country and capital is ' + country['capital'])
    # As you can tell, we are now using the key country, which we haven't specified originally
my_function(country = 'Norway', capital = 'Oslo')
# As you can tell it works, since we've provided the neccesary argument along with it
print ('#######################')
# Now we will look at parameter values calling a function without an argument uses the default value prefiven
def my_function(country = "Denmark"):
    print ('I am from ' + country)
    # So we've preassigned it as denmark
my_function('Finland')
my_function('Latvia')
my_function('Estonia')
my_function()
# As you can see we are missing Denmark, since we haven't provided the argument it will become the default
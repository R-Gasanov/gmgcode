# What we will be doing here is using functions, which are essentially closed of code that can be used later
def my_function():
    # Above here what I am doing is defining my function
    print ('Hello from a function')
# And as you can tell we have to indent when creating a function, what this function does is it prints hello
my_function()
# Although we are using the print command it does not print so we actually have to call out the function
print ('#######################')
# Data can go through the function as arguments
def my_function(cars):
    print (cars + " sold")
# So whenever we call our function, and provide values, it will passs through the function    
my_function('Audi')
my_function('BMW')
my_function('Nissan')
# When we print this out, the variable cars will be provided with the values in the call plus the string at the end
print ('#######################')
# Sometimes functions require additional arguments otherwise it would not operate, heres an example
def my_function (count, city):
    print (count + " " + city)
    # Here is the two arguments provided in the bootm
my_function('Austria','Vienna')


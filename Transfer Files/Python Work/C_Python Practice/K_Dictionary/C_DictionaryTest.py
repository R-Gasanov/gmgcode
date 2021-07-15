# Now that we know some of the basics within a dictionary, how would we access some specific parts of inforamtion?
headphones = {
    'brand': 'Beexcellent',
    'wireless': False,
    'year': 2021
}
# What we can do is assign a new variable to equal the value within a specific key
x = headphones['brand']
# With this we are taking the brand key which has the contents beexcellent that is the actual value
print (x)
# There is an addtional method for this as well
print ('####################')
# What we are using here is the command (get) which allows us to obtain the value within the key year
y = headphones.get('year')
# This ultimately does the same thing but can be percieved as another way of doing so
print (y)
# There is a method for you to access what keys there are within the dictionary as well
print ('####################')
# There is a command called (keys) to do so
z = headphones.keys()
# This will show us all the keys within the dictionary
print (z)
# Lets continue here and see what happens if we add something to the dictionary after we add something
headphones['colour'] = 'green'
# Now that we have appended the result what will happend to the variable z
print ('####################')
# As shown below it now shows us the new key that has been added
print (z)
# We also have another command for values as well not just for the keys
print ('####################')
# The command is called (values), which allows us to look at the values specifically for us
w = headphones.values()
# With this, as straightforware we will now be revealed what is the values within headphones below
print (w)
# We can even see the changes towards the variable as well, with the value of w being updated similarly to the variable z
print ('####################')
# So lets do another key and value towards the dictionary headphones
headphones['Adjustable'] = True
# Now lets see whether or not the value of w changes
print (w)
# We can also get accessed to all the items within the dictionary, almost represented as a list
print ('####################')
# It is generally represented as the command items
v = headphones.items()
# This will essentially provide all of the items within the actual headphones itself
print (v)
# What about if we want to copy a specific Dictionary?
console = {
    'brand': 'Playstation',
    'type': 'PS3',
    'year': 2010
}
# Well of course there is indeed a command for this as well
print ('####################')
# The command is called (copy), which seems pretty self explanatory
purchases = console.copy()
# We essentially assign a new variable which then copies the variable itself
print (purchases)
# There is another way supposedly if you didn't want to use the (copy) command
print ('####################')
# What instead is we will be assigned purchases as console, but specifying that it would be a dictionary
purchases_two = dict(console)
# We use the (dict) command in order for us to do the supposed change in the end
print (purchases_two)

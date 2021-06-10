# Theres still a lot to look into with strings, now we will go into even more specifics in strings

x = ('Good Morning')
# What we are doing is requesting a specific section of the string to be printed out
print ('Morning' in x)
# With this we will only be getting the specific line of (Monring) as our output
print ('#######################')
# With this unique operation, we can now inspect various lines of strings and interact with them
if 'Good' in x:
    print (f'The person was more formal since he used (Good) in his response.')
else: # An else statement essentially means the the inital if statement was not true, and alterior outcome will occur
    print ('The person was being informal.')
# As you can tell, we can do quite a lot with this statement
print ('#######################')
# Not only can we look for what we want in a text, we can also do the opposite as well with NOT (operation)
print ('Spaghetti' not in x)
# We definetly know Spaghetti is not in the string
print ('#######################')
# Simularly we can use this in a more complex setting
if 'Good' not in x:
    print ('The person was being informal.')
else: # Since (Good) is indeed in the text, the else statement will be true in this occasion
    print (f'The person was more formal since he used (Good) in his response.')
# As you can tell we can use this in multiple different settings



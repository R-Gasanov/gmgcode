# We can't technically change its values with a tuple, although there are some unique ways of doing so
vegtables = ('cucumber','carrot','zuccini','swiss chard','garlic')
# As a small portion of us know, zuccini is not a vegtable
veg_list = list(vegtables)
# What we're doing here, is converting this tuple into a list, which means we can change its content now
print (veg_list)
# Now we can change zuccini in an actual vegtable
veg_list[2] = 'kale'
# We know that the index of zuccini is 2, so we specify this value and change it to kale, which is an actual vegtable
vegtables = tuple(veg_list)
# Now we are doing the opposite with what we've done on our 2nd line of code, changing it back to a tuple
print (f"""As you can see,
we have changed the contents within this tuple.
How you might ask?
Well we converted the tuple into a list,
which then became changable,
so we reasigned the 3rd value,
into an actual vegtable.
As shown ahead, {vegtables}""")
# Which is one way to technically change the contents of a tuple
print ("""Now remember, a tuple can not be changed or add new values,
so you can not use the command (append) in order to add additonal information,
but as shown above we were able to change an existing value.
Via conerting it into a tuple.""")
# So how would we add an additional value within the tuple?
print ('####################')
# We will be doing the same thing essentially in basic principle
veg_list = list(vegtables)
# So we wil now be apending a list, which is actually doable.
veg_list.append('tomato')
# And we do the same thing, which is reversing it back to a tuple
vegtables = tuple(veg_list)
# Which indeed works, now we were able to add an additional value to the whole variable
print (vegtables)
# Now we done, change and add. What above removing?
print ('####################')
# It might be as you guessed it similar to what we've done previously
veg_list = list(vegtables)
# We do the same concept but of course, change the command using to (remove)
veg_list.remove('tomato')
# We all should know that tomatoes are not vegtables of course
vegtables = tuple(veg_list)
# As you can see from below, we've edited the tuple through the same system to remove tomato
print (vegtables)
# And finally what if we want to delete all together? Well you guessed it...
print ('####################')
# Its simple you simply use the del command
del vegtables
# If we were to print out vegtables we would recieve and error since, its now equivelant to nothing

# Now lets get into String Formatting, we can combine strings together right?
txt = ('temperature')
# But what about integers and strings?
num = (17)
# This will allow the format() command to understand
print (txt,format(num))

print ('#######################')
# But what about specifying specific parts of a proper text for example? We use this unique brackets
one = (6)
two = (4)
three = (10)
# As you see below, we're currently using these unique brackets to formulate where each numericle value goes
maths = ('There are {} eggs in hen one, and {} in hen two, which equals to {}')
print (maths.format(one,two,three))
# As the order provided each one of the variables will go into the order based on the brakets as well
print ('#######################')
# Heres what you can do as well
print ("""You can also specify the order with the number in the brackets,
So lets say that you position the first bracket as {2}.
This would mean that the 3rd number positioned in the format command will be presented there,
Some people may prefer this in specific scenarios.""")
# Additional Stuff that could be handy in the later future
print ('#######################')
# Escape characters; they are essentially allow you to use illegale characters that will not operate

#badscript = ("Juliet speaks softly,"Art thou Romeo?" pondering around aimlessly in her stary night view. ")

# As you can tell, using speech marks on the 2nd row does not properly operate for this string
goodscript = ("Juliet speaks softly,\"Art thou Romeo?\" pondering around aimlessly in her stary night view. ")
# Now what you can see here, we use this symbol '\' which allows us to use illegal characters within the string
print (goodscript)
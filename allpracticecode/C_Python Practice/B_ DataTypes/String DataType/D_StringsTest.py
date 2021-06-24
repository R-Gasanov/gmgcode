# Now we will be looking at slicing , essentially splitting strings seperately
x = 'Good Morning'
# Now as you can see from the bottom we're using a colon ':'
print (x[:4])
# Now what were doing is we selected a letter through the representation of numericle values
print ('#######################')
# And using the colon depending on which side, since its in front we're going backwards

# Reveal all the other letters that are after the inital letter with it as well
print ("""As you can see,
we got the word Good.
Since the 4th position in the string is d,
and the the colon (:) is in the beggining,
we went backwards which spelled Good.""")
# We can do this as well to go forwards additionally
print ('#######################')
# We will be using the colon after the specific numericle value as seen below
print (x[5:])
# The 5th position is M, and with the colon we will get (Morning)
print ('#######################')
# We can even go backwards with the numericle value, if your working with very long strings
print (x[:-7])
# Now we've went backwards, which in the end has printed Good since g the end of morning is -0
print ('#######################')

print (x[2:8])
# With this we can even go between numericle numbers to show what we might want in between

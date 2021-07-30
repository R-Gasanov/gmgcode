# Now lets look into loops with Dictionaries, and see how they would interact with them
book = {
    'name': 'Operation Open Sky',
    'Author': 'R.G',
    'genre': 'fantasy/steampunk'
}
# We've created a simply dictionary above as you can see
print ('####################')
# Lets see what happens if we use a simple for loop for this dictionary
for x in book:
    print (x)
    # As you can tell we are only given back the value itself and not the actual contents
print ('####################')
# For us to return the values instead, we again use the command values()
for y in book.values():
    print (y)
    # This instead will give us the list of values rather than the actual key
print ('####################')
# There is supposedly another way to get the keys only rather than the first method which is longer but at least you'll know
for z in book.keys():
    print (z)
    # As you can see it is longer but using the command (keys) can be useful in multiple other different occasions
print ('####################')
# What about printing out both the values and keys?
for w, u in book.items():
    print (w, u)
    # Well we use the command (items), which allows us to do that following


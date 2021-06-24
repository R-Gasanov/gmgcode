# With dictionaries we can also check whether or not certain specific keys exist or not.
cars = {
    'brand': 'Nissan',
    'model': 'Skyline',
    'year': 1989,
    'colour': 'blue'
}
# So we will use an if statement to see whether or not this specific key is here or not
if 'colour' in cars:
    print (f'Yes it appears we do have our colour selected from our user.')
else:
    print ('It appears the user has not provided a colour for the selected car')
    # Since there is the key colours within the dictionary, we know for certain that it would appear true
print ('####################')
# We can even change the desired values within the dictionaries as we place, since dictionaries are changeable
cars['colour'] = 'red'
# What we've done above is changed the value in the key cataogry colour to the value red instead of blue
print (cars)
# As we know we can not have duplicates within a dictionary, so the data instead will be updated to red rather than blue
print ('####################')
# We cam of course use the (update) command as well to essentially do the same thing as well
cars.update({'colour': 'black'})
# This is of course another way of doing this with the use of the (update)
print (cars)
# There are ways to remove items with a specified key name
print ('####################')
# What the command is for this is (pop) which is used to remove the item specifically
cars.pop('year')
# As you can see what we've done essentially is pop out the key year and all of its values
print (cars)
# There is another comamand with the use of (pop)
print ('####################')
# Its called popitem() you essentially code it very similarly to the actual command pop
cars.popitem()
# What this does, is it removes the last inserted item within the dictionary
print (cars)
# As shown it removed the last item within the dictionary which was the colour
print ('####################')
# We can also clear the entire directory with the (clear) command as shown below
cars.clear()
# If we were to print this, we wouldn't get any values or keys back
print (cars)
# You would only get the curly brackets at the end which is essentially no value
print ('####################')
# But to remove it completely we can simply use the del() command
del cars
# If we printed this out it wouldn't work out all, since the entire directory is completely deleted
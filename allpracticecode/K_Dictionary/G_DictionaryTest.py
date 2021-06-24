# Now lets look at more complex dictionaries
countries = {
    'country_one': {
        'name': 'United Kingdom',
        'capital': 'London',
        'continent': 'Europe'
    },
    'country_two': {
        'name': 'China',
        'capital': 'Beijing',
        'continent': 'Asia'
    },
    'country_three': {
        'name': 'Ethiopia',
        'capital': 'Addis Ababa',
        'continent': 'Africa'
    }
}
# This is what we call a nested loop, holding dictionaries within the dictionary itself
print ('####################')
# Lets see what it will output when we print it out
print (countries)
# What intersting is that dictionaries can interact with each other as well
country_one = {
    'name': 'United Kingdom',
    'capital': 'London',
    'continent': 'Europe'
}
country_two = {
    'name': 'China',
    'capital': 'Beijing',
    'continent': 'Asia'
}
country_three = {
    'name': 'Ethiopia',
    'capital': 'Addis Ababa',
    'continent': 'Africa'
}
# Now what we've done here, is made the dictionaries individual here instead of them in one dictionary
three_countries = {
    'country_one': country_one,
    'country_two': country_two,
    'country_three': country_three
}
# And we can essentially turn it into an entire dictionary right here
print ('####################')
# Sp lets see if it does the same thing
print (three_countries)

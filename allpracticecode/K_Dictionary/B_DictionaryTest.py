# Now lets look into more of the basic characteristics of a dictionary
phone = {
    'brand': 'Huawei',
    'type': 'Honor Play',
    'colour': 'blue',
    'colour': 'red'
}
# We know that we can change the contents within a dictionary but we can't duplicate
print (phone)
# Meaning that the last key and value provided will overright the previous one
print ('####################')
# What about the representation of a dictionary length?
phone_two = {
    'brand': 'Apple',
    'type': 'iphone 12',
    'colour': 'chrome'
}
# We simply can find out when we use the length command (len)
print (len(phone_two))
# So the numerical value we would get is 3 since, we are looking at the values here, not the keys
print ('####################')
# What about can it use all datatypes? For dictionaries yes, they can store all datatypes
headphones = {
    'brand': 'Razor',
    'wireless': False,
    'year': 2021
}
# As you can see we are using an integer, boolean and string within this dictionary.
print (headphones)
# But what if we wanted to figure out what datatype this dictionary is?
print (type(headphones))
# Well within the perspective of python, it would be defined as dict
# Python percieves a tuple as a object called you guest it, a tuple
atuple = ('Mexico','Paraguay','Sweden')
print(type(atuple))
# What we get is as you gest it, the class of this variable is a tuple
atuple_two = tuple(('Bolivia','Brazil','Portugal','Spain'))
print (atuple_two)
# What we are doing above is we are assigning the variable and actually making it a tuple
print ('####################')
#As of which allows us to constructs tuples, which is what its generally called
days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
# Now lets have some fun with these tuples
today = ('Wednesday')

count = 0

if today  == days[2]:
    print (f'It appears today is within the tupla variable, as shown here {days[2]}')
    print ('####################')
    count = count + 1
    if count == 1:
        print ('Now lets see if this has Sunday and Monday, just to test this tuple')
        print ('####################')
        if 'Monday' == days[0] and 'Sunday' == days [6]:
            print (f'Now we know that this tuple has {days[0]} as well as {days[6]}')


else:
    print (f'It unfortunately seems that {today} is not within the tuple')


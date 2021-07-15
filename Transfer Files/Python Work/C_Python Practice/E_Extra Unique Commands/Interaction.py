# Now I want to test whether or not we can interact with the bash so why not try it?
name = input('Please provide your first name and surname, ')
# The input command allows the terminal to help you provide a response in ensuring and additional input
age = int(input('Additionally please provide your age as well, '))
# What int does is it makes sure whatever the use inputs in changes it to a integer for it to fully operate
if age >= 18:
    print ("You are an adult.")
else: # We then want to see whether or not the code will interact properly, so lets see if it does
    print ("You are young.")
# It appears to work successfully, which is good for us!
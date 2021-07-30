# We first of all need to import this function in order for it to operate
import sys
# Now what I want to do here is essentially experiment with the the exporting of an output to an outside folder
sys.stdout = open('test.txt','w')
# What we are doing here is within this specific region we will be jumping these files in a txt document
print ('Good Morning')
# The 1st line of code is doing exactly that, opening a text file and allowing us to write for 'w'
sys.stdout.close()
# We then close the file and save what we've essentially added, lets see if this works

# Now if we look at the testfile it was able to work successfully!
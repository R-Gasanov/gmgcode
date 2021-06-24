import sys
# The command above, provides the neccesary means for me to store data into files, which we are specifically using within this round of work
import boto3
# Meanwhile what boto3 does, is that it allows me to use python commands that are specifically orientes to AWS
print ('###########################################')
# This is my project to try and obtain the databases that we don't specifically need within the datbase in aws
print ('These are some of the Databases')
# As shown below, we are using one of boto3 commands, which essentially means we will be using the command lines in aws athena
client = boto3.client('athena')
# Below what we are doing here is that we are listing the databases from the catalog AwsDataCatalog
response = client.list_databases(CatalogName = 'AwsDataCatalog')
# Lets see what we get here, when we print this information out now shall we?
db_list = response.get('DatabaseList')
# But first, we need to use the (get) command in order for us to actually visable see whats in the contents of DatabaseList
print (db_list)
# As we can tell this is specifically a dictionary for us as of which to use
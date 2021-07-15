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
# Now what we have here below is a variety of lists for us to catagories the tables we will be keeping and removing
tables_to_keep = []
tables_to_remove = []
# We are using functions since essentially what we will be doing here is sifting throught the various amounts of data and taking the things we actually need and want
def my_function(tablename):
# Here is where we define my function
    if tablename.endswith('_gz') or tablename.startswith('0') or tablename.startswith('1') or tablename.startswith('2'):
        tables_to_remove.append(tablename)
        # Within the If statement what we are essentially doing here is specifying that we would want to keep these specific files instead of the other
    else:
        tables_to_keep.append(tablename)
        # And with the rest that do not follow the specific condition will append to the tablename instead
db_list = response.get('DatabaseList')
# What we are doing here is essentially, we will be extracting the names from the DatabaseList, that is enslisted in AwsDataCatalog
for dbn in db_list:
    name = dbn.get('Name')
    # What we are doing here, is that we are looking through db_list, and we are trying to specifically get out the Name key from the dictionary
    print (name)
    md = client.list_table_metadata(
        CatalogName = 'AwsDataCatalog',
        DatabaseName = name
    )
    tmd = md.get('TableMetadataList')
    # What we are doing here is that we are specifically getting the metadata table we need to catagories the CatalogName which is AwsDataCatalog, while the DatabaseName would be the name specifically
    for mdn in tmd:
        mtn = mdn.get('Name')
        my_function(mtn)
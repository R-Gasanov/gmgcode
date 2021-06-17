import sys
# The command above, provides the neccesary means for me to store data into files, which we are specifically using within this round of work
import boto3
# Meanwhile what boto3 does, is that it allows me to use python commands that are specifically orientes to AWS
print ('###########################################')
# This is my project to try and obtain the databases that we don't specifically need within the datbase in aws
print ('These are some of the Databases')
# As shown below, we are using one of boto3 commands, which essentially means we will be using the command lines in aws athena
client = boto3.client('athena')

# Now what we have here below is a variety of lists for us to catagories the tables we will be keeping and removing

dictionary_keep = {
    'name': '',
    'tablename': ''
}
dictionary_remove = {
    'name': '',
    'tablename': ''

}
# We are using functions since essentially what we will be doing here is sifting throught the various amounts of data and taking the things we actually need and want
def my_function(tablename):
# Here is where we define my function
    return tablename.endswith('_gz') or tablename.startswith('0') or tablename.startswith('1') or tablename.startswith('2')

def process_database(name):
    next_token = None
    tables_to_remove = []
    tables_to_keep = []

    md = client.list_table_metadata(
        CatalogName = 'AwsDataCatalog',
        DatabaseName = name
    )
    tmd = md.get('TableMetadataList')
    dictionary_keep['name'] = (name)
    dictionary_remove['name'] = (name)
    # What we are doing here is that we are specifically getting the metadata table we need to catagories the CatalogName which is AwsDataCatalog, while the DatabaseName would be the name specifically
    for mdn in tmd:
        mtn = mdn.get('Name')
        if my_function(mtn):
            tables_to_remove.append(mtn)
        else:
            tables_to_keep.append(mtn)
            while True:
                Kwargs = {
                        'CatalogName':'AwsDataCatalog'
                         }
                if next_token is not None:
                    Kwargs['NextToken'] = next_token
                    response_two = client.list_databases(
                            **Kwargs
                            )
                    next_token = response_two.get('NextToken')
                elif next_token is None:
                    break


        # And with the rest that do not follow the specific condition will append to the tablename instead
    return {
        'db_name': name,
        'tables_to_remove': tables_to_remove,
        'tables_to_keep': tables_to_keep,
    }




# Below what we are doing here is that we are listing the databases from the catalog AwsDataCatalog
response = client.list_databases(CatalogName = 'AwsDataCatalog')
db_list = response.get('DatabaseList')
# What we are doing here is essentially, we will be extracting the names from the DatabaseList, that is enslisted in AwsDataCatalog
for dbn in db_list:
    name = dbn.get('Name')
    # headphones['colour'] = 'green'
    # What we are doing here, is that we are looking through db_list, and we are trying to specifically get out the Name key from the dictionary
    print (f'#########{name}#########')
    # result = process_database(name)
    result = process_database(name)
    count = 0
    print(result['db_name'])
    for keep in result['tables_to_keep']:
        count = count+1
        print (keep)
    print (f'We have {count} databases we want to keep.')
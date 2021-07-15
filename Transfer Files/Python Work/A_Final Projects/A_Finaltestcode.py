import sys
import boto3

print ('###########################################')

print ('These are some of the Databases')

client = boto3.client('athena')

response = client.list_databases(CatalogName = 'AwsDataCatalog')
tables_to_keep = []
tables_to_remove = []

next_token = None
def my_function(tablename):

    if tablename.endswith('_gz') or tablename.startswith('0'or'1'or'2'):
        tables_to_remove.append(tablename)
    else:
        tables_to_keep.append(tablename)

db_list = response.get('DatabaseList')
for dbn in db_list:
    name = dbn.get('Name')
    print (name)
    md = client.list_table_metadata(
        CatalogName = 'AwsDataCatalog',
        DatabaseName = name
    )
    for mdn in md:
        tmd = md.get('TableMetadataList')
        for mdn_two in tmd:
            mtn = mdn_two.get('Name')
            my_function(mtn)

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
print ('###########################################')

count = len(tables_to_remove)

num = len(tables_to_keep)

print (f'We have found {count} tables that we would want to remove.')
print (f'We have found {num} tables that we would want to keep.')

print ('###########################################')

condition = 1

while condition == 1:

    request = input('Would you like to look at the following tables (Y/N)?')

    if request == 'Y':

        tablerequest = int(input('Which table would you like to look at? Type 1 for tables to keep or 2 for tables to remove'))

        if tablerequest == 1:
            for tablename in tables_to_keep:
                print (tablename)

        elif tablerequest == 2:
            for tablename in tables_to_remove:
                print (tablename)

    elif request == 'N':
        print ('Thank you for using my program')
        condition = condition + 1


import sys

sys.stdout = open('Tables.txt','w')

print ('################################################################################')
print (f'We have found {num} tables that we would want to keep.')
print ('################################################################################')
for tablename in tables_to_keep:
    print (tablename)

print ('###############################################################################')
print (f'We have found {count} tables that we would want to remove.')
print ('###############################################################################')
for tablename in tables_to_remove:
    print (tablename)

sys.stdout.close()







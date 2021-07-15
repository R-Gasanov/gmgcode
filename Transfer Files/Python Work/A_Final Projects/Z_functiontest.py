import boto3

client = boto3.client('athena')

response = client.list_databases(CatalogName = 'AwsDataCatalog')
tables_to_keep = []
tables_to_remove = []

next_token = None
def my_function(tablename):

    if tablename.endswith('_gz'):
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
                print (f'Next token is {next_token}')
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

count = len(tables_to_remove)

print(f'Found {count} tables to remove!')

print (f'These are the tables I want to keep')
for tablename in tables_to_keep:
    print (tablename)


for tablename in tables_to_remove:
    print (tablename)
import boto3

client = boto3.client('athena')

response = client.list_databases(CatalogName = 'AwsDataCatalog')

next_token = None
def my_function(tablename):

    gz = filter(my_function,'gz')
    print (f'Here is a list of gz: {gz}')
    print (f'Here is the function: {tablename}')
    return False

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
            print (f'TABLE_NAME: {mtn}')

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
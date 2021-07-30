import boto3

client = boto3.client('codecommit')

response = client.get_comments_for_pull_request(
    pullRequestId = "65"
)
print (response)
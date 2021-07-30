import boto3

client = boto3.client('codecommit')

#def convert_pr_comments_to_gerrit():
response = client.get_comments_for_pull_request(
    pullRequestId = "65"
)
    
cc_comments = response['commentsForPullRequestData']
for comments in cc_comments:
    location = comments['location']
    feedback = comments['comments']

filepath = location.get('filePath')
fileposition = location.get('filePosition')

print (type(filepath))
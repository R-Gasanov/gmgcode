import boto3

client = boto3.client('codecommit')

response = client.get_comments_for_pull_request(
    pullRequestId = "65"
)

cc_comments = response['commentsForPullRequestData']
content = str()
feedback = []
for comments in cc_comments:
    location = comments['location']
    feedback = feedback + comments['comments']
for commentdata in feedback:
    content = content + "|" + commentdata.get('content')
print (content)


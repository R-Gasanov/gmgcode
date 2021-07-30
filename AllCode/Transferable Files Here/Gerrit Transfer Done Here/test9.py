import boto3

def converter(string):
    split = list(string.split("|"))
    return split

client = boto3.client('codecommit')

response = client.get_comments_for_pull_request(
    pullRequestId = "65"
)

cc_comments = response['commentsForPullRequestData']
content = str()
fileposition = []
feedback = []
for comments in cc_comments:
    location =  comments['location']
    #fileposition = fileposition + location.get('filePosition')
    feedback = feedback + comments['comments']
    #print (fileposition)
    fileposition.append((location.get('filePosition')))
    
for commentdata in feedback:
    content = content + "|" + commentdata.get('content')

statement = (converter(content))

while("" in statement) :
    statement.remove("")
print (statement)
print (fileposition)
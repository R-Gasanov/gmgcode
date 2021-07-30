import boto3

def converter(string):
    split = list(string.split("|"))
    return split

client = boto3.client('codecommit')


def convert_pr_comments_to_gerrit():
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
        repositoryname = comments.get('repositoryName')
    filepath = location.get('filePath')
    for commentdata in feedback:
        content = content + "|" + commentdata.get('content')

    statement = (converter(content))
    
    while("" in statement) :
        statement.remove("")
    #print (statement)
    #print (fileposition)


    gerrit_comment =  {
    "tag": repositoryname,
    "comments": {
        filepath: [
            {
                "line": '',
                "message": '',
            }
            ]
        }
      }
  
    for line in fileposition:
        gerrit_comment['line'] = (line)
    for message in statement:
        gerrit_comment['message'] = (message)
  
    return (gerrit_comment)

output = convert_pr_comments_to_gerrit()
print (output)

#dictionary_keep['name']
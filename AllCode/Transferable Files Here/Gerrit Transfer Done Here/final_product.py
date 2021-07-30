import boto3

client = boto3.client('codecommit')

def convert_pr_comments_to_gerrit():
    response = client.get_comments_for_pull_request(
        pullRequestId = "65"
    )
    
    cc_comments = response['commentsForPullRequestData']
    for comments in cc_comments:
        location = comments['location']
        feedback = comments['comments']
        repositoryname = comments.get('repositoryName')
    for commentdata in feedback:
        content = commentdata.get('content')
        commentid = commentdata.get('commentId')

    filepath = location.get('filePath')
    fileposition = location.get('filePosition')
    #content = feedback.get('content')
    # commentid = feedback(f'commentId{[0]}')
    
    
    gerrit_comment =  {
    "tag": repositoryname,
    "comments": {
        filepath: [
            {
                "line": fileposition,
                "message": content,
            }
            ]
        }
      }
  
    return (gerrit_comment)
        
        
    
    
    
    #return response
output = convert_pr_comments_to_gerrit()
print (output)
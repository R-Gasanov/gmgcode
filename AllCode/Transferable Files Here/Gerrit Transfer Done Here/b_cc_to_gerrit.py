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
        for filelocation in location:
            filepath = filelocation.get('filePath')
            fileposition = filelocation.get('filePosition')
            for commentdata in feedback:
                content = commentdata.get('content')
                commentid = commentdata.get('commentId')
    
    gerrit_comment = {
        'repositoryName': repositoryname,
        'filepath': filepath,
        'fileposition': fileposition,
        'comments': {
            'commentId': commentid,
            'comment': content
        }
        
    }
    
    return (gerrit_comment)
        
        
    
    
    
    #return response
output = convert_pr_comments_to_gerrit()
print (output)
import json
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
    
    output_comments = {}
    
    for comments in cc_comments:
        location =  comments['location']
        #fileposition = fileposition + location.get('filePosition')
        feedback = feedback + comments['comments']
        #print (fileposition)
        fileposition.append((location.get('filePosition')))
        repositoryname = comments.get('repositoryName')
        
        filepath = location.get('filePath')
        input_file_comments = comments['comments']
        
        output_file_comments = output_comments.get(filepath, [])
        
        for input_file_comment in input_file_comments:
            output_file_comments.append({
                'line': location['filePosition'],
                'message': input_file_comment['content']
            })
        
        output_comments[filepath] = output_file_comments
        
    
    gerrit_comment =  {
        "tag": repositoryname,
        "comments": output_comments
     }
  
    return (gerrit_comment)

output = convert_pr_comments_to_gerrit()
print (json.dumps(output))

#dictionary_keep['name']
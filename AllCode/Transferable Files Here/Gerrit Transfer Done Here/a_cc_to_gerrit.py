# https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#set-review
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_pull_request

# pr_id

import logging
import boto3
import pprint

client = boto3.client('codecommit')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
pp = pprint.PrettyPrinter(indent=4)

def convert_pr_comments_to_gerrit():

    response = client.get_comments_for_pull_request(
        pullRequestId = "65"
    )

    cc_comments = response['commentsForPullRequestData']

    gerrit_comments = {}

    for comment in cc_comments:
        print(comment)
        repositoryName = comment.get('repositoryName')
        fileposition = comment.get('filePosition')
        content = comment.get('content')
        commentId = comment.get('commentId')






result = convert_pr_comments_to_gerrit()

pp.pprint(result)






#for messages in response:
#    comments = messages.get('comments')
#print (comments)


#"""Retrieves comments from a pull request in CodeCommit
#and converts them into the format required to post these comments
#to gerrit.
#
 #   Returns a dictionary that can be used as a payload to the set-review
 #   call.

 #   """
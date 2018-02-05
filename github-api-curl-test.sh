# # Get Root Endpoints
# curl --request GET \
#   --url https://api.github.com/
#
# # Get Content
# curl --request GET \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/contents/FILE-PATH
#
# # Create Content
# curl --request PUT \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/contents/FILE-PATH \
#   --header 'authorization: token MY-TOKEN' \
#   --data '{
#   "message": "commit from INSOMNIA",
#   "content": "MY-CONTENT-ENCODED-BASE64"
# }'
# 
# 
# # Update Content
# curl --request PUT \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/contents/FILE-PATH \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "message": "update from INSOMNIA",
#   "content": "MY-CONTENT-ENCODED-BASE64", 
#   "sha": "CONTENT-SHA"
# }
# '
# 
# # Delete Content
# curl --request DELETE \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/contents/FILE-PATH \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "message": "delete a file",
#   "sha": "CONTENT-SHA"
# }'
# 
# # Create Issue
# curl --request POST \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/issues \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "title": "Creating issue from API",
#   "body": "Posting a issue from Insomnia"
# }'
# 
# # Edit Issue
# curl --request PATCH \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/issues/ISSUE-NUMBER \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "title": "Creating issue from API(updated title)",
#   "body": "Posting a issue from Insomnia \n\n Updated from insomnia.",
#   "state": "open"
# }'
# 
# # Lock Issue
# curl --request PUT \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/issues/ISSUE-NUMBER/lock \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "locked": true,
#   "active_lock_reason": "too heated"
# }'
# 
# # Unlock Issue
# curl --request DELETE \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/issues/ISSUE-NUMBER/lock \
#   --header 'authorization: token MY-TOKEN'
# 
# # Create Comment
# curl --request POST \
#   --url https://api.github.com/repos/solomonxie/USER-NAME/REPO-NAME/issues/ISSUE-NUMBER/comments \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "body": "Create a comment from INSOMNIA"
# }'
# 
# # Create Comment with Image
# curl --request POST \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/issues/ISSUE-NUMBER/comments \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "body": "Create a comment with picture from Insomnia \n\n ![img](https://user-images.githubusercontent.com/14041622/35807698-77cf55d8-0abe-11e8-9677-59f2961b5b0f.png)"
# }'
# 
# # Edit Comment
# curl --request PATCH \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/issues/comments/COMMENT-ID \
#   --header 'authorization: token MY-TOKEN' \
#   --header 'content-type: application/json' \
#   --data '{
#   "body": "Create a comment from INSOMNIA \n\n ----updated"
# }'
# 
# # Delete Comment
# curl --request DELETE \
#   --url https://api.github.com/repos/USER-NAME/REPO-NAME/issues/comments/COMMENT-ID \
#   --header 'authorization: token MY-TOKEN'

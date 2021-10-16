#######################################################################
#                      LOCAL SECRETS GENERATION                       #
#######################################################################

echo > /tmp/env.txt
echo GH_USER="solomonxie" >> /tmp/env.txt
echo GH_NAME="$(git config --global user.name)" >> /tmp/env.txt
echo GH_EMAIL="$(git config --global user.email)" >> /tmp/env.txt
echo GH_TOKEN="$(cat ~/.ssh/github_token.txt)" >> /tmp/env.txt

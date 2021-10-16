#!/usr/bin/sh
#######################################################################
#             THIS SCRIPT RUNS INSIDE OF DOCKER CONTAINER             #
#######################################################################

# ENV check: requires specific Environment variables
if [ "${GH_USER}" == "" ] || \
   [ "${GH_NAME}" == "" ] || \
   [ "${GH_EMAIL}" == "" ] || \
   [ "${GH_TOKEN}" == "" ] || \
   false;
then
    echo [ FAILED. ] Environment variables are not set ===========
    exit 127
fi

mkdir -p /root/.ssh

# Copy ssh-keys from host
# echo "${ID_RSA}" > /root/.ssh/id_rsa
# echo "${ID_RSA_PUB}" > /root/.ssh/id_rsa.pub
# chmod 700 /root/.ssh/id_rsa
# chmod 700 /root/.ssh/id_rsa.pub

# Set github user for commit
git config --global user.name "${GH_USER}"
git config --global user.email "${GH_EMAIL}"

# Add github host
cat <<- EOF >> /root/.ssh/config
Host github.com
    StrictHostKeyChecking no
EOF
touch /root/.ssh/known_hosts
ssh-keyscan github.com >> /root/.ssh/known_hosts

# start cron
/usr/bin/crontab /Gitissues/crontab.txt
# /usr/sbin/crond -f -l 8
# /usr/sbin/crond -fd 0


#######################################################################
#     IMPORTANT - THIS KEEPS ENTRY ON FOREGROUND TO MAKE -d WORKS     #
#######################################################################
# tail -f /dev/null
# /usr/sbin/crond -f -l 8
/usr/sbin/crond -fd 0

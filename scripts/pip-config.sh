echo """[global]
index-url=https://${AZ_DEVOPS_FEED_NAME}:${AZ_DEVOPS_TOKEN}@pkgs.dev.azure.com/${AZ_DEVOPS_ORG_NAME}/${AZ_DEVOPS_PROJECT_NAME}/_packaging/${AZ_DEVOPS_FEED_NAME}/pypi/simple/
""" > /etc/pip.conf
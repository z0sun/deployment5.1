# Deployment 5.1
### By Joseph White
---

## Purpose

This deployment aims to deploy a Banking Flask application to EC2 instances using a Jenkins agent. AWS cloud infrastructure is deployed using Terraform, setting up a Jenkins CI/CD server and two Web application servers running Gunicorn, Python, and SQLite code.
---
## Steps

1. Using the Terraform [main.tf][https://github.com/z0sun/deployment5.1/blob/main/main.tf] file build the aws infrastructure containing:

* 1 VPC
* 2 AZ's
* 2 Public Subnets
* 3 EC2s (The application instances should be in their own subnet)
* 1 Route Table
* Security Group Ports: 8080, 8000, 22

2. On the first instance install both [python][https://github.com/z0sun/runit/blob/main/pythoninstall.sh] and [jenkins][https://github.com/z0sun/runit/blob/main/jenkins.sh](This will be a multibranch pipeline build). On the second instance only install Jenkins.

4. Clone Repository and Integrate Jenkins:
`git clone https://github.com/kura-labs-org/c4_deployment-5.1.git
cd c4_deployment-5.1/
git init
git remote set-url origin https://github.com/z0sun/deployment5.1.git
git fetch
git push --mirror
git branch second
git switch second
#make edits to the Jenkinsfile
git commit -a
git push --set-upstream origin second
#Run Jenkins build
git switch main
git merge second
git push`

During this step edits to the Jenkins file were split between two branches and in order for the Jenkins agents to work in the next step `awsDeploy` and `awsDeploy2` tags were used in the Jenkins agents configuration. The repo was split into a [Main][https://github.com/z0sun/deployment5.1/blob/second/Main%20Branch.png] and a [Second][https://github.com/z0sun/deployment5.1/blob/second/Second%20Branch.png] branch. 

6. In this build two Jenkins agents were utilized on each instance the application was deployed on. Here are the steps to create your nodes:
`    Select "Build Executor Status"
    Click "New Node"
    Choose a node name that will correspond with the Jenkins agent defined in our Jenkins file
    Select permenant Agent
    Create the node
    Use the same name for the name field
    Enter "/home/ubuntu/agent1" as the "Remote root directory"
    Use the same name for the labels field
    Click the dropdown menu and select "only build jobs with label expressions matching this node"
    Click the dropdown menu and select "launch agent via SSH"
    Enter the public IP address of the instance you want to install the agent on, in the "Host" field
    Click "Add" to add Jenkins credentials
    Click the dropdown menu and select "Select SSH username with private key"
    Use the same name for the ID field 
    Use "ubuntu" for the username
    Enter directly & add a private key by pasting it into the box
    Click "Add" and select the Ubuntu credentials
    Click the dropdown menu and select "non-verifying verification strategy"
    Click save & check in Jenkins UI for a successful installation by clicking "Log"`
[Jenkins Agents][https://github.com/z0sun/deployment5.1/blob/main/Nodes.png]

Both Applications deployed on both instances successfully. [Jenkins Builds][https://github.com/z0sun/deployment5.1/blob/main/Successful%20Main.png, https://github.com/z0sun/deployment5.1/blob/main/Second%20Build%20Success%20.png]

[Applications][https://github.com/z0sun/deployment5.1/blob/main/Application1.png, https://github.com/z0sun/deployment5.1/blob/main/Application2.png]


---
## Issues

* There was an error within the requirements.txt file, `sudo apt update` and `sudo apt upgrade` resolved those issues. [Error][https://github.com/z0sun/deployment5.1/blob/main/Pip%20install%20error.png] 

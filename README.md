# Deployment 5.1
### By Joseph White
---

## Purpose

The purpose of this deployment is to deploy a Banking Flask application to EC2 instances using a Jenkins agent. AWS cloud infrastructure is deployed using Terraform, setting up a Jenkins CI/CD server and two Web application servers running Gunicorn, Python, and SQLite code.
---
## Steps

1. Using the Terraform [main.tf][https://github.com/z0sun/deployment5.1/blob/main/main.tf] file build the aws infrastructure containing:

`* 1 VPC
* 2 AZ's
* 2 Public Subnets
* 3 EC2s (The application instances should be in their own subnet)
* 1 Route Table
* Security Group Ports: 8080, 8000, 22`


---
## Issues

* There was an error within the requirements.txt file, `sudo apt update` `sudo apt upgrade` resolved those issues. [Error][https://github.com/z0sun/deployment5.1/blob/main/Pip%20install%20error.png] 

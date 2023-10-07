<p align="center">
<img src="https://github.com/kura-labs-org/kuralabs_deployment_1/blob/main/Kuralogo.png">
</p>

## Deployment Instructions:
1. Create a VPC with Terraform and the VPC **MUST** have only the components listed below:
    - 1 VPC
    - 2 AZ's
    - 2 Public Subnets
    - 2 EC2's
    - 1 Route Table
    - Security Group Ports: 8080, 8000, 22
    - Only 1 instance per subnet    
2. For the first instance follow the below instructions:
```
- Install Jenkins
- Install the following plugin: “Pipeline Keep Running Step”
- Set up Jenkins agent {Follow the scribe link after you've created an ssh key on the second instance}
```
3. On the second instance, install the following:
```
- Create a public and private key on this instance with ssh-keygen
- Copy the contents of the private key and save it somewhere
- Install the following: {default-jre, nginx, software-properties-common, sudo add-apt-repository -y ppa:deadsnakes/ppa, python3.7, python3.7-venv}
- Set up nginx (Review Repo 4 or your documentation for set up)
```
4. Now follow the Jenkins agent scribe: link
5. Create a Jenkins multibranch pipeline and run the Jenkinsfile 
6. Check the application on the second instance!!
7. Now make a change to the HTML
8. Set up email notifications in Jenkins and a monitoring agent
9. Redeploy the application 
10. How is the server performing?
11. Would you need to run the agent build and application on another server?
12. Which instance should be in a private subnet? Should both instances be in a private subnet? Why?


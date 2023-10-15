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
    - Only 1 application instance per subnet
    - One Jenkins imstance   
2. For the Jenkins instance follow the below instructions:
```
- Install Jenkins
- Install the following plugin: “Pipeline Keep Running Step”
- Set up Jenkins agent {Follow the scribe link after you've created an ssh key on the second instance}
```
3. On the 2 instances, install the following:
```
- Create a public and private key on this instance with ssh-keygen
- Copy the contents of the private key and save it somewhere
- Install the following: {default-jre, nginx, software-properties-common, sudo add-apt-repository -y ppa:deadsnakes/ppa, python3.7, python3.7-venv}
- Set up nginx (Review Repo 4 or your documentation on Nginx setup)
```
4. Now follow the Jenkins agent scribe: link
5. Create a Jenkins multibranch pipeline and run the Jenkinsfile (Change the agent name in the Jenkinsfile to deploy to the second instance) 
6. Check the application!!
7. What should be added to the infrastructure to make it more available?
8. Which instance should be in a private subnet? Should both instances be in a private subnet? Why?


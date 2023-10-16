<p align="center">
<img src="https://github.com/kura-labs-org/kuralabs_deployment_1/blob/main/Kuralogo.png">
</p>

## Deployment Instructions:
1. When you create the new instances, first create a new key pair in AWS, save the .pem file on your computer, and attach the new key to all your instances
2. Create a VPC with Terraform and the VPC **MUST** have only the components listed below:
    - 1 VPC
    - 2 AZ's
    - 2 Public Subnets
    - 3 EC2's
    - 1 Route Table
    - Security Group Ports: 8080, 8000, 22
    - Only 1 application instance per subnet 
3. For the Jenkins instance follow the instructions below:
```
- software-properties-common, sudo add-apt-repository -y ppa:deadsnakes/ppa, python3.7, python3.7-venv}
- Install the following plugin: “Pipeline Keep Running Step”
- Set up Jenkins agent {Follow the scribe link after you've created an SSH key on the second and third instance}
```
4. On the 2 instances, install the following:
```
- Install the following: {default-jre, software-properties-common, sudo add-apt-repository -y ppa:deadsnakes/ppa, python3.7, python3.7-venv}
```
5. Jenkins agent scribe: [link](https://scribehow.com/shared/Step-by-step_Guide_Creating_an_Agent_in_Jenkins__xeyUT01pSAiWXC3qN42q5w)
6. Create a Jenkins multibranch pipeline and run the Jenkinsfile 
7. Check the application!!
8. Now figure out how to deploy the application on the third instance
9. What should be added to the infrastructure to make it more available?
10. Which instance (Jenkins and application servers) should be in a private subnet? Should both instances be in a private subnet? Why?


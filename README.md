# AWS Cloud DevOps Capstone Project

## Introduction

This project is for applying the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

* Working in AWS
* Using Jenkins to implement Continuous Integration and Continuous Deployment
* Building pipelines
* Working with CloudFormation to deploy clusters
* Building Kubernetes clusters
* Building Docker containers in pipelines

### Project steps

Step 1: Propose and Scope the Project

* Deploying a simple web application (url shortener) to AWS EKS cluster.
* Using Jenkins to build, test and deploy the application.
* Using rolling update strategy to update the web app.
  
Step 2: Use Jenkins and implement rolling deployment.

* Setting github repository with 3 branches (dev, uat and prod).
* Setting up EC2 Instance for Jenkins.
* Configure Jenkins plugins and credentials.

![Jenkins](https://i.imgur.com/OlGQLzP.png)
  
Step 3: Build AWS Kubernetes as a Service (EKS) Kubernetes cluster.

* Using eksctl to create a cluster using the configuration file (./eks/eks-config.yml)

![Cloud Formation](https://i.imgur.com/lIKYqdI.png)
  
Step 4: Build your pipeline

* Construct your pipeline in your GitHub repository.
* Set up all the steps that your pipeline will include.
* Configure a deployment pipeline.
* Include your Dockerfile/source code in the Git repository.
* Include with your Linting step both a failed Linting screenshot and a successful Linting screenshot to show the Linter working properly.

Fail linting step:
![Failed linting step](https://i.imgur.com/cfJ9eZj.png)

Successful linting step:
![Success Linting Step](https://i.imgur.com/W3mEM8T.png)

Step 5: Test your pipeline

* Perform builds on your pipeline.
* Verify that your pipeline works as you designed it.
* Take a screenshot of the Jenkins pipeline showing deployment.

Blue version of the webapp:

![Blue Version](https://i.imgur.com/XfofELd.png)

Aprroval step to deploy to production:

![Deployment Approval](https://i.imgur.com/BKBqGr8.png)

Rollout Status:

![Rollout update Status](https://i.imgur.com/HpFKw6L.png)

Green version of the webapp:

![Green Version](https://i.imgur.com/pjQHYhl.png)

#### Find me in social media

[![Github](https://img.shields.io/badge/-Github-black?style=flat&labelColor=black&logo=github&logoColor=white "Github")](https://github.com/ahmed-gharib89 "Github")
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white "LinkedIn")](https://www.linkedin.com/in/agharib89/ "LinkedIn")
[![Facebook](https://img.shields.io/badge/-Facebook-informational?style=flat&labelColor=informational&logo=facebook&logoColor=white "Facebook")](https://www.facebook.com/a.gharib89/)
[![Whatsapp](https://img.shields.io/badge/-Whatsapp-brightgreen?style=flat&labelColor=brightgreen&logo=whatsapp&logoColor=whiteg "Whatsapp")](https://wa.me/201096995535?text=Hello)
[![Instagram](https://img.shields.io/badge/-Instagram-c13584?style=flat&labelColor=c13584&logo=instagram&logoColor=white "Instagram")](https://www.instagram.com/ahmed.gharib89/)

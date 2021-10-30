pipeline{
    agent any
    environment {
        DOCKER_IMAGE_NAME = "agharib/url-short"
    }
    stages{
        stage("Installing Requirments"){
            steps{
                echo "========executing Installing Requirments========"
                withPythonEnv('python3') {
                    sh "make install"
                }
            }
            post{
                success{
                    echo "========Installing Requirments executed successfully========"
                }
                failure{
                    echo "========Installing Requirments execution failed========"
                }
            }
        }
        stage("Formating the code with black"){
            steps{
                echo "========executing Formating the code with black========"
                withPythonEnv('python3') {
                    sh "make format"
                }
            }
            post{
                success{
                    echo "========Formating the code with black executed successfully========"
                }
                failure{
                    echo "========Formating the code with black execution failed========"
                }
            }
        }
        stage("Linting"){
            steps{
                echo "========executing Linting========"
                withPythonEnv('python3') {
                    sh "make lint"
                }
            }
            post{
                success{
                    echo "========Linting executed successfully========"
                }
                failure{
                    echo "========Linting execution failed========"
                }
            }
        }
        stage("Testing the code"){
            steps{
                echo "========executing Testing the code========"
                withPythonEnv('python3') {
                    sh "make test"
                }
            }
            post{
                success{
                    echo "========Testing the code executed successfully========"
                }
                failure{
                    echo "========Testing the code execution failed========"
                }
            }
        }
        stage("Displaying Test Report"){
            steps{
                echo "========executing Displaying Test Report========"
                withPythonEnv('python3') {
                    sh "make test-report"
                }
            }
            post{
                success{
                    echo "========Displaying Test Report executed successfully========"
                }
                failure{
                    echo "========Displaying Test Report execution failed========"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    app = docker.build(DOCKER_IMAGE_NAME)
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-login') {
                        app.push("V1.0.${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
    }
    post{
        success{
            echo "========pipeline executed successfully ========"
            checkout( [$class: 'GitSCM', branches: [[name: 'dev']], 
                       extensions: [[$class: 'PreBuildMerge', options: [mergeRemote: 'origin', mergeTarget: 'uat']],
                       [$class: 'AuthorInChangelog']], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/ahmed-gharib89/AWS-Cloud-DevOps-Engineer-Capstone-Project']]])        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}
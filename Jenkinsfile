pipeline{
    agent any
    environment {
        DOCKER_IMAGE_NAME = "agharib/url-short"
    }
    stages{
        stage("Installing Requirments"){
            when {
                branch 'dev'
            }
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
            when {
                branch 'dev'
            }
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
            when {
                branch 'dev'
            }
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
            when {
                branch 'dev'
            }
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
            when {
                branch 'dev'
            }
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
            when {
                branch 'dev'
            }
            steps {
                script {
                    app = docker.build(DOCKER_IMAGE_NAME)
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'dev'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-login') {
                        app.push("v1.0.${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage("Replace image version with build number"){
            steps{
                echo "====++++executing Replace image version with build number++++===="
                script {
                    def buildNumber = Jenkins.instance.getItem('urlshort').getItem('dev').lastSuccessfulBuild.number
                    echo "====++++Build Number is $buildNumber++++===="
                    sh "sed -i -E '12s/(.+?)\\.[0-9]+/\\1\\.$buildNumber/' urlshort-chart/values.yaml"
                    sh "cat urlshort-chart/values.yaml"
                }
            }
            post{
                success{
                    echo "====++++Replace image version with build number executed successfully++++===="
                }
                failure{
                    echo "====++++Replace image version with build number execution failed++++===="
                }
        
            }
        }
        stage("Replace App version in chart.yml"){
            steps{
                echo "====++++executing Replace App version in chart.yml++++===="
                script {
                    def buildNumber = Jenkins.instance.getItem('urlshort').getItem('dev').lastSuccessfulBuild.number
                    echo "====++++Build Number is $buildNumber++++===="
                    sh "sed -i -E '6s/(.+?)\\.[0-9]+/\\1\\.$buildNumber/' urlshort-chart/Chart.yaml"
                    sh "cat urlshort-chart/Chart.yaml"
                }
            }
            post{
                success{
                    echo "====++++Replace App version in chart.yml executed successfully++++===="
                }
                failure{
                    echo "====++++Replace App version in chart.yml execution failed++++===="
                }
        
            }
        }
        stage("Deploy to UAT environment"){
            when {
                branch 'uat'
            }
            steps{
                echo "====++++executing Deploy to UAT environment++++===="
                withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                    withKubeConfig([credentialsId: 'kubeconfig']) {
                        sh 'helm upgrade urlshort urlshort-chart --namespace uat'
                    }
                }
            }
            post{
                success{
                    echo "====++++Deploy to UAT environment executed successfully++++===="
                    withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                        withKubeConfig([credentialsId: 'kubeconfig']) {
                            sh '''
                                URL=$(kubectl get svc -n uat | grep elb.amazonaws | awk '{print $4}')
                                curl -X GET http://$URL/_status/healthz
                            '''
                        }
                    }
                }
                failure{
                    echo "====++++Deploy to UAT environment execution failed++++===="
                }
            }
        }
        stage("Deploy to Production environment"){
            when {
                branch 'main'
            }
            steps{
                input 'Deploy to Production?'
                echo "====++++executing Deploy to Production environment++++===="
                withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                    withKubeConfig([credentialsId: 'kubeconfig']) {
                        sh 'helm upgrade urlshort urlshort-chart --namespace production'
                    }
                }
            }
            post{
                success{
                    echo "====++++Deploy to UAT environment executed successfully++++===="
                    withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                        withKubeConfig([credentialsId: 'kubeconfig']) {
                            sh '''
                                URL=$(kubectl get svc -n production | grep elb.amazonaws | awk '{print $4}')
                                curl -X GET http://$URL/_status/healthz
                            '''
                        }
                    }
                }
                failure{
                    echo "====++++Deploy to Production environment execution failed++++===="
                }
            }
        }
    }
    post{
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}
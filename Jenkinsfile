pipeline{
    agent any
    environment {
        DOCKER_IMAGE_NAME = "agharib/url-short"
    }
    stages{
        stage("Installing Requirments"){
            steps{
                echo "========executing Installing Requirments========"
                sh "make install"
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
                sh "make format"
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
                sh "make lint"
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
                sh "make test"
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
                sh "make test-report"
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
                branch 'master'
            }
            steps {
                script {
                    app = docker.build(DOCKER_IMAGE_NAME)
                    app.inside {
                        sh 'ls -la'
                    }
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
        stage("PLACE_HOLDER"){
            steps{
                echo "========executing PLACE_HOLDER========"
            }
            post{
                success{
                    echo "========PLACE_HOLDER executed successfully========"
                }
                failure{
                    echo "========PLACE_HOLDER execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}
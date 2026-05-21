pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python Syntax Test...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build & Deploy') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    def appImage = docker.build("flask-cicd-app:latest", ".")
                    
                    echo 'Stopping old container if exists...'
                    sh 'docker stop flask-app-container || true'
                    sh 'docker rm flask-app-container || true'
                    
                    echo 'Running new container...'
                    appImage.run("-d -p 5000:5000 --name flask-app-container")
                }
            }
        }
    }
}
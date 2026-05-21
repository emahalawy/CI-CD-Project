pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t flask-cicd-app:latest .'
            }
        }
        stage('Deploy Container') {
            steps {
                echo 'Deploying Application...'
                sh 'docker stop flask-app-container || true'
                sh 'docker rm flask-app-container || true'
                
                sh 'docker run -d -p 5000:5000 --name flask-app-container flask-cicd-app:latest'
            }
        }
    }
}
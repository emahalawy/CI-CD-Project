pipeline {
    agent any

    stages {
        // 1. سحب الكود من GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // 2. البناء والتشغيل مباشرة (الـ Dockerfile كفيل باختبار وبناء الكود)
        stage('Build & Deploy') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t flask-cicd-app:latest .'
                
                echo 'Stopping old container if exists...'
                sh 'docker stop flask-app-container || true'
                sh 'docker rm flask-app-container || true'
                
                echo 'Running new container...'
                sh 'docker run -d -p 5000:5000 --name flask-app-container flask-cicd-app:latest'
            }
        }
    }
}
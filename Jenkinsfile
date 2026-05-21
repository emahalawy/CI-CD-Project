pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t flask-app-image .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'docker run --rm flask-app-image pytest test_app.py'
            }
        }

        stage('Deploy (Container)') {
            steps {
                echo 'Deploying Application as Container...'
 
                sh 'docker rm -f flask-app-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-app-container flask-app-image'
            }
        }
    }
}
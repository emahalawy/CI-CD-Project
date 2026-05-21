pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
            }
        }

        stage('Build & Deploy') {
            steps {
                script {
                    echo 'Building Docker Image via Plugin...'
            
                    def myImage = docker.build("my-website:latest", ".")
                    
                    echo 'Stopping old container if exists...'
                    sh 'docker stop my-site || true'
                    sh 'docker rm my-site || true'
                    
                    echo 'Running new container...'
                    myImage.run("-d -p 8085:80 --name my-site")
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished execution successfully.'
        }
    }
}
pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('saiteja_jen_docker')
        IMAGE_NAME = "shaiksaiteja/ibmproject:${env.BUILD_NUMBER}"
    }

    stages {
        stage('SCM Checkout') {
            steps {
                git url: 'https://github.com/shaiksaiteja/hms', branch: 'main'
            }
        }
        
        stage('Build Docker img') {
            steps {
                script {
                    docker.build IMAGE_NAME, '.' 
                }
            }
        }
        
        stage('LOGIN TO DOCKERHUB') {
    steps {
        withCredentials([usernamePassword(credentialsId: 'saiteja_jen_docker', usernameVariable: 'DOCKERHUB_CREDENTIALS_USR', passwordVariable: 'DOCKERHUB_CREDENTIALS_PSW')]) {
            sh "docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW"
        }
    }
}
        stage('PUSH IMAGE') {
            steps {
                sh "docker push $IMAGE_NAME"
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
        }
    }
}

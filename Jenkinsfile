pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('saiteja_jen_docker')
        IMAGE_NAME = "shaiksaiteja/finalsemproject:${env.BUILD_NUMBER}"
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
 sh             "docker push $IMAGE_NAME"
                // Run the Docker container after pushing the image
                sh "docker run -p 8000:8000 $IMAGE_NAME", returnStatus: true  }
        }
    }
    
    post {
        always {
            sh 'docker logout'
        }
    }
}

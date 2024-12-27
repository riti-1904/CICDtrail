pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\pasar\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\pasar\\AppData\\Local\\Programs\\Python\\Python312\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Set the PATH and install dependencies using pip
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
            }
        }
        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token') // Accessing the SonarQube token stored in Jenkins credentials
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                
                //sonar-scanner -Dsonar.projectKey=RitikaCICDtest ^
                              // -Dsonar.sources=. ^
                              // -Dsonar.host.url=http://localhost:9000 ^
                              // -Dsonar.token=%SONAR_TOKEN%


                              set PATH=%PYTHON_PATH%;%PATH%
                              sonar-scanner -Dsonar.projectKey=RitikaCICDtest ^
                              -Dsonar.sources=. ^
                              -Dsonar.host.url=http://localhost:9000 ^
                              -Dsonar.token=sqp_34760008e0fda02e341b30ea61a614c1be3505ec
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}

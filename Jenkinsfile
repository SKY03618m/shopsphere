// ==============================================================================
// ShopSphere - Declarative Jenkins CI/CD Pipeline
// Project: Distributed Commerce Platform: A DevOps-Driven E-Commerce Application
// ==============================================================================

pipeline {
    agent any

    environment {
        APP_NAME     = 'shopsphere'
        IMAGE_NAME   = "shopsphere:${BUILD_NUMBER}"
        IMAGE_LATEST = "shopsphere:latest"
        PYTHON_CMD   = 'python'
    }

    stages {
        stage('1. Checkout SCM') {
            steps {
                echo '=== Stage 1: Checking out source code from GitHub ==='
                checkout scm
            }
        }

        stage('2. Environment & Dependencies') {
            steps {
                echo '=== Stage 2: Verifying Python & Installing Dependencies ==='
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('3. Automated Testing (Pytest)') {
            steps {
                echo '=== Stage 3: Executing Pytest Test Suite ==='
                sh '''
                    python3 -m pytest -v --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results.xml'
                }
            }
        }

        stage('4. Docker Build & Image Packaging') {
            steps {
                echo "=== Stage 4: Building Docker Image ${IMAGE_NAME} ==="
                sh """
                    docker build -t ${IMAGE_NAME} -t ${IMAGE_LATEST} .
                """
            }
        }

        stage('5. Deploy to Kubernetes (Minikube)') {
            steps {
                echo '=== Stage 5: Deploying ShopSphere to Kubernetes Cluster ==='
                sh '''
                    # Apply Kubernetes manifests
                    kubectl apply -f k8s/configmap.yaml
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml

                    # Verify rollout status
                    kubectl rollout status deployment/shopsphere-deployment --timeout=120s
                '''
            }
        }
    }

    post {
        success {
            echo '======================================================'
            echo ' [SUCCESS] ShopSphere Pipeline executed successfully! '
            echo ' Continuous Integration & Deployment Complete.        '
            echo '======================================================'
        }
        failure {
            echo '======================================================'
            echo ' [FAILURE] ShopSphere Pipeline encountered an error.   '
            echo ' Please inspect stage logs and test reports.           '
            echo '======================================================'
        }
        always {
            cleanWs deleteDirs: true, notFailBuild: true
        }
    }
}

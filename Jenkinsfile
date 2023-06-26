pipeline {
    agent none
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd assign_2
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd assign_2
                python -m unittest test_main.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SOURHEAD/python-unittest-for-jenkinjob.git']])
            }
        }
        stage('Build') {
            steps {
                sh '''pip3 install requests
                python3 -m unittest tests.py'''
            }
        }
    }
}

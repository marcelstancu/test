pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/marcelstancu/test', branch: 'main')
      }
    }

    stage('Shell Script') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Install Golang') {
      steps {
        sh '''apt update
wget https://go.dev/dl/go1.19.6.linux-amd64.tar.gz
tar -C /usr/local/ -xzf go1.19.6.linux-amd64.tar.gz
ls /usr/local/'''
      }
    }

  }
}
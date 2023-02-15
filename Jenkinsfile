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

  }
}
pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/marcelstancu/test', branch: 'main')
      }
    }

    stage('Import proxy') {
      steps {
        sh '''export http_proxy=http://proxy-dmz.intel.com:912 &&
export https_proxy=http://proxy-dmz.intel.com:912
'''
      }
    }

  }
}
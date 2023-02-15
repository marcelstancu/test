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

    stage('Curl something from internet') {
      steps {
        sh 'curl https://ww1.prweb.com/prfiles/2010/06/17/4161594/2_Getty04.jpg && ls -la'
      }
    }

  }
}
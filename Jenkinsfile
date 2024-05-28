

pipeline {
    agent {
      docker {
        image 'python:3'

      }
    }

    stages {
        stage('build') {
when {
       not { branch 'master'
       }
   }
      steps {
      sh 'apt-get install python3'
      sh 'apt install python3-pip'
        sh 'python3 --version'
        sh 'source venv/Scripts/activate'
      }
    }
        stage('Test') {
        when {
       not {           branch 'master'
       }
   }
            steps {

                sh """
              python --version
              python ./test.py
              """
            }
        }
    }
}


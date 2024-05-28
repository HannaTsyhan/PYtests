

pipeline {
    agent any


    stages {
        stage('build') {
when {
       not { branch 'master'
       }
   }
      steps {
        sh 'python3 --version'
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


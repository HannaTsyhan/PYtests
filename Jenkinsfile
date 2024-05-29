pipeline {
    agent any


    stages {
        stage('build') {
when {
       not { branch 'master'
            }
     }
      steps {

      sh 'pip install pymssql'
        sh 'python3 --version'
        sh 'python ./test.py'
      }
    }
        stage('Test') {
        when {
       not { branch 'master'
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
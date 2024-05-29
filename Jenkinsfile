pipeline {
    agent any


    stages {

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
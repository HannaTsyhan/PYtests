pipeline {
    agent any


    stages {


        stage('Test') {
        when {
       not { branch 'master'
           }
             }
            steps {
                withPythonEnv('/usr/bin/python3.11'){
                        sh """
                      python --version
                      python ./test.py
                      """
                      }
                }
        }
    }
}
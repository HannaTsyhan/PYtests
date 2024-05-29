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
                      pytest  /var/jenkins_home/workspace/Py_tests_HW_5/testSQL.py
                      """
                      }
                }
        }
    }
}
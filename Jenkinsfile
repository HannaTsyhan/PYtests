pipeline {
    agent any


    stages {


        stage('Build') {
            withPythonEnv('/usr/bin/python3.11'){
                sh "pip install pytest-html"
            }
        }



        stage('Test') {
            steps {
                withPythonEnv('/usr/bin/python3.11'){
                        sh """
                      python --version
                      pytest  /var/jenkins_home/workspace/Py_tests_HW_5/testSQL.py
                      --html=report.html
                      """
                      }
                }
        }
    }
}
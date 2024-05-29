pipeline {
    agent any

    triggers {
        githubPush()
    }


    stages {


        stage('Build') {
         steps {
                withPythonEnv('/usr/bin/python3.11'){
                    sh "pip install pytest-html"
                }
            }
        }

        stage('Test') {
            steps {
                withPythonEnv('/usr/bin/python3.11'){
                        sh """
                      python --version
                      pytest  /var/jenkins_home/workspace/Py_tests_HW_5/testSQL.py
                      """
                      }
                }
        }

        stage('Report') {
            steps {
                withPythonEnv('/usr/bin/python3.11'){
                        sh """
                      pytest  --html=report.html
                      """
                      }
                }
        }
    }
}
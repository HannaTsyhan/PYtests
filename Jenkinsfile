pipeline {
    agent any

    triggers {
        githubPush()
    }


    stages {


        stage('Build') {
                        when {
                   not { branch 'master'
                       }
                }
         steps {
                withPythonEnv('/usr/bin/python3.11'){
                    sh "pip install pytest-html"
                    sh "pip install pymssql"
                }
            }
        }

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

        stage('Report') {
                        when {
                   not { branch 'master'
                       }
                }
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
pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Build') {
         steps {
                withPythonEnv('/usr/bin/python3.11'){
                    sh """
                        python --version
                        pip install pytest-html
                        pip install pymssql
                    """
                }
            }
        }

        stage('Test') {
            steps {
                withPythonEnv('/usr/bin/python3.11'){
                        sh """

                      pytest  /var/jenkins_home/workspace/Py_tests_HW_5/testSQL.py
                      """
                      }
                }
        }

         stage('Completed') {
                        when {
                               { branch 'main'
                                   }
                            }
            steps {
                        sh """
                       echo "Completed"
                      """
                }
        }
    }
}
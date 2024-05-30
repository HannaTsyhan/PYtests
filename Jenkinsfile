pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

         stage('Github') {
             steps {
                      sh "git status"
                }
        }

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

         stage('Create release') {
             when {
                    expression {
                          env.BRANCH_NAME == 'master'
                          }
                    }
            steps {
                       sh '''
                           git clone https://github.com/HannaTsyhan/PYtests.git --branch release
                           git checkout release
                           git push
                       '''
                }
        }
    }
}

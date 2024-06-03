pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

         stage('Github') {
                 when {
                    expression {
                          env.GITHUB_PR_STATE == "CLOSE"
                          }
                 }
             steps {

                      sh "git status"
                      sh "echo 'PR was merged'"
                }
        }

        stage('Build') {
             steps {
                    withPythonEnv('/usr/bin/python3.11'){
                        sh """
                            python --version
                            pip install pytest-html
                            pip install pymssql
                            echo '$env.GITHUB_PR_STATE'
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
    expression {
      env.BRANCH_NAME == 'dev' || env.BRANCH_NAME == 'main'
      }
  }
            steps {
                       sh '''

                        mkdir repo && cd repo
                        git init
   git config --global user.email "you@ahoo.com"
  git config --global user.name "My Name"
                        git clone https://github.com/HannaTsyhan/PYtests.git && cd PYtests
                        git add .
                        git checkout -b release
                        git remote set-url origin https://HannaTsyhan:${TOKEN}@github.com/HannaTsyhan/PYtests.git
                        git push --set-upstream origin release
                       '''
                }
        }
    }
}
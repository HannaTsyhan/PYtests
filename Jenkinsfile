

pipeline {
    agent any

    stages {
        stage('Setup') {
            steps{
                script {
                    sh 'python3 --version'
                    sh 'pip --version'
                    sh 'python3 -m venv venv'
                    sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt'''

                        }
                   }
                        }
        stage('build') {
when {
       not { branch 'master'
           }
      }
      steps {
      echo 'Building...'
            }
    }
        stage('Test') {
        when {
       not {  branch 'master'
           }
             }
            steps {

                sh """
             . venv/bin/activate
             pytest
              """
            }
        }
    }
}


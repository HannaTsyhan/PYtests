pipeline {
    agent any


    stages {
        stage('build') {
when {
       not { branch 'master'
            }
     }
      steps {
      sh 'su -S <<< "1111" -c "apt-get install python3-pip"'
      sh 'pip install pymssql'
        sh 'python3 --version'
        sh 'python ./test.py'
      }
    }
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
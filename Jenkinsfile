

pipeline {
    agent any

    stages {
        stage('build') {
when {
       not {           branch 'master'
       }
   }
      steps {
        bat 'python --version'

      }
    }
        stage('Test') {
        when {
       not {           branch 'master'
       }
   }
            steps {
                bat 'pip install -r requirements.txt'
                bat 'make check || true'
                bat 'pytest ./testSQL.py'
                bat 'pytest testSQL.py --html=report.html'
            }
        }
    }
}



pipeline {
    agent any

    stages {
        stage('build') {
when {
       not {           branch 'master'
       }
   }
      steps {
        sh 'python --version'

      }
    }
        stage('Test') {
        when {
       not {           branch 'master'
       }
   }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'make check || true'
                sh 'pytest ./testSQL.py'
                sh 'pytest testSQL.py --html=report.html'
            }
        }
    }
}

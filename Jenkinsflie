

pipeline {
    agent any

    stages {
        stage('build') {
when {
       not {           branch 'master'
       }
   }
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
        stage('Test') {
        when {
       not {           branch 'master'
       }
   }
            steps {
                sh 'make check || true'
                sh 'pytest ./testSQL.py'
                sh 'pytest testSQL.py --html=report.html'
            }
        }
    }
}



pipeline {
    agent any

    stages {
        stage('build') {
when {
       not {           branch 'master'
       }
   }
      steps {
      bat 'sudo apt-get install python3'
                bat 'sudo apt install python3-pip'

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



pipeline {
    agent any

    stages {
        stage('build') {
when {
       not { branch 'master'
       }
   }
      steps {
      sh 'sudo apt-get install python3'
      sh 'sudo apt install python3-pip'
        sh 'python3 --version'
        sh 'source venv/Scripts/activate'
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

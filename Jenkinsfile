pipeline {
    agent any

    stages{
        stage('checkout code'){
            steps {
                git credentialsId: 'pathelloworld' , url : "https://github.com/kimjisoo22/admin.git" , branch : 'master'
            }
        }
        stage('install Dependencies') {
            steps{
                bat ''' 
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirement.txt
                    '''
            }
        }

        stage('run test'){
            steps {
                bat '''
                    call venv\\Scripts\\activate 
                    pytest test_log.py
                    '''
            }
        }
        stage('deploy') {
            steps {
                echo "Deploying application..."

                bat '''
                    call venv\\Scripts\\activate
                    python mem_login.py
                    '''
            }
        }
    }   

    post{
        success {
            echo 'pipeline succeeded'
        }
        failure {
            echo 'pipeline failed'
        }
    }
}
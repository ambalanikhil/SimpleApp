pipeline {
    environment {
    imagename = "backend"
    jenkinsProject = 'calculator-webapp-backend'
  }

    agent any
    stages {

        stage('Git Staging'){

            steps{

                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-cred', url: 'https://github.com/ambalanikhil/SimpleApp.git']]])

            }
        }


        stage('Build image') {

            steps{
                sh 'sudo su - jenkins -s/bin/bash'
                //sh 'sudo docker stop $imagename'
                //sh 'sudo docker rm $imagename'
                //sh 'sudo docker rmi $imagename'
                sh 'sudo docker image build -t  $imagename .'

            }

        }
        stage('Run Tests') {
            steps {
                sh 'sudo docker run --rm $imagename pytest test_app.py'
            }
        }
        
        stage('Run image ') {

            steps{
                sh 'sudo docker run -p5000:5000 --restart=always --name $imagename  -itd $imagename'

            }

        }
        

        
    }
}

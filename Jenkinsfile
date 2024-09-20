pipeline {
    environment {
    imagename = "backend"
    jenkinsProject = 'calculator-webapp-backend'
  }

    agent any
    stages {

        stage('SourceCode CheckOut'){

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
        // stage('Trivy Scan') {
           // steps {
                // Run Trivy to scan the Docker image for vulnerabilities
             //   sh 'trivy image --exit-code 1 --severity HIGH,CRITICAL $imagename'
            //}
       // }

        stage('Run image ') {

            steps{
                // Stop and remove any existing container with the same name
                sh 'sudo docker stop $imagename || true' // Ignore error if container isn't running
                sh 'sudo docker rm $imagename || true'   // Ignore error if no container exists
                // Run the Flask application
                sh 'sudo docker run -p5000:5000 --restart=always --name $imagename  -itd $imagename'

            }

        }
        

        
    }
}

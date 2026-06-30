pipeline{
    agent any;
    stages{
        stage("Clone"){
            steps{
                git url: "https://github.com/mujawarsaad/flask-app", branch: "main"
            }
        }
        stage("Build"){
            steps{
                sh "docker build -t flaskapp ."
            }
        }
        stage("Push"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: "dockerHubCreds",
                    usernameVariable: "dockerHubUser",
                    passwordVariable: "dockerHubPass")]){
                    sh 'echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin'
                    sh 'docker image tag flaskapp:latest $dockerHubUser/flaskapp:latest'
                    sh 'docker push $dockerHubUser/flaskapp:latest'
                }
            }
        }
        stage("Deploy"){
            steps{
                sh 'docker run -d -p 5000:5000 flaskapp'
            }
        }
    }
}

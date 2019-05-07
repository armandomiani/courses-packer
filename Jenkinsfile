ansiColor('xterm') {
    node {
        stage('Checkout') {
            // Clean the workspace
            cleanWs()

            // Get some code from a GitHub repository
            checkout scm
        }
        stage('Setup') {
            dir('05_jenkins/') {
                sh "ansible-galaxy install -r requirements.yml"
            }
        }
        stage('Validate') {
            dir('05_jenkins/') {
                sh "packer validate jenkins.json"
            }
        }
        stage('Build') {
            withCredentials([usernamePassword(credentialsId: '685d64a9-34bb-4f23-ac5d-0bdf62c9cf8e', usernameVariable: 'AWS_ACCESS_KEY', passwordVariable: 'AWS_SECRET_KEY')]) {
                dir('05_jenkins/') {
                    sh "packer build -var 'aws_region=us-east-2' jenkins.json"
                }
            }
        }
        stage('Store Artifacts') {
            dir('05_jenkins/') {
                archiveArtifacts 'manifest.json'
            }
        }
    }
}
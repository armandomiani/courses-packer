ansiColor('xterm') {
    dir('04_tests/') {
        node {
            stage('Checkout') {
                // Clean the workspace
                cleanWs()

                // Get some code from a GitHub repository
                checkout scm
            }
            stage('Setup') {
                dir('04_tests/') {
                    sh "ansible-galaxy install -r requirements.yml"
                }
            }
            stage('Validate') {
                sh "packer validate 11_tests.json"
            }
            stage('Build') {
                withCredentials([usernamePassword(credentialsId: 'aws_access_keys', usernameVariable: 'AWS_ACCESS_KEY', passwordVariable: 'AWS_SECRET_KEY')]) {
                // Run the packer build
                    sh "packer build -var 'aws_region=us-east-2' 11_tests.json"
                }
            }
            stage('Store Artifacts') {
                archiveArtifacts 'manifest.json'
            }
        }
    }
}
ansiColor('xterm') {
    node {
        stage('Checkout') {
            // Clean the workspace
            cleanWs()

            // Get some code from a GitHub repository
            checkout scm
        }
        stage('Setup') {
            sh "ansible-galaxy install -r requirements.yml"
        }
        // stage('Validate') {
        //     // dir "04_tests"
        //     sh "packer validate 11_tests.json"
        // }
        // stage('Build') {
        //     withCredentials([usernamePassword(credentialsId: 'aws_access_keys', usernameVariable: 'AWS_ACCESS_KEY', passwordVariable: 'AWS_SECRET_KEY')]) {
        //     // Run the packer build
        //         sh "packer build -var 'aws_region=us-east-2' 11_tests.json"
        //     }
        // }
        // stage('Store Artifacts') {
        //     archiveArtifacts 'manifest.json'
        // }
    }
}
/*******************************************************************************
 * DJ Joe Calendar Build Automation
 *
 * Build, Deploy, and Share the Full-Page Calendar
 ******************************************************************************/

node ('x86-32-build') {

    // Build in the DJ Joe Application Server
    checkout scm


    // Provide Credentials to Support Spotify Client
    withCredentials([
        string(credentialsId: 'GOOGLE_API_KEY',
        variable: 'GOOGLE_API_KEY')
    ]) {

        testPython()

        buildContainer()

        pushContainer()
    }
}


// Test Python Scripts
def testPython() {
    stage("Test Python") {
        // Install Python Requirements
        sh "python3 -m pip install --upgrade --no-cache-dir -r test/pytest-requires.txt"

        // Run Tests
        sh "python3 -m pytest"
    }
}


// Build the Application
def buildContainer() {
    stage("Build Container") {
        sh "docker build -t engineerjoe440/full-page-calendar:latest ."
    }
}


// Push the Application Container to Docker-Hub
def pushContainer() {
    stage("Push Container") {
        sh "docker push engineerjoe440/full-page-calendar:latest"
    }
}
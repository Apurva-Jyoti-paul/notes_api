pipeline {
 environment {
  appName = "server"
  registry = "apurvajpaul/flipr"
  registryCredential = "fliprRegistry"
  projectPath = "/jenkins/data/workspace/django-server"
 }

 agent any

 parameters {
  gitParameter name: 'RELEASE_TAG',
   type: 'PT_TAG',
   defaultValue: 'master'
 }

 stages {

  stage('Basic Information') {
   steps {
    sh '''
    echo tag: ${params.RELEASE_TAG}
    echo "hello"
    '''
   }
  }
  }

  


}

def getBuildName() {
 "${BUILD_NUMBER}_$appName:${params.RELEASE_TAG}"
}

def isMaster() {
 "${params.RELEASE_TAG}" == "master"
}
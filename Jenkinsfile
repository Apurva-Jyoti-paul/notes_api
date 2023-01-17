pipeline {
 environment {
  appName = "server"
  registry = "apurvajpaul/flipr"
  registryCredential = "fliprRegistry"
  projectPath = "/jenkins/data/workspace/djangoenn"
 }

 agent any

 parameters {
  gitParameter name: 'RELEASE_TAG',
   type: 'PT_TAG',
   defaultValue: 'v1.0.3'
 }

 stages {

  stage('Basic Information') {
   steps {
    sh "echo tag: ${params.RELEASE_TAG}"
   }
  }

  stage('Build Image') {
   steps {
    script {
     if (isMaster()) {
      dockerImage = docker.build "$registry:latest"
     } else {
      dockerImage = docker.build "$registry:${params.RELEASE_TAG}"
     }
    }
   }
  }

  stage('Deploy Image') {
   steps {
    script {
      docker.withRegistry("https://registry.hub.docker.com", registryCredential) {
      dockerImage.push()
      }
    }
   }
  }

  stage('DeployToProd')
  {
    steps{
      script{
  sshagent(credentials : ['prod']) {

  def release="${params.RELEASE_TAG}"
  sh '''
 echo ''' + release + ''' 
 ssh -t -t api@54.85.69.14 -o StrictHostKeyChecking=no "pwd"
  '''
     }
      }
    }
  }

  stage('Garbage Collection') {
   steps {
    sh "docker rmi $registry:${params.RELEASE_TAG}"
    sh "docker image prune -a -f"
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
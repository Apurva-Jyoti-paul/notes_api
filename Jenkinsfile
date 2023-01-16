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
   defaultValue: 'v1.0.0'
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

//   stage('Check Lint') {
//    steps {
//     sh "docker run --rm $registry:${params.RELEASE_TAG} flake8"
//    }
//   }

//   stage('Run Tests') {
//    steps {
//     sh "docker run -v $projectPath/reports:/app/reports  --rm --network='host' --env-file=.test.env $registry:${params.RELEASE_TAG} coverage run -m pytest --verbose --junit-xml reports/results.xml"
//    }
//   }

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
  sh 'ssh -t -t api@54.85.69.14 -o StrictHostKeyChecking=no "ls"'
     }
      }
    }
  }

  stage('Garbage Collection') {
   steps {
    sh "docker rmi $registry:${params.RELEASE_TAG}"
    sh "docker image prune -a"
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
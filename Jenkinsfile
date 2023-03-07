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
   defaultValue: 'latest'
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
stage('Packing AMI')
{
    steps {
      script{
        withAWS(credentials:'aws-key',region:'us-east-1'){
        sh """
        packer build ./Iaas/packer.json
        """
        EC2_AMI_ID = sh(returnStdout: true, script: "cat manifest.json | jq -r '.builds[0].artifact_id' | cut -d: -f2").trim()
        sh """
        echo ${EC2_AMI_ID}
        """
        }
        }
      }
}
  // stage('DeployToProd')
  // {
  //   steps{
  //     script{
  // sshagent(credentials : ['prod']) {

  // def release="${params.RELEASE_TAG}"
  // sh '''
  // ssh -t -t api@54.85.69.14 -o StrictHostKeyChecking=no "./prodDeploy.sh $registry:"'''+release+'''""
  // '''
  //    }
  //     }
  //   }
  // }
   stage('Deploy to EC2') {
      steps {
        script {
           withAWS(credentials:'aws-key',region:'us-east-1'){

    sh """
     aws ec2 run-instances \
    --image-id ${EC2_AMI_ID} \
    --count 1 \
    --instance-type t2.micro \
    --key-name prod \
    --security-group-ids sg-03c91b5cba5bc22fe \
    --subnet-id subnet-0602ea70b8096f0c5 \
    --block-device-mappings "[{\"DeviceName\":\"/dev/sdf\",\"Ebs\":{\"VolumeSize\":10,\"DeleteOnTermination\":false}}]" \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=production}]' 'ResourceType=volume,Tags=[{Key=Name,Value=demo-server-disk}]'
          """
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
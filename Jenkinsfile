def runshell(cmd){
    sh('#!/bin/sh -e\n' + cmd)
}

pipeline
{
agent any 

 stages{
     
     stage(cleanWorkspace){
         steps{
            deleteDir() 
         }
     }
     
     
     stage(checkout){
         steps{
             checkout([$class: 'GitSCM',
             branches: [[name: '*/main']],
             userRemoteConfigs: [[credentialsId: '******************************', url:'https://github.com/deepakchandra1096/Mercedes_Code.git']]])
         }
     }
     
     
     
     
     stage(build){
         steps{
             script{
                sh label: '', script:'''#!/bin/bash
                set -x
                docker build -t mercedes:${BUILD_NUMBER} .
                
                ''' 
             }
        }
    }

stage(Deployment){
         steps{
             script{
                sh label: '', script:'''#!/bin/bash
                set -x

                docker run -d --name mercedes mercedes:${BUILD_NUMBER}

                docker cp `docker container ps | awk '{ print $1,  $NF }' | grep -w mercedes | awk '{print $1}'`:/app/user_data.xlsx /tmp/

                echo "User data has been saved to user_data.xlsx."

                ''' 
             }
        }
    }     

stage(Cleanup){
         steps{
             script{
                sh label: '', script:'''#!/bin/bash
                set -x
                docker container stop mercedes
                docker container rm mercedes
                docker rmi mercedes:${BUILD_NUMBER}
                
                ''' 
             }
        }
    }     
     
 }
}

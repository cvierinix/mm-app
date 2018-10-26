def dockerRegistry = 'https://registry.hub.docker.com'
def dockerRegistryCredKey = 'docker-registry'
def dockerRepo = 'cvierinix'

if ( env.BRANCH_NAME == 'master' ) {
    k8s_env = 'prod'
} else if ( env.BRANCH_NAME == 'develop' ) {
    k8s_env = 'dev'
} else {
    k8s_env = 'dev'
}


node () {
  stage('Preparation') {
    checkout([
      $class: 'GitSCM',
      branches: scm.branches,
      extensions: scm.extensions + [[$class: 'LocalBranch'], [$class: 'CleanCheckout']],
      userRemoteConfigs: scm.userRemoteConfigs,
    ])
  }

  stage('Dockerize') {
    docker.withRegistry(dockerRegistry, dockerRegistryCredKey) {
      def serviceImage = docker.build("${dockerRepo}/app:${env.BRANCH_NAME}-latest")
      serviceImage.push()
    }
  }

  stage('Deploy') {
    sh "helm upgrade --recreate-pods --install --timeout 240 --wait --namespace ${k8s_env} -f helm/environment/${k8s_env}/mm-app.yaml mm-app-${k8s_env} helm/charts/mm-app/"
  }

  deleteDir()
}


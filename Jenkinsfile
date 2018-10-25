def dockerRegistry = 'docker.io'
def dockerRegistryCredKey = 'docker-registry'
def dockerRepo = 'cvierinix'


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

  deleteDir()
}


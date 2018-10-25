def dockerRegistry = 'https://index.docker.io'
def dockerRegistryCredKey = 'docker-registry'
def dockerRepo = 'app'


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
      def serviceImage = docker.build("${dockerRepo}/cvierinix/app:${env.BRANCH_NAME}-latest")
      serviceImage.push()
    }
  }

  deleteDir()
}


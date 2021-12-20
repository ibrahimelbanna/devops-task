# Diagram of the end-to-end solution
![Diagram of the end-to-end solution](https://github.com/ibrahimelbanna/devops-task/raw/main/banq-misr.drawio.png)
# Vagrant setup
cd vagrant-provisioning && vagrant up  

# Prerequisites steps of the minio server
- kubectl create namespace minio-tenant-1 
# Insllalocal path provissioner
- kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
# Install of krew 
- (
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
- export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
# Install of minio  
- kubectl krew install minio
- kubectl minio init
- kubectl get pods -n minio-operator
- kubectl minio tenant create tenant1 --servers 1 --volumes 4 --capacity 10Gi --namespace  minio-tenant-1 --storage-class local-path
# And I have created a bash script file to instlal minio diectlry and automate the steps of the installation. 
# Proxy minio client
- kubectl minio proxy -n minio-operator
# Create a bucket under your tanent and a user.
- And replace them in the code 
- build the image 
- docker build -t ibrahimmohamed/minio_uploader:latest . 
# Deploy our application:
- kubectl apply -f deployment.yml -n app
- kubectl apply -f minio_service.yml -n minio-operator 
# AutoScaler for the pod"
kubectl autoscale deployment  --cpu-percent=50 --min=1 --max=10 -n app

# Jenkins
- kubectl create namespace devops-tools 
- kubectl apply -f serviceAccount.yaml
- kubectl apply -f deployment.yaml -n devops-tools
- kubectl apply -f jenkins-service.yaml  -n devops-tools
- Head to http://172.16.16.100:32000/ to install it and create admin user
- create a multibranch pipeline for our project



# User Rescources in this exercise: 
- https://devopscube.com/setup-jenkins-on-kubernetes-cluster/ 
- https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-kubernetes
- https://github.com/minio/operator/blob/master/README.md
- https://docs.min.io/docs/python-client-quickstart-guide.html
- https://thenewstack.io/how-minio-brings-object-storage-service-to-kubernetes/
- https://www.magalix.com/blog/create-a-ci/cd-pipeline-with-kubernetes-and-jenkins
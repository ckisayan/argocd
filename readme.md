go to azure portal and create AKS
then in vscode connect to az
az account clear
az login
az aks get-credentials -g rg-akscluster -n aks-cki-training or
az aks get-credentials -g rg-aks-py-argoCD -n pyargocd

run a sample command
kubectl get svc
kubectl get nodes to make sure you are connected

https://argoproj.github.io/

go to ArgoCD getting started
https://argo-cd.readthedocs.io/en/stable/

create a namespace
kubectl create namespace argocd

copy below to your local folder.  You can install from internet but it will always get latest and you don't have control over versions
https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


now lets deploy
kubectl -n argocd apply -f .\argo\argo-cd\install.yaml

create github repo
commit your code
create applicaiton.yaml

run below to see what is out there
kubectl -n argocd get pods


kubectl port-forward svc/argocd-server -n argocd 8080:443


to login to argo cd
https://localhost:8080/
advance-proceed

how to get pwd for admin user
kubectl get secret argocd-initial-admin-secret -n argocd -o yaml

S2lQc3hQQk5lOXloMFJVaw==

base64 decode above
KiPsxPBNe9yh0RUk

now create app
kubectl apply -n argocd -f .\argo\argo-cd\app.yaml

go back to ui
you should see app

workflows
https://argoproj.github.io/argo-workflows/quick-start/
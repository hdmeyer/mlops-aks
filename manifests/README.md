build

```sh
kustomize build ./manifests/ | kubectl apply -f -
```

port-forward

```sh
kubectl port-forward service/employee-attrition-service 8443:8000
```

testing 

```sh
curl 127.0.0.1:8443
```
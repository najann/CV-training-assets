kubectl delete service api
kubectl delete deployment api
docker build -t  us.icr.io/comvis/tfjs_api:latest .
docker push us.icr.io/comvis/tfjs_api:latest 
kubectl apply -f api-deployment.yaml,api-service.yaml
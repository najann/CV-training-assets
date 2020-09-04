kubectl delete service web
kubectl delete deployment web
docker build -t  us.icr.io/comvis/tfjs:latest .
docker push us.icr.io/comvis/tfjs:latest 
kubectl apply -f web-deployment.yaml,web-service.yaml


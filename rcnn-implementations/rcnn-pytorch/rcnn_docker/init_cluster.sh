docker build -t us.icr.io/comvis/simplercnn:latest .
ibmcloud cr image-rm us.icr.io/comvis/simplercnn:latest
docker push us.icr.io/comvis/simplercnn:latest
kubectl apply -f simple-rcnn-deployment.yaml
kubectl apply -f simple-rcnn-service.yaml
# kubectl expose deployment/yolo-docker-deployment --type=NodePort --port=8080 --name=yolo-service --target-port=8080%  

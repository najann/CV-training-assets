kubectl delete service yolo-service
kubectl apply -f yolo-docker-deployment.yaml
kubectl apply -f yolo-service.yaml
# kubectl expose deployment/yolo-docker-deployment --type=NodePort --port=8080 --name=yolo-service --target-port=8080

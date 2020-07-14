kubectl delete service yolo-service
kubectl delete deployment yolo-docker-deployment
kubectl apply -f yolo-docker-deployment.yaml
kubectl apply -f yolo-service.yaml
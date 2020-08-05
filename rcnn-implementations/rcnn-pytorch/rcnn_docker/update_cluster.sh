
kubectl delete service simple-rcnn-service
kubectl delete deployment simple-rcnn-deployment
kubectl apply -f simple-rcnn-deployment.yaml
kubectl apply -f simple-rcnn-service.yaml
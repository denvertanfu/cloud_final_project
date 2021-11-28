# cloud_final_project

## Web GUI:
![image](https://user-images.githubusercontent.com/60454133/143777876-cc6f3dc6-913d-42e5-8eeb-4878bc18ae55.png)

Demo Video Link:

## Source Code for the main terminal application
### Containerize my microservice application
- the python script is as microservice.py, which provides the terminal application.
- microservice docker image on docker hub: https://hub.docker.com/r/ftan44/cloud_micro


## Source code for all Dockerfiles that were created and URLs for all docker images on Docker Hub
### Docker image used url (existing):
- Juypter notebook: https://hub.docker.com/r/jupyter/minimal-notebook
- Apache Hadoop:
  - namenode: https://hub.docker.com/r/bde2020/hadoop-namenode
  - datanode: https://hub.docker.com/r/bde2020/hadoop-datanode
- Apache Spark: https://hub.docker.com/r/bitnami/spark/
- Sonarqube: https://hub.docker.com/_/sonarqube

## Steps for running the microservices

## Create a Kubernetes Cluster on GCP
![image](https://user-images.githubusercontent.com/60454133/143778324-9d476870-f16d-42d0-8b9a-e92fed748cff.png)
you can also used the cluster created from before in the homework assignments

### Docker Image on GCP-Deployment and Service:
#### Download four_services folder from this repository
![image](https://user-images.githubusercontent.com/60454133/143781497-d870cb21-5cfb-412d-9f7f-88f6e83507bd.png)

#### Upload to GCP using GUI console, select the four_services from your local and upload all the yaml files
![image](https://user-images.githubusercontent.com/60454133/143781441-a75cd127-aa49-4692-8d19-c904350dc6e5.png)

#### cd to four_services file and type "kubectl apply -f .", this would deploy and expose all the images and services
![image](https://user-images.githubusercontent.com/60454133/143782069-64cfcdd8-a683-4fb0-8364-dc9f69bae885.png)

#### from the kubernetes engine service, we can see the Endpoints for each services
![image](https://user-images.githubusercontent.com/60454133/143782080-4c788ad7-a585-4e26-89ab-0a0a5e7c674a.png)


#### Save those endpoints and set in microservice.py


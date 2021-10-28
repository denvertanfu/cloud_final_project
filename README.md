# cloud_final_project

## Source Code for the main terminal application
### Containerize my microservice application
- the python script is as microservice.py, which provides the terminal application.
- docker built -t ftan44/microserver (without user input) and push to dockerhub (https://hub.docker.com/r/ftan44/microservice)
- docker built -t ftan44/my_microserver (with user input) and push to dockerhub (https://hub.docker.com/r/ftan44/my_microservice)


## Source code for all Dockerfiles that were created and URLs for all docker images on Docker Hub
### Docker image used url (existing):
- Juypter notebook: docker pull jupyter/datascience-notebook
- Apache Hadoop: docker pull sequenceiq/hadoop-docker
- Apache Spark: docker pull bitnami/spark
- Sonarqube: docker pull sonarqube

## deploy to kubernetes enginer on GCP
### Screenshot for the Kubernetes Engine with the containers running on it
<img width="1280" alt="Screen Shot 2021-10-28 at 2 27 06 PM" src="https://user-images.githubusercontent.com/60454133/139333340-bc9f59c6-5db7-456b-a4c8-0ff6165ad745.png">

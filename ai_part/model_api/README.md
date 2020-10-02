# Notes

## Run  

The API is wrapped up in a Dockerfile to make it easier to run.
Before running the Dockerfile which can be found in the `docker_files` folder.

Do the following inside the `docker_files` folder :  

1- Install [docker](https://docs.docker.com/get-docker/) if you don't have it
2- Create a [Docker Hub](https://hub.docker.com/) account
3- Type in your terminal:

```sh
# Command to build the Dockerfile
docker build --rm . -t your_dockerhub_id/detectron2:cleanout_v0
# Command to run the Dockerfile
docker run -p 8484:5000 -it your_dockerhub_id/detectron2:cleanout_v0 bin/bas
```

2- Use Postman and fill the `POST` with the following address: `http://127.0.0.1:8484/api/score-image`
![Postman Configuration](postman_config.png)

## Push and Deploy

### Push your docker

1- List all the docker images in your system
2- Get the tag of the docker you want to deploy
3- Log In to your Docker Hub account
4- Push the docker to Docker Hub

```sh
# Get the docker tag
docker images
# Tag your docker
docker tag your_docker_tag your_dockerhub_id/detectron2:cleanout_v0
# Log In to your Docker Hub account
docker login --username=your_dockerhub_id --password=your_dockerhub_password
# Push your docker
docker push your_dockerhub_id/detectron2:cleanout_v0
````

### Deploy your docker using Azure

1- Go to [Azure Shell](https://shell.azure.com/)
2- Log In to your account
3- Create a resource group, push your docker to it then get your deployed API address

```sh
az group create --name detectron2 --location eastus

az container create --resource-group detectron2 --name predictor --image your_dockerhub_id/detectron2:cleanout_v0 --cpu 2 --memory 4  --dns-name-label detectron2api --ports 5000

az container show --resource-group detectron2 --name predictor --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
```

## Client part

Run the following in your terminal:

```sh
npm install
npm install -g browserify
npm install -g watchify
npm i konva
npm i xhr-request
watchify index.js -o bundle.js
```

After this click on `index.html` to visualize the results.

**NB:**
I run the docker in parallel for now until I deploy the API.  
Remember to type `docker run -p 8484:5000 -it your_user_name/detectron2:cleanout_v0 bin/bas` to do so.  
Also, notice that some websites hosting images have a bit strict CORS policies so not all images will work fine. But you can check out the response using the inspectore `console` section.  

After you deploy in Azure, change the local address to your new API address.

## References

[Reference on which this work is based upon.](https://towardsdatascience.com/detectron2-the-basic-end-to-end-tutorial-5ac90e2f90e3)

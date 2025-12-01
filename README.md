### Welcome

This is the documentation for the project.

Compontents:
- python webapp
- docker
- github workflow


##### Build steps for app to container

In order to build the container please use the following commands from the project root!

``` bash
docker build -t <username>/gh-david-project:latest .
```

In order to take the freshly built container to a test drive use the following commnad. 

``` bash
 docker run -it -p 10080:8080 <username>/gd-david-project:latest
```

Then verify it via the appropriate url.

``` bash
administrator@debian:/tmp/demo $ curl http://localhost:10080
This is the demo app running on :8080
```

###### Dockerhub

The image is avaialable on [hub.docker.com](https://hub.docker.com) with the following image name: `<username>/gd-david-project`.

You can pull the image with the following command.

``` bash
docker pull <username>/gd-david-project:latest
```

Or just simply run the app the following way.

``` bash
docker run -d -p 8080:8080 <username>/gd-david-project:latest
```

> [!TIP]
> This workflow uses two github  action secrets to authenticate to docker hub, one is `DOCKERHUB_TOKEN` the other is `DOCKERHUB_USERNAME`. Change these to point the solution to another user or repository.

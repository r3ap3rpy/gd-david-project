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



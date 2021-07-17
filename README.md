# **Talking Containers**

Example of using two docker containers communicating through sockets.

In this example one container is reciting Shakespeare's Hamlet to another assuming an average reading speed of 150 words per minute.

## **How to run**

Use `docker-compose up` inside the `docker` folder to start the communication between the two containers.


## **How to run the code locally with *Bazel* already installed on host**

Optionally you can also run it locally (don't forget to change the `config/settings.ini` IP address to `localhost`):

Once you have successfully installed *Bazel* you can run the code in two separate terminals using:

```bash
docker run //:run_container -- -t "server"
docker run //:run_container -- -t "client"
```

### Bazel installation

[Install Bazel](https://docs.bazel.build/versions/master/install.html)


## **Dockerhub**

The container image is available at:

[hub.docker.com/repository/docker/framaxwlad/talking_container](https://hub.docker.com/repository/docker/framaxwlad/talking_container)

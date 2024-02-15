Linux
```shell
    sudo docker run -it --name tfx --rm -p 8888:8888 -p 6006:6006 -v $PWD:/tfx/src --entrypoint /run_jupyter.sh  tensorflow/tfx:1.12.0

Windows
```shell
    docker run -it --name tfx --rm -p 8888:8888 -p 6006:6006 -v .:/tfx/src --entrypoint /run_jupyter.sh  tensorflow/tfx:1.12.0

```shell
    docker-compose up
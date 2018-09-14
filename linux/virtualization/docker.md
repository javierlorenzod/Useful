You can change Docker’s storage base directory (where container and images go) using the -g option when starting the Docker daemon.

Ubuntu/Debian: edit your /etc/default/docker file with the -g option: DOCKER_OPTS="-dns 8.8.8.8 -dns 8.8.4.4 -g /mnt"

Fedora/Centos: edit /etc/sysconfig/docker, and add the -g option in the other_args variable: ex. other_args="-g /var/lib/testdir". If there’s more than one option, make sure you enclose them in " ". After a restart, (service docker restart) Docker should use the new directory.

Using a symlink is another method to change image storage.

Caution - These steps depend on your current /var/lib/docker being an actual directory (not a symlink to another location).

Stop docker: service docker stop. Verify no docker process is running ps faux
Double check docker really isn’t running. Take a look at the current docker directory: ls /var/lib/docker/
2b) Make a backup - tar -zcC /var/lib docker > /mnt/pd0/var_lib_docker-backup-$(date +%s).tar.gz
Move the /var/lib/docker directory to your new partition: mv /var/lib/docker /mnt/pd0/docker
Make a symlink: ln -s /mnt/pd0/docker /var/lib/docker
Take a peek at the directory structure to make sure it looks like it did before the mv: ls /var/lib/docker/ (note the trailing slash to resolve the symlink)
Start docker back up service docker start
restart your containers

## Detect and Track

1. Crear container con la siguiente instrucción (dentro de la carpeta *docker*):
```
docker build -t "detect_and_track:Dockerfile" .
```

1. Lanzar esta línea para ejecutar el docker de "detect and track"
```
docker run --runtime=nvidia -i -t detect_and_track:Dockerfile /bin/bash
```

1. Una vez dentro, se puede ejecutar lo siguiente para copiar archivos:
```
docker cp pretrained_models-selected a5a4fc6539b7:/detectandtrack/pretrained_models-selected
```

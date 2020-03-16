- How to uninstall docker completely, deleting also caches and storage usage (Copied from [this answer](https://askubuntu.com/questions/935569/how-to-completely-uninstall-docker)):

To completely uninstall Docker:

*Step 1*

<!-- language-all: lang-bash -->

    dpkg -l | grep -i docker

To identify what installed package you have:

*Step 2*

    sudo apt-get purge -y docker-engine docker docker.io docker-ce  
    sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce  

The above commands will not remove images, containers, volumes, or user created configuration files on your host. If you wish to delete all images, containers, and volumes run the following commands:

    sudo rm -rf /var/lib/docker /etc/docker
    sudo rm /etc/apparmor.d/docker
    sudo groupdel docker
    sudo rm -rf /var/run/docker.sock

You have removed Docker from the system completely.

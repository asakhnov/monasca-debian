# monasca-debian

This repository intends to provide control and supported files to build Monasca
related packages for Ubuntu Xenial.

Each directory contains **control**, **etc** directories and **helper.yml** file:
* **control** : contains DEBIAN control file and pre/post install/rm scripts.
* **etc** : contains related configuration files, e.g. logrotate, systemd.
* **helper.yml** : has a list of files from **etc** that needs to be added
                   to **pom.xml**


[pom.py](pom.py) provides ability to update **pom.xml** with extra files that needs
to be placed in a packages. Usage:
```code
./pom.py pom.xml helper.yaml
```

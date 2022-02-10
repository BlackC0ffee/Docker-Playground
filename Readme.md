# Docker Playground

## Install Docker on RPi

```
sudo apt update && sudo apt upgrade -f
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker Pi
dockerd-rootless-setuptool.sh install
```

## Build Web App

```
cd C0ffee
docker build -t c0ffee .
docker run -d -p 80:80 c0ffee
```

## Install composer

```
pip3 install docker-compose
```

## Compose POC

Source: https://docs.docker.com/compose/gettingstarted/

```
cd C0ffee
docker-compose up -d --build
```

## Docuwiki Container

Copy installation files of docker inside the folder DocuWiki/docuwiki
```
cd DocuWiki
docker build -t docuwiki .
docker run -d -p 80:80 docuwiki
```
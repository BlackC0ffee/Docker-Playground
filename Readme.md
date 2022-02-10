#Docker POC

## Install Docker on RPi

```
sudo apt update && sudo apt upgrade -f
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker Pi
`/usr/bin/dockerd-rootless-setuptool.sh uninstall -f ; /usr/bin/rootlesskit rm -rf /home/pi/.local/share/docker`
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

```
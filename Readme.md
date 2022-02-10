sudo apt update && sudo apt upgrade -f
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker Pi
`/usr/bin/dockerd-rootless-setuptool.sh uninstall -f ; /usr/bin/rootlesskit rm -rf /home/pi/.local/share/docker`
dockerd-rootless-setuptool.sh install
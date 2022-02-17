# Docker Playground

Warning: all content of  this repository was used as a Proof of Concept with no security in mind. DO NOT USE THIS IN PRODUCTION.

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
docker-compose up --build
```

## RPi Montior using Grafana and Influxdb

- Source (kind of): https://andreea-sonda31.medium.com/monitor-raspberry-pi-resources-and-parameters-with-grafana-board-part-1-ab0567303e8
- And also: https://www.jeffgeerling.com/blog/2021/monitor-your-internet-raspberry-pi
- Influx DB 1.8 stuff: https://blog.anoff.io/2020-12-run-influx-on-raspi-docker-compose/
- InfluxDB stuff (not supported under RPi 4 32-bit): https://www.influxdata.com/blog/running-influxdb-2-0-and-telegraf-using-docker/
- https://simonhearne.com/2020/pi-metrics-influx/

See: Media\Docker-Grafana+influxdb+pythonscript.png

```
cd Monitor
```
Generate the config file fore influxdb `docker run --rm influxdb:1.8 influxd config > influxdb.conf`

This has created a `influxdb.conf` file under the currend directory

```
pip3 install influxdb-client psutil
docker-compose up -d
```
1. Open the grafana dashboard (http://hostname:3000/) and log in with admin:admin.
1. Go to Data sources and create a new Influxdb Data source with following parameters:
    - URL: http://influxdb:8086
    - Database: pyexample
1. Save the data source. In the menu click on Import
1. Import the json-file Grafana/Dashboard.json
1. In the terminal, run the script:
```
python3 Monitor.py
```

## Grafana, Influxdb and Telegraf

source: https://nwmichl.net/2020/07/14/telegraf-influxdb-grafana-on-raspberrypi-from-scratch/

```
cd Monitor
docker-compose up -d
```

Attach a shell (using visual studio code) on the influxdb container

```
influx
create database telegraf
exit
```

Close the attached shell and install telegraf on the hosts

```
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt update
sudo apt install telegraf
```

Add the user to the correct groups, copy the config files and enable the service 

```
sudo usermod -a -G video telegraf
sudo cp Telegraf/telegraf.conf
sudo cp Telegraf/raspberrypi.conf /etc/telegraf/telegraf.d/
sudo systemctl enable telegraf
sudo systemctl start telegraf
```

1. Open the grafana dashboard (http://hostname:3000/) and log in with admin:admin.
1. Go to Data sources and create a new Influxdb Data source with following parameters:
    - Name: InfluxDB-Telegraf
    - URL: http://influxdb:8086
    - Database: telegraf
1. Click on Import
1. Enter the ID 10578 and click on Load
1. Select InfluxDB-Telegraf as data source
1. Click on Import
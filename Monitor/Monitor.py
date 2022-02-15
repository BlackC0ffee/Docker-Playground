import string
from influxdb import InfluxDBClient
import os
import datetime
import psutil

def InfluxDBExist(client:InfluxDBClient, databaseName) -> bool:
    db = client.get_list_database()
    for t in db:
        if databaseName in t.values():
            return True
    return False

def WriteCPU(client:InfluxDBClient):
    
    datapoints = [{
    "measurement": "RaspberryPi",
    "tags":
        {"Hostname": os.uname().nodename,},
    "time": datetime.datetime.utcnow(),
    "fields": {
        "cpu": psutil.cpu_percent(5),
        "memory": psutil.virtual_memory().percent
        }
    } 
    ]
    return client.write_points(datapoints)

if __name__ == "__main__":

    client = InfluxDBClient(host='localhost', port=8086)
    dbName = "pyexample"
    if not InfluxDBExist(client, dbName):
        client.create_database(dbName)

    client.switch_database(dbName)
    for x in range(500):
        WriteCPU(client)
    print("The End")
    #client.drop_database(dbName)
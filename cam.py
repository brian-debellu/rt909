# python 3.6

import random
import time
import json

from paho.mqtt import client as mqtt_client


broker = '172.17.0.2'
port = 1883
topic = "/CAM"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        data = {
            "stationId": random.choice(['1', '2', '3']),
            "stationType": random.choice(['5', '10', '15']),
            "vitesse":  random.randint(0, 130),
            "heading": random.randint(0, 180),
            "gps": '48.86,2.29',
            "accident": random.choice(['oui','non'])
        }
        msg=json.dumps(data)
        #msg = f"stationId: {msg_count}\n{data_out}"
        #msg = f"stationId: {msg_count}\nstationType: {stationType}\nvitesse: {vitesse}\nheading: {heading}\nGPS: {gps}"
        if data['vitesse'] <= 90:
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send\n`{msg}`\n to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1
        else:
            time.sleep(10)
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send\n`{msg}`\n to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

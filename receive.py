# python3.6

import random
import json

from paho.mqtt import client as mqtt_client


broker = '172.17.0.2'
port = 1883
topic = "/CAM"
topic2 = "/DENM"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):
    global slow
    slow = []
    global accident
    accident = 0

    def on_message(client, userdata, msg):
        if msg.topic == '/CAM':
            msg = msg.payload.decode()
            #print(f"data: {data}")
            data = json.loads(msg)
            if (data['vitesse']) < 90:
                global slow
                if (data['stationId']) in slow:
                    None
                else:
                    slow.append(data['stationId'])
            print (slow)

            print(f"message: {data}")

            if len(slow) >= 3:
                print(f"Attention embouteillage en cours !")
            else:
                None
            #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        elif msg.topic == '/DENM':
            msg = msg.payload.decode()
            #print(f"data: {data}")
            data = json.loads(msg)
            print(f"message: {data}")
            #print(data['causeCode'])
            if int(data['causeCode']) == 4:
                global accident
                accident += 1
                if accident >= 2:
                    print(f"Attention accident !")
            else:
                None


    client.subscribe(topic)
    client.subscribe(topic2)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()

#DOCKERFILE pour une voiture de test CAM

#Image serveur MQTT
FROM python:3.7-alpine

#Copie des scripts
COPY ./ /app

#Installation packages
RUN pip3 install --no-cache paho-mqtt

#Execution des scripts
CMD python3 /app/cam.py

# rt909
TP RT909

cam.py : script d'envoi de message CAM
denm.py : script d'envoi de message DENM
receive.py : script de récupération des messages MQTT
dockerfile : dockerfile pour la création du docker "car" contenant les scripts cam.py et denm.py, on le retrouve dans le docker hub suivant : briandebellu/car:latest
xmpp.py : script permettant la remonté d'information au serveur XMPP, appelé par receive.py

# rt909
TP RT909

cam.py : script d'envoi de message CAM
denm.py : script d'envoi de message DENM
receive.py : script de récupération des messages MQTT
dockerfile : dockerfile pour la création du docker "car" contenant le cam.py
xmpp.py : script permettant la remonté d'information au serveur XMPP, appelé par receive.py

docker hub :
briandebellu/xmpp
briandebellu/mqtt
briandebellu/car contient cam.py
briandebellu/car2 contient denm.py

# rt909

cam.py : script d'envoi de message CAM <br/>
denm.py : script d'envoi de message DENM <br/>
receive.py : script de récupération des messages MQTT <br/>
dockerfile : dockerfile pour la création du docker "car" contenant le cam.py <br/> 
dockerfile_denm : dockerfile pour la création du docker "car2" contenant le denm.py <br/> 
xmpp.py : script permettant la remonté d'information au serveur XMPP, appelé par receive.py <br/>

docker hub : <br/>
briandebellu/xmpp <br/> 
briandebellu/mqtt <br/>
briandebellu/car contient cam.py <br/> 
briandebellu/car2 contient denm.py <br/>

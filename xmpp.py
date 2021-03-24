# python 3

import sys,os,xmpp

id = "admin@example.com"
password = "admin"
receiver = "admin@example.com"
message = "test"

jid = xmpp.protocol.JID(id)
connection.connect(server=('172.17.0.3'))
connection.auth(user=jid.getNode(), password=password, resource=jid.getResource())
connection.send(xmpp.protocol.Message(to=receiver, body=message))

import paho.mqtt.client as mqtt



#----------------------------------------------------------------------
broker_address= "your server"
port = 187xx
user = "your username"
password = "your password"
topic = "your topic"
#----------------------------------------------------------------------





# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe(topic + "/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	cmd=str(msg.payload)
	if cmd == "b'left'":
		print("go left . . .")
	if cmd == "b'right'":
		print("go right . . .")
	if cmd == "b'front'":
		print("go front . . .")
	if cmd == "b'back'":
		print("go back . . .")
	if cmd == "b'up'":
		print("go up . . .")
	if cmd == "b'down'":
		print("go down . . .")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address,port, 60)
client.username_pw_set(user,password)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

from socket import *


def listen_rewrite(sockId):
	for payload in sockId.makefile():
		try:
			payload = payload.strip()

			if payload == "QUIT":
				raise error("Client requested shutdown")

			elif payload == "RESTART":
				sockId.shutdown(SHUT_RDWR)
				sockId.close()
				return "RESTART"
			
			print "<-"+payload
			payload = "SERVER * ACK " + "<" + payload + ">"
			print "--->"+payload[:20]
			sockId.send(payload+"\r\n")

		except Exception as e:
			print "exception raised",e
			sockId.shutdown(SHUT_RDWR)
			sockId.close()
			break

def spawn_worker(serverSocket):
	server.listen(1)
	client, address = server.accept()
	client.setblocking(True)
	print client.gettimeout()
	server.settimeout(100)
	return listen_rewrite(client)


server = socket()
server.bind(("127.0.0.1", 6465))
server.settimeout(10)
print server.gettimeout()

while(spawn_worker(server) is "RESTART"):
	print "restarting worker"
	

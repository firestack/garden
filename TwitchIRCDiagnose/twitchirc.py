#Twitch irc testing script
#For raw messages
import socket as s

NICK = "bomb_mask"
PASS = "oauth:z2feoa04bhpnxz6et565uhg6y4ckaq"

irc = s.socket()

irc.connect(("irc.twitch.tv",6667))

irc.send("PASS {}\r\n".format(PASS))
irc.send("NICK {}\r\n".format(NICK))
irc.send("JOIN #{}\r\n".format(NICK))

irc.send("CAP REQ:twitch.tv/commands")
while True:
	print irc.recv(4096)

irc.close()

k = input()

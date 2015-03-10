#Twitch irc testing script
#For raw messages
import socket as s

NICK = "bomb_mask"
PASS = "REDACTED"

irc = s.socket()

irc.connect(("irc.twitch.tv",6667))

irc.send("PASS {}\r\n".format(PASS))
irc.send("NICK {}\r\n".format(NICK))
irc.send("JOIN #{}\r\n".format(NICK))

irc.send("CAP REQ:twitch.tv/commands")
filedec = irc.makefile()
filedec.

print "exited file"


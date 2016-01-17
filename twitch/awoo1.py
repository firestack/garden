#!/usr/bin/env python
# coding: utf-8
# Import some necesary libraries.
import socket,time
import twitchtools.login


#for userName in raw_input("Users: ").split(" "):

User = twitchtools.login.Profile(raw_input("User? :"))
nick = User.name
auth = User.password

irc = socket.socket()



irc.connect(("irc.twitch.tv", 6667))
irc.sendall("pass {}\r\n".format(auth))
irc.sendall("nick {}\r\n".format(nick))

def printAt(message, line):
    print "\033[{}B".format(line),
    print message,
    print "\033[{}A".format(line),

def sendLogger(irc , message, channel, number):
    message = ("PRIVMSG #{} :{}\r\n".format(channel, message))

    irc.sendall(message)

    try:
        sendLogger.number += 1
        sendLogger.emotes += number

    except AttributeError:
        print "initializing..."
        print "Creating message counter....",
        sendLogger.number = 0
        print "done\nCreating emote counter....",
        sendLogger.emotes = number
        print "done"

    #print "\rNumber of messages sent: {}; Number of emotes sent: {} ".format(sendLogger.number, sendLogger.emotes),
    printAt("Nmb of msg: {}; Nmb of emote: {}".format(sendLogger.number, sendLogger.emotes), 5)

while True:
    for i in range(1,6):
        sendLogger(irc, "AWOO "*i, "codecan", i)
        time.sleep(1.6)


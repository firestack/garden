import os
import socket
from time import sleep
from garden.twitchtools import login

spam = input("Bool : ")
print type(spam)
amount = input("(int)amount : ")
size = input("(int)size : ")


data = raw_input("(str)String : ")
channel = raw_input("(str)channel : ")

user = login.Profile("bomb_mask")
t_nick = user.name
t_oauth = user.oauth

twitch_host = "irc.twitch.tv"
twitch_port = 6667

print "Joining {} as {}.\n".format(channel,t_nick)

irc = socket.socket()
irc.connect((twitch_host,twitch_port))

irc.sendall('PASS {}\r\n'.format(t_oauth))
irc.sendall('NICK {}\r\n'.format(t_nick))
irc.sendall('JOIN #{}\r\n'.format(channel))

print irc.recv(8192)

go = raw_input("ready?...")
irc.sendall('JOIN #{}\r\n'.format(channel))
print irc.recv(4092)

if spam:
        for amountSize in range(amount):
                for i in range(1,size+size):
                        total_i = (i if i < size else size - (i % size))

                        print total_i
                        toSend = 'PRIVMSG #{} :{}\r\n'.format(channel, (data+' ')*total_i*spam)
                        print "message",i
                        print toSend
                        #sleep(1.21)
                        #if mod
                        sleep(0.01)
                        irc.sendall(toSend)
else:
        for amountSize in range(amount):
                tosend = 'PRIVMSG #{} :{}\r\n'.format(channel, data)
                print amountSize, tosend
                irc.sendall(tosend)
                #sleep(1.21)
                
print irc.recv(4096)

irc.close()

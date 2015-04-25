#! /usr/bin/env python2.7

# import socket
# import thread
from sys import path 
import os
path.append(os.path.abspath(r"C:\Users\bombmask\Source"))

import twitchtools.login



# class IRC:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port

#     def sock_init(self):
#         try:
#             self.irc = socket.socket()
#             self.irc.settimeout(600)
#         except Exception as e:
#             print("Failed to create socket.")
#             raise

#     def sock_connect(self):
#         try:
#             self.irc.connect((self.host, self.port))
#         except Exception as e:
#             print("Failed to connect to the host.")
#             raise

#     def send_raw(self, msg):
#         self.irc.sendall("{}\r\n".format(msg).encode("utf-8"))

#     def send_pass(self, password):
#         self.send_raw("PASS {}".format(password))

#     def send_nick(self, nick):
#         self.send_raw("NICK {}".format(nick))

#     def send_join(self, channel):
#         self.send_raw("JOIN #{}".format(channel))

#     def send_pm(self, channel, msg):
#         self.send_raw("PRIVMSG #{} :{}".format(channel, msg))

#     def sock_raw_recv(self, amount):
#         msg = self.irc.recv(amount)
#         if msg:
#             return msg
#         elif msg == "":
#             raise ValueError
#         else:
#             return None

#     def sock_recv(self, amount):
#         msg = self.sock_raw_recv(amount)
#         try:
#             msg = msg.decode("utf-8")
#         except AttributeError as e:
#             return None

#         if msg.startswith("PING"):
#             self.send_raw(msg.replace("PING", "PONG"))
#         return msg

#     def sock_disconnect(self):
#         try:
#             self.send_raw("QUIT")
#         except Exception as e:
#             pass
#         finally:
#             self.irc.close()

#     def destroy_socket(self):
#         del self.irc



class IRC(object):
    """
    IRC((Address, port), [(user, pass), (Profile object)])
    """
    user = None

    channels = {}
    def __init__(self, IRC, USER):
        self.link = None

        if isinstance(USER, (tuple, list)):
            #bla bla bla
            self.user = twitchtools.login.Profile(USER[0], username=USER[0], oauth=USER[1])

        elif isinstance(USER, twitchtools.login.Profile):
            self.user = USER

        else:
            raise TypeError("User is not of correct type")


    def connect(self):
        pass

    def disconnect(self):
        pass

    def raw(self, message):
        pass

    def nick(self):
        pass
        
    def password(self):
        pass

    def join(self, channel):
        pass

    def part(self, channel):
        pass

    def pm(self, CHANNELOBJ, message):
        pass

    def read(self, amount = 512, timeout = -1):
        pass

class Channel(object):
    """
    Channel(IRCobject, name)
    """

    users = {}

    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name
        
        
class User(object):
    """
    """
    messages = []
    def __init__(self, ):
        pass

if __name__ == '__main__':
    m = IRC(("irc.twitch.tv", 6667), twitchtools.login.Profile("bomb_mask"))
    k = raw_input("press enter to exit...")
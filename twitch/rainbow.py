# -*- coding: utf-8 -*-
import socket
from time import sleep
import colorsys
import threading
from sys import argv, path 
import os

#path.append(os.path.abspath("C:/Users/levi/Source/"))

from twitchtools.color import colors as color
from twitchtools import login

channel_macros = {
    "dive":{
        "message":u".me ก็็็็็็็็็็็็็ʕ•͡ᴥ•ʔ ก้ DIVE ก็็็็็็็็็็็็็ʕ•͡ᴥ•ʔ ก้"
    },
    "snarfresub":{
        "channel":"snarfybobo", 
        "message":".me snarfHype THANK YOU FOR YOUR CONTINUED BOBO PATRONAGE!! snarfHype",
        "amount":7
        },  
    "snarfsub":{
        "channel":"snarfybobo",
        "amount":7,
        "message":".me snarfHype snarfCat WELCOME TO THE BOBOBROS snarfBear snarfHype"
    },
    "daisyhi":{
        "channel":"daisy8789",
        "message":".me HI DAISY, HAVE A RAINBOW!!"
    },
    "ratshi":{
        "channel":"rats7eli",
        "message":".me SMASH THE SIXTY FOUR?! tloFace"
    },
    "snarfhype":{
        "channel":"bomb_mask",
        "message":u"snarfHype\u200bsnarfHype\u200bsnarfHype"
    }
}

for k,v in channel_macros.items():
    channel_macros[k]["message"] = unicode(v["message"])

def ping_return(socket_obj,print_all=False):
    print("Print all: ", print_all)
    print(socket_obj)
    while True:
        
        data = socket_obj.recv(512)
        if not data: break
        if print_all:
            print data
        if data.startswith("PING"):
            socket_obj.sendall("PONG tmi.twitch.tv\r\n")
    
    print ("Socket read thread has quit...")



def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in xrange(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)


def setup_rainbow_words():
    # Rainbow words
    command = raw_input("Command: ")
    if command in channel_macros:
        return (channel_macros[command]["channel"], [channel_macros[command]["message"]+ ("." if number % 2 == 0 else "") for number in range(len(color.colors))])
    else:
        channel = command

    words = raw_input("Please input {} words: ".format(len(color.colors))).strip()

    #rainbow word
    if ((len(words.split(' ')) == 1 and words is not '') or (words[0] == "$")):
        if words[1] == '$' and words[2:] in channel_macros:
            return (channel, [channel_macros[words[2:]]["message"] + ("." if number % 2 == 0 else "") for number in range(len(color.colors))])
            

        words = [ ".me "+ words[1:] + ("." if number % 2 == 0 else "") for number in range(len(color.colors))]
    #rainbow words<
    else:
        words = [".me "+i for i in words.split(' ')]

    return (channel, words)

def rainbow_loop(length_mod = 1, cwPair = (None, None), wait_amount = 0.18, offset = 0, irc = None):
    colors = color.color_hex
    colors.sort(key=lambda x: get_hsv(x[1]))
    length_mod = len(color.colors) / length_mod 
    wait_time = wait_amount
    channel, words = setup_rainbow_words() if cwPair[0] is None else cwPair
    multiplier = lambda x: (x*length_mod if x*length_mod < len(color.colors) else x*length_mod % len(color.colors))


    print "multiplier: ", multiplier, "Length: ", len(words)
    print words

    print "Channel : \'{}\'' is okay?".format(channel)
    if(raw_input(' > ') != ''):raise ValueError("Wrong channel")

    for i in (range((len(words) if length_mod == 1 else len(color.colors) / length_mod))):

        print "i value: ",i,"i x multiplier : ", multiplier(i)

        curColor, curWord = (colors[multiplier(i+offset)], words[i])
        channelMessage = u"PRIVMSG #{} :{}\r\n"
        colorChange = channelMessage.format(channel, ".color "+curColor[0])
        wordInsert = channelMessage.format(channel, curWord)
        irc.sendall(colorChange)
                                
        #sleep(wait_time)

        irc.sendall(wordInsert.encode('utf-8'))
        
        #sleep(wait_time)
        print colorChange,'\n',wordInsert.encode('utf-8')

def rainbow_change_color(irc, time):
    channel_target = raw_input("CHANNEL TARGET : ")
    irc.sendall("JOIN #{}\r\n".format(channel_target))
    i = 0
    MAX_ITER = len(colors)

    while True:
        sleep(time)
        print ("PRIVMSG #{base} :.color {color}\r\n".format(base=channel_target, color=colors[i][0]))
        irc.sendall("PRIVMSG #{base} :.color {color}\r\n".format(base=channel_target, color=colors[i][0]))
        i = i+1 if i < MAX_ITER-1 else 0
        
def quoter(irc, time, channel, command = "!quote"):
    irc.sendall("JOIN #{}\r\n".format(channel))

    while True:
        irc.sendall("PRIVMSG #{} :{}\r\n".format(channel, command))
        sleep(time)

def talk_loop(irc):
    while True:
        msg = raw_input(">>")
        irc.sendall("PRIVMSG #{} :{}\r\n".format(channel, msg))


def normal_operation(): 
    #Sort
    #channel, words = setup_rainbow_words(  )
    colors = color.color_hex
    colors.sort(key=lambda x: get_hsv(x[1]))
    #colors = color.color_hex
    bomb_mask = login.Profile("bomb_mask")
    NICKNAME = bomb_mask.name #"bomb_mask"#put your nickname here please
    OAUTH_KEY = bomb_mask.password #"oauth:i9ujz4x4abcxg913m7kh36v571ak4u"#put your oauth key here please

    twitch_host = "irc.twitch.tv"
    twitch_port = 6667

    #Join IRC
    irc = socket.socket()
    #print "Joining {} as {}.\n".format(channel,NICKNAME)
    irc.connect((twitch_host,twitch_port))

    printer = threading.Thread(target=ping_return, args=(irc,True))
    printer.daemon = True
    printer.start()

    irc.sendall('PASS {}\r\n'.format(OAUTH_KEY))
    irc.sendall('NICK {}\r\n'.format(NICKNAME))
    #irc.sendall('JOIN #{}\r\n'.format(channel))

    rainbow_loop(7,wait_amount=0.026, irc = irc)
    #rainbow_loop(25, wait_amount=0.015, irc = irc)
    #rainbow_change_color(irc, 2 )
    #quoter(irc, 65, "snarfybobo")

    sleep(2)
    irc.close()

if __name__ == '__main__':
    #try:
    normal_operation()

    #finally:
    print "Program exit."
    raw_input("Press enter to exit...")

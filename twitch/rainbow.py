# -*- coding: utf-8 -*-
<<<<<<< HEAD
import socket
from time import sleep
=======
import twitchtools.utils
import twitchtools.chat
import twitchtools.color 
import twitchtools.login
import time
>>>>>>> origin/master
import colorsys

##
twitchtools.utils.Printer.ON = True
twitchtools.utils.Printer.level = "DEBUG"
p = twitchtools.utils.Printer("MAINLOOP")
##Global settings variables
TOTAL_MESSAGES = len(twitchtools.color.colors)
MULTIPLIER = 1
IS_MOD = True
SORTED = True
DEBUG_DO_TWITCH_SEND = True
#Turbo dependent
USER_HAS_TURBO = True
ENSURE_WEB_SAFE = False

##END
##Macro Lookup table
macros = {
    "dive":{
        "message":u"ก็็็็็็็็็็็็็ʕ•͡ᴥ•ʔ ก้ DIVE ก็็็็็็็็็็็็็ʕ•͡ᴥ•ʔ ก้",
        "amount":12
    },
    "rainbow":{
        "message":u"LOOK AT ALL THE RAINBOW",
        "amount":30,

<<<<<<< HEAD
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
=======
    },
    "TURBO":{
        "message":u"snarfBoo Hi snarfHype\u200bsnarfHype\u200bsnarfHype snarfBoo",
        "amount":20,
        "channel":"bomb_mask"

    },
    "turbotest":{
        "message":"Glcls HI",
        "amount":255
    },
    "snarfresub":{
        "channel":"snarfybobo", 
        "message":"snarfHype THANK YOU FOR YOUR CONTINUED BOBO PATRONAGE!! snarfHype",
        "amount":4
        },  
    "snarfsub":{
        "channel":"snarfybobo",
        "amount":4,
        "message":"snarfHype snarfCat WELCOME TO THE BOBOBROS snarfBear snarfHype"
>>>>>>> origin/master
    },
    "daisyhi":{
        "channel":"daisy8789",
        "message":"HI DAISY, HAVE A RAINBOW!!"
    },
    "ratshi":{
        "channel":"rats7eli",
<<<<<<< HEAD
        "message":".me SMASH THE SIXTY FOUR?! tloFace"
=======
        "message":"SMASH THE SIXTY FOUR?! tloFace"
>>>>>>> origin/master
    },
    "snarfhype":{
        "channel":"bomb_mask",
        "message":u"snarfHype\u200bsnarfHype\u200bsnarfHype"
    }
}
<<<<<<< HEAD

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


=======
##END
>>>>>>> origin/master

def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in xrange(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)




if __name__ == '__main__':
    command = raw_input("[Enter a channel]> ")
    #Split command list

    #set up temp vars
    strings = []
    string_channel = ''

    #Create words list
    if command in macros:
        #If macros specify a value for amount or multiplier
        TOTAL_MESSAGES = macros[command].get("amount", TOTAL_MESSAGES)
        p(TOTAL_MESSAGES)
        MULTIPLIER = macros[command].get("multiplier", MULTIPLIER)
        string_channel = macros[command].get("channel", '')

        if "split" in macros[command]:
            strings = [string for string in macros[command]["message"].split(' ')]
        else:
            strings = [macros[command]["message"] for i in range(TOTAL_MESSAGES)]

        
    else:
        string_channel = command.strip().strip('!')
        strings = raw_input("[Enter a message]> ")

        #If override channel in macros
        if strings[2:].strip() in macros and strings[:2] == "$$":
            genString = strings[2:].strip()
            TOTAL_MESSAGES = macros[genString].get("amount", TOTAL_MESSAGES)



            if "split" in macros[genString]:
                strings = [string for string in macros[genString]["message"].split(' ')]

            else:
                strings = [macros[genString]["message"] for i in range(TOTAL_MESSAGES)]

        #if send whole line
        elif strings[0] == "$":
            strings = [strings[1:] for i in range(TOTAL_MESSAGES)]

        #else split and send
        else:
            strings = [string for string in strings.strip().split(' ')]
            TOTAL_MESSAGES = len(strings)

<<<<<<< HEAD
        curColor, curWord = (colors[multiplier(i+offset)], words[i])
        channelMessage = u"PRIVMSG #{} :{}\r\n"
        colorChange = channelMessage.format(channel, ".color "+curColor[0])
        wordInsert = channelMessage.format(channel, curWord)
        irc.sendall(colorChange)
                                
        #sleep(wait_time)

        irc.sendall(wordInsert.encode('utf-8'))
        
        #sleep(wait_time)
        print colorChange,'\n',wordInsert.encode('utf-8')
=======

    if string_channel == "":
        string_channel = raw_input("Channel? : ")
>>>>>>> origin/master


    #Gen Colorspace
    if not USER_HAS_TURBO:
        if SORTED:colors = sorted(twitchtools.color.color_hex, key = lambda x: get_hsv(x[1]))
        else: colors = twitchtools.color.color_hex 

        if TOTAL_MESSAGES < len(colors):
            MULTIPLIER = len(colors) / float(TOTAL_MESSAGES)
            p(TOTAL_MESSAGES, len(colors), MULTIPLIER)

    elif USER_HAS_TURBO:
        colors = ['#'+''.join(['{:02X}'.format(int(n * 255)) for n in colorsys.hsv_to_rgb(float(i) / TOTAL_MESSAGES, 1, 1)]) for i in range(TOTAL_MESSAGES)]
        #colors = #["#"+''.join(['{:02X}'.format(int(n*255)) for n in colorsys.hsv_to_rgb(i/TOTAL_MESSAGES ,.5,1)]) for i in range(TOTAL_MESSAGES)]

    #Gen interleaved message array
    messages = []

    i = 0
    for string in strings:
        if not USER_HAS_TURBO:
            messages.append('.color {}'.format(colors[int(round(i*MULTIPLIER)) % len(colors)][1]))
        elif USER_HAS_TURBO:
            messages.append('.color {}'.format(colors[i]))
        
        messages.append(".me " + string)
        i += 1

    for message in range(len(messages)):
        messages[message] = messages[message].encode('utf-8')
        #p( messages[message] )

    #write to twitch socket/IRC
    if DEBUG_DO_TWITCH_SEND:
        with twitchtools.chat.IRC(("irc.twitch.tv", 6667), twitchtools.login.Profile("bomb_mask")) as twitch:
            twitch.capibilities("tags")
            twitch.capibilities("commands")
            channel = twitch.join(string_channel)
            twitch.read()

            for message in messages:
                channel.pm(message)
                if not IS_MOD:
                    time.sleep(1.6 / 2.0)
                else:
                    #time.sleep(0.01)
                    pass

            twitch.read()
    else:
        p(colors)
        from Tkinter import *

        MAX_ROWS = 18
        FONT_SIZE = 10 # (pixels)

        root = Tk()
        root.title("Named colour chart")
        row = 0
        col = 0

        if not USER_HAS_TURBO:
            colors = [c[1] for c in colors]

<<<<<<< HEAD
def normal_operation(): 
    #Sort
    #channel, words = setup_rainbow_words(  )
    colors = color.color_hex
    colors.sort(key=lambda x: get_hsv(x[1]))
    #colors = color.color_hex
    bomb_mask = login.Profile("bomb_mask")
    NICKNAME = bomb_mask.name #"bomb_mask"#put your nickname here please
    OAUTH_KEY = bomb_mask.password #"oauth:i9ujz4x4abcxg913m7kh36v571ak4u"#put your oauth key here please
=======
        for color in colors:
          e = Label(root, text=' ', background=color, 
                font=(None, -FONT_SIZE))
          e.grid(row=row, column=col, sticky=E+W)
          row += 1
          if (row > MAX_ROWS):
            row = 0
            col += 1
>>>>>>> origin/master

        root.mainloop()




<<<<<<< HEAD
    rainbow_loop(7,wait_amount=0.026, irc = irc)
    #rainbow_loop(25, wait_amount=0.015, irc = irc)
    #rainbow_change_color(irc, 2 )
    #quoter(irc, 65, "snarfybobo")
=======
# 
# import socket
# from time import sleep
# import colorsys
# import threading
# from sys import argv, path 
# import os
>>>>>>> origin/master


# from twitchtools.color import colors as color
# from twitchtools import login



# for k,v in channel_macros.items():
#     channel_macros[k]["message"] = unicode(v["message"])




# def get_hsv(hexrgb):
#     hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
#     r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in xrange(0,5,2))
#     return colorsys.rgb_to_hsv(r, g, b)


# def setup_rainbow_words():
#     # Rainbow words
#     command = raw_input("Command: ")
#     if command in channel_macros:
#         return (channel_macros[command]["channel"], [channel_macros[command]["message"]+ ("." if number % 2 == 0 else "") for number in range(len(color.colors))])
#     else:
#         channel = command

#     words = raw_input("Please input {} words: ".format(len(color.colors))).strip()

#     #rainbow word
#     if ((len(words.split(' ')) == 1 and words is not '') or (words[0] == "$")):
#         if words[1] == '$' and words[2:] in channel_macros:
#             return (channel, [channel_macros[words[2:]]["message"] + ("." if number % 2 == 0 else "") for number in range(len(color.colors))])
            

#         words = [ ".me "+ words[1:] + ("." if number % 2 == 0 else "") for number in range(len(color.colors))]
#     #rainbow words<
#     else:
#         words = [".me "+i for i in words.split(' ')]

#     return (channel, words)

# def rainbow_loop(length_mod = 1, cwPair = (None, None), wait_amount = 0.18, offset = 0, irc = None):
#     colors = color.color_hex
#     colors.sort(key=lambda x: get_hsv(x[1]))
#     length_mod = len(color.colors) / length_mod 
#     wait_time = wait_amount
#     channel, words = setup_rainbow_words() if cwPair[0] is None else cwPair
#     multiplier = lambda x: (x*length_mod if x*length_mod < len(color.colors) else x*length_mod % len(color.colors))


#     print "multiplier: ", multiplier, "Length: ", len(words)
#     print words

#     print "Channel : \'{}\'' is okay?".format(channel)
#     if(raw_input(' > ') != ''):raise ValueError("Wrong channel")

#     for i in (range((len(words) if length_mod == 1 else len(color.colors) / length_mod))):

#         print "i value: ",i,"i x multiplier : ", multiplier(i)

#         curColor, curWord = (colors[multiplier(i+offset)], words[i])
#         channelMessage = u"PRIVMSG #{} :{}\r\n"
#         colorChange = channelMessage.format(channel, ".color "+curColor[0])
#         wordInsert = channelMessage.format(channel, curWord)
#         irc.sendall(colorChange)
                                
#         sleep(wait_time)

#         irc.sendall(wordInsert.encode('utf-8'))
        
#         sleep(wait_time)
#         print colorChange,'\n',wordInsert.encode('utf-8')

# def rainbow_change_color(irc, time):
#     channel_target = raw_input("CHANNEL TARGET : ")
#     irc.sendall("JOIN #{}\r\n".format(channel_target))
#     i = 0
#     MAX_ITER = len(colors)

#     while True:
#         sleep(time)
#         print ("PRIVMSG #{base} :.color {color}\r\n".format(base=channel_target, color=colors[i][0]))
#         irc.sendall("PRIVMSG #{base} :.color {color}\r\n".format(base=channel_target, color=colors[i][0]))
#         i = i+1 if i < MAX_ITER-1 else 0
        
# def quoter(irc, time, channel, command = "!quote"):
#     irc.sendall("JOIN #{}\r\n".format(channel))

#     while True:
#         irc.sendall("PRIVMSG #{} :{}\r\n".format(channel, command))
#         sleep(time)

# def talk_loop(irc):
#     while True:
#         msg = raw_input(">>")
#         irc.sendall("PRIVMSG #{} :{}\r\n".format(channel, msg))


# def normal_operation(): 
#     #Sort
#     #channel, words = setup_rainbow_words(  )
#     colors = color.color_hex
#     colors.sort(key=lambda x: get_hsv(x[1]))
#     #colors = color.color_hex
#     bomb_mask = login.Profile("bomb_mask")
#     NICKNAME = bomb_mask.name #"bomb_mask"#put your nickname here please
#     OAUTH_KEY = bomb_mask.password #"oauth:i9ujz4x4abcxg913m7kh36v571ak4u"#put your oauth key here please

#     twitch_host = "irc.twitch.tv"
#     twitch_port = 6667

#     #Join IRC
#     irc = socket.socket()
#     #print "Joining {} as {}.\n".format(channel,NICKNAME)
#     irc.connect((twitch_host,twitch_port))

#     printer = threading.Thread(target=ping_return, args=(irc,True))
#     printer.daemon = True
#     printer.start()

#     irc.sendall('PASS {}\r\n'.format(OAUTH_KEY))
#     irc.sendall('NICK {}\r\n'.format(NICKNAME))
#     #irc.sendall('JOIN #{}\r\n'.format(channel))

#     rainbow_loop(2,wait_amount=0.026, irc = irc)
#     #rainbow_loop(25, wait_amount=0.015, irc = irc)
#     #rainbow_change_color(irc, 2 )
#     #quoter(irc, 65, "snarfybobo")

#     sleep(2)
#     irc.close()

# if __name__ == '__main__':
#     #try:
#     normal_operation()

#     #finally:
#     print "Program exit."
#     raw_input("Press enter to exit...")

# -*- coding: utf-8 -*-
import twitchtools.utils
import twitchtools.chat
import twitchtools.color
import twitchtools.login
import time
import colorsys
import json
import codecs
##
twitchtools.utils.Printer.ON = True
twitchtools.utils.Printer.level = "DEBUG"
p = twitchtools.utils.Printer("MAINLOOP")
##Global settings variables
TOTAL_MESSAGES = len(twitchtools.color.colors)
MULTIPLIER = 1
## JSON SETTABLE SETTINGS
with open("config.json",'r') as fin:
    data = json.load(fin)
    USER = data["user"]
    IS_MOD = bool(data["is_mod"])
    SORTED = bool(data["sorted"])
    DEBUG_DO_TWITCH_SEND = not bool(data["debug"])
    USER_HAS_TURBO = bool(data["is_turbo"])

#Turbo dependent
ENSURE_WEB_SAFE = False

##END
##Macro Lookup table
macros = {
    "dive":{
        "message":u"ก็็็็็็็็็็็็็ʕ•͡ᴥ•ʔ ก้ DIVE ก็็็็็็็็็็็็็ʕ•͡ᴥ•ʔ ก้",
        "amount":10
    },
    "rainbow":{
        "message":u"LOOK AT ALL THE RAINBOW",
        "amount":30,

    },
    "max":{
        "message":"spam",
        "amount":255
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
    },
    "daisyhi":{
        "channel":"daisy8789",
        "message":"HI DAISY, HAVE A RAINBOW!!"
    },
    "ratshi":{
        "channel":"rats7eli",
        "message":"SMASH THE SIXTY FOUR?! tloFace"
    },
    "nohype":{
        "channel":"theno1alex",
        "message":u"no1HYPE\u200bno1HYPE\u200bno1HYPE"
    },
    "pb":{
        "message":"snarfHype PB HYPE snarfHype",
        "amount":15
    }
}
##END

def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

if __name__ == '__main__':
    print("Avalible commands:")
    for i in macros.items():
        print(i[0])
    command = input("[Enter a channel]> ")
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
        strings = input("[Enter a message]> ")

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


    if string_channel == "":
        string_channel = input("Channel? : ")


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
        with twitchtools.chat.IRC(("irc.twitch.tv", 6667), twitchtools.login.Profile(USER)) as twitch:
            twitch.capibilities("tags")
            twitch.capibilities("commands")
            channel = twitch.join(string_channel)
            twitch.read()

            for message in messages:
                print(type(message))
                channel.pm(message)
                if not IS_MOD:
                    time.sleep(1.6 / 2.0)
                else:
                    time.sleep(0.08)
                    pass

            twitch.read()
    else:
        p(colors)
        from tkinter import *

        MAX_ROWS = 18
        FONT_SIZE = 10 # (pixels)

        root = Tk()
        root.title("Named colour chart")
        row = 0
        col = 0

        if not USER_HAS_TURBO:
            colors = [c[1] for c in colors]

        for color in colors:
          e = Label(root, text=' ', background=color,
                font=(None, -FONT_SIZE))
          e.grid(row=row, column=col, sticky=E+W)
          row += 1
          if (row > MAX_ROWS):
            row = 0
            col += 1

        root.mainloop()

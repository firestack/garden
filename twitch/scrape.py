import twitchtools.login as login
import twitchtools.chat as chat

print dir(chat)

twitchlink = ("irc.twitch.tv",6667)

annon = login.Profile("justinfan0007", oauth="blaw")
bomb = login.Profile("bomb_mask")
channel = "snarfybobo"
scrapeTime = 20
scrapeMessages = 400




with chat.IRC.IRC(twitchlink, bomb) as twitch:
    twitch.join(channel)
    twitch.capibilities("tags")
    twitch.capibilities("commands")
    twitch.join("bomb_mask")
    

    for i in twitch.readfile():
        print i
        with open(__file__[:-3]+'.log', 'a') as fout: 
            fout.write(repr(i)+"\n")


flink = twitch.link.makefile()


raw_input('Press enter to exit...')
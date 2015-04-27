import twitchtools.login as login
import twitchtools.chat as chat

print dir(chat)
# twitchlink = ("irc.twitch.tv",6667)
twitchlink = ("127.0.0.1", 6465)
annon = login.Profile("justinfan0007", oauth="blaw")
bomb = login.Profile("bomb_mask")
channel = "snarfybobo"
scrapeTime = 20
scrapeMessages = 400


# with chat.IRC.IRC(twitchlink, bomb) as twitch:
#     twitch.join(channel)
#     twitch.capibilities("tags")
#     twitch.capibilities("commands")
#     twitch.join("bomb_mask")
    

#     for i in twitch.readfile():
#         print i
#         with open(__file__[:-3]+'.log', 'a') as fout: 
#             fout.write(repr(i)+"\n")
#         # with open(__file__[:-3]+".raw.log", 'a') as fout:
#         #     fout.write(repr(i)+'\n')

twitch = chat.IRC.IRC(twitchlink, bomb)
twitch.join(channel)
twitch.capibilities("tags")
twitch.capibilities("commands")
twitch.link.settimeout(5)

flink = twitch.link.makefile()


raw_input('Press enter to exit...')
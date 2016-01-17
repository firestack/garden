from twitchtools import login, chat
import time

twitchlink = ("irc.twitch.tv",6667)

def BanBotRuntime(channel, message):

    if message.serverCOM == "CLEARCHAT":
        for oldMessage in channel.users[message.sender].messages[-5:]:
            channel.sendMessage(oldMessage)
            time.sleep(0.1)
            #channel.sendMessage(channel.users[message.sender].messages[-1])

with chat.IRC.IRC(twitchlink, login.Profile("TheMaskOfTruth")) as twitch:
    twitch.capibilities("tags")
    twitch.capibilities("commands")
    twitch.join("bomb_mask").MessageCallback(BanBotRuntime)
    

    for i in twitch.readfile():
        print i
        if i.message == "QUIT":
            break

    #     if hasattr(i, 'serverCHAN'):
    #         try:
    #             if i.serverCOM == "PRIVMSG":
    #                 if i.message.startswith(":"):twitch.channels[i.serverCHAN].sendMessage(i.message)
    #         except KeyError:
    #             pass
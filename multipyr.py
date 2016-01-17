from twitchtools import login, chat, utils
import time

if __name__ == '__main__':
    utils.Printer.level = "DEBUG"

    # with chat.IRC(("irc.twitch.tv", 6667), login.Profile("bomb_mask")) as twitch:
    #     twitch.capibilities("tags")
    #     twitch.capibilities("commands")
    #
    #     user = input("User>")
    #     message = input("Message>")
    #     length = int(input("Length/2>"))
    #
    #     USER = chat.User(chat.Channel("","testing"), user)
    #
    #     if not message[-1] == ' ':
    #         message += ' '
    #
    #     for i in range(1,length*2):
    #         if i < length:
    #             math = i
    #         else:
    #             math = length - (i%length)
    #
    #         time.sleep(.4)
    #
    #
    #         twitch.whisper(USER, message*math)


    user = input("Channel>")
    message = input("Message>")
    length = int(input("Length/2>"))

    if not message[-1] == ' ':
        message += ' '

    twitch_link=("irc.twitch.tv",6667)
    accounts = ["bomb_mask","themaskoftruth","whitetail_atom","bombmask"]
    twitchs = [chat.IRC(twitch_link, login.Profile(account), True) for account in accounts]
    USER = chat.User(chat.Channel("","testing"), user)

    time.sleep(.2)

    for twitch in twitchs:
        twitch.join(user)

    time.sleep(.2)

    print()

    for i in range(1,length*2):
        if i < length:
            math = i
        else:
            math = length - (i%length)

        twitchs[(i-1)%len(twitchs)].channels[user].pm(message*math)
        #twitchs[(i-1)%len(twitchs)].whisper(USER, message*math)
        
        time.sleep(.2)

        # if (i-1)/len(twitchs) < 1:
        #     print(i, i/len(twitchs), i%len(twitchs))
        # else:
        #     print(i, i/len(twitchs), i%len(twitchs),'a')

    print()
    for i in twitchs:
        i.disconnect()

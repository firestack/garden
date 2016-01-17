from twitchtools import login, chat, utils
import time

if __name__ == '__main__':
    utils.Printer.level = "DEBUG"

    with chat.IRC(("irc.twitch.tv", 6667), login.Profile("bomb_mask")) as twitch:
        twitch.capibilities("tags")
        twitch.capibilities("commands")

        user = input("User>")
        message = input("Message>")
        length = int(input("Length/2>"))
        USER = chat.User(chat.Channel("","testing"), user)

        if not message[-1] == ' ':
            message += ' '

        for i in range(1,length*2):
            if i < length:
                math = i
            else:
                math = length - (i%length)

            time.sleep(.4)


            twitch.whisper(USER, message*math)

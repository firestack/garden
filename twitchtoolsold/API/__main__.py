import requests

class API:

    chat_url = "http://tmi.twitch.tv/group/user/{nickname}/chatters"
    stream_url = "https://api.twitch.tv/kraken/streams?channel="

    def __init__(self, channels):
        self.channels = channels

    def get_viewers(self, channel):
        try:
            chat_response = requests.get(self.chat_url.format(nickname=channel))
            chat_response.raise_for_status()
            chat_decode = chat_response.json()
            viewers = list(chat_decode["chatters"]["moderators"] + chat_decode["chatters"]["staff"] + chat_decode["chatters"]["admins"] + chat_decode["chatters"]["global_mods"] + chat_decode["chatters"]["viewers"])
            return viewers
        except Exception as e:
            raise

    def get_live_status(self):
        try:
            live_dict = {}
            for i in self.channels:
                live_dict[i] = False
            live_resopnse = requests.get(self.stream_url + ','.join(self.channels))
            live_resopnse.raise_for_status()
            live_decode = live_resopnse.json()
            for i in live_decode["streams"]:
                live_dict[i["channel"]["name"]] = True
            return live_dict
        except Exception as e:
            raise
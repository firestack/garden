
import time
from IRC import IRC

class TwitchChannel(IRC):

    def __init__(self, host, port, speaker_queue, channels):
        super().__init__(host, port)
        self.running = False
        self.channels = channels
        self.speaker_queue = speaker_queue

    def main_connect(self):
        self.sock_init()
        self.sock_connect()
        self.send_pass("bleh")
        self.send_nick("justinfan7219")
        self.sock_recv(1024)
        self.send_raw("CAP REQ :twitch.tv/tags")
        self.sock_recv(1024)
        for i in self.channels:
            self.send_join(i)
            time.sleep(1)

    def main_loop(self):
        self.main_connect()
        msg = ""
        self.running = True
        while self.running:
            msg += self.sock_recv(2048)
            if msg:
                messages = msg.split("\r\n")
                while len(messages) > 1:
                    current_msg = messages.pop(0)
                    if not current_msg.startswith('@'):
                        continue
                    c_msg = current_msg.split(' ', 4)
                    if c_msg[2] == "PRIVMSG":
                        user = c_msg[1].split('!')[0][1:]
                        target_channel = c_msg[3]
                        self.speaker_queue.put([target_channel, user, "speaking", 1])
                msg = messages[0]
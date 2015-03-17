import socket

class IRC:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def sock_init(self):
        try:
            self.irc = socket.socket()
            self.irc.settimeout(600)
        except Exception as e:
            print("Failed to create socket.")
            raise

    def sock_connect(self):
        try:
            self.irc.connect((self.host, self.port))
        except Exception as e:
            print("Failed to connect to the host.")
            raise

    def send_raw(self, msg):
        self.irc.sendall("{}\r\n".format(msg).encode("utf-8"))

    def send_pass(self, password):
        self.send_raw("PASS {}".format(password))

    def send_nick(self, nick):
        self.send_raw("NICK {}".format(nick))

    def send_join(self, channel):
        self.send_raw("JOIN #{}".format(channel))

    def send_pm(self, channel, msg):
        self.send_raw("PRIVMSG #{} :{}".format(channel, msg))

    def sock_raw_recv(self, amount):
        msg = self.irc.recv(amount)
        if msg:
            return msg
        elif msg == "":
            raise ValueError
        else:
            return None

    def sock_recv(self, amount):
        msg = self.sock_raw_recv(amount)
        try:
            msg = msg.decode("utf-8")
        except AttributeError as e:
            return None

        if msg.startswith("PING"):
            self.send_raw(msg.replace("PING", "PONG"))
        return msg

    def sock_disconnect(self):
        try:
            self.send_raw("QUIT")
        except Exception as e:
            pass
        finally:
            self.irc.close()

    def destroy_socket(self):
        del self.irc
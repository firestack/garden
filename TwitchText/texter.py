import smtplib
import json
import requests
import time
from threading import Thread, Event

run = Event()


class Text:
	credentials = "REDACTED"
	users = "REDACTED"
	@classmethod
	def send(Text, message, opuser=None):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(Text.credentials['user'], Text.credentials['pass'])
		print opuser
		print "send mail to : ",((opuser if opuser is not None else Text.users))
		server.sendmail("bomb", (opuser if opuser is not None else Text.users), message)
		server.quit()

class listener(Thread):
	def __init__(self, channel, users = None):
		super(listener, self).__init__()
		
		self.channel = channel
		self.url = "https://api.twitch.tv/kraken/streams/{user}".format(user=channel)
		self.users = users
		self.last_status = False
		self.sleep_time = 30
		print "Channel : ", self.channel
		print "Users : ",self.users
		print "Request url : ", self.url

	def run(self):
		headers = {'Accept' : 'application/vnd.twitchtv.v3+json'}

		run.wait()
		while run.is_set():
			data = requests.get(self.url, headers = headers)

			
			if data.status_code == 200:


				jsonv = data.json()
				

				if jsonv["stream"] is not None:
					if self.last_status is False:
						try:
							Text.send("{channel} Has gone live with \"{title}\"! Playing: {game}".format(channel=self.channel, title=jsonv["stream"]["channel"]["status"], game=jsonv["stream"]["game"]), opuser=self.users)
							self.last_status = True
						except smtplib.SMTPDataError as e:
							print e
				else:
					self.last_status = False

			else:
				self.last_status = False

			
			print self.last_status
			print (600 if self.last_status else 30)
			time.sleep((600 if self.last_status else 30))

if __name__ == '__main__':
	l = listener("REDACTED")
	
	
	l.setDaemon(True)
	print l.isDaemon()
	run.set()


	l.start()
	
	while True:
		k = raw_input(">>>")
		if k == "stop":
			print "joining thread"
			run.clear()
			l.join()
			
			quit("Game over")




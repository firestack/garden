
import json
import os
import sys
from glob import iglob
#
# Use this bated VV
class Profile(object):


	def __init__(this, name, directory=None, username = None, oauth = None):
		this.nameDict = {}
		if username and oauth:
			this.makeDict(username, oauth)
			this.export((directory if directory else './')+name)
			return
		this.loadFile(name, directory)

	def loadFile(this, name, dirCheck=None):
		if not dirCheck:
			#load file name via importer
			try:
				this.get(name)
				this.fromRaw()

				return
			except Exception as e:
				dirCheck = './'


		if dirCheck:
			#find file name based on username
			absPath = os.getcwd()
			os.chdir(dirCheck)
			for filename in iglob("*.json"):
				print filename
				this.get(filename)
				this.fromRaw()
				if this.raw["profile"]["twitch_username"] == name:
					print "Name found:", this.raw["profile"]["twitch_username"]

					os.chdir(absPath)
					return

				else:
					print "Found non matching name:", this.raw["profile"]["twitch_username"]
					this.raw = None


			os.chdir(absPath)
			return

	def makeFile(this, filename=None):
		this.export((this.name+'.json' if filename == None else filename))

	def get(this, filename):
		with open(filename) as fin:
			this.raw = json.load(fin)

	def export(this, filename):
		with open(filename+'.json', 'w') as fout:
			fout.write(json.dumps({"profile":this.nameDict}))

	def makeDict(this, name=None, oauth=None):
		if name:
			this.nameDict["twitch_username"] = name
			
		else:
			this.nameDict["twitch_username"] = this.name

		if oauth:
			this.nameDict["oauth"] = oauth
			
		else:
			this.nameDict["oauth"] = this.oauth

		if name or oauth:
			this.syncDict()


	def syncDict(this):
		this.name = this.nameDict["twitch_username"]
		this.oauth = this.nameDict["oauth"]

	def fromRaw(this):
		namespace = this.raw["profile"]
		this.name = namespace["twitch_username"]
		this.oauth = namespace["oauth"]

		this.makeDict()

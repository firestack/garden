from math import floor, log

class ffx:
	gold = 0
	compat = 0
	overdrive = False
	level = 1

	characters = {
		"zanmoto":{"char": 80.0, "comp": 4},
		"wakizashi":{"char":48.0, "comp": {"multitarget" : 3, "single": 1}}
	}	
	@classmethod
	def __init__(self):
		pass	

	@classmethod
	def user_input(ffx):
		ffx.gold = float(raw_input("Gold motivation :"))
		ffx.compat = float(raw_input("Compatibility : "))
		ffx.overdrive = str(raw_input("Overdrive? (y/n) : "))

		while not isinstance(ffx.overdrive, bool):

			if ffx.overdrive[0].lower() == "y":
				ffx.overdrive = True
				break
			elif ffx.overdrive[0].lower() == 'n':
				ffx.overdrive = False
				break
			else:
				ffx.overdrive = raw_input("Please input yes or no : ")

		ffx.level = int(raw_input("Level : "))

		ffx.targetPrecent = (raw_input("Target percent?(Leave blank for 100%) : "))
		ffx.targetPrecent = (1 if ffx.targetPrecent == "" else float(ffx.targetPrecent)/100.0)

	@classmethod	
	def calcGold(self, precent = 100):
		overdrive_mod = (20.0 if self.overdrive else 0.0)
		level_mod = (0.8 if self.level < 4 else 0.4)


		for charName, charVal in ffx.characters.items():

			tracker = ffx.targetPrecent

			tracker -= charVal["char"]
			tracker /= -1.0
			tracker -= overdrive_mod
			tracker /= level_mod
			tracker -= (self.compat / 4.0)

			yield (charName, tracker)
	
	@classmethod
	def calcPrecent(self):
		overdrive_mod = (20.0 if self.overdrive else 0.0)
		level_mod = (0.8 if self.level < 4 else 0.4)

		for charName, charVal in ffx.characters.items():
			tracker = 0

			tracker += self.compat / 4.0
			tracker += self.gold
			tracker *= level_mod
			tracker += overdrive_mod
			tracker = charVal["char"] - tracker
			tracker /= 63
			tracker *= 100

			yield (charName, tracker)

	@classmethod
	def goldToGil(self, gold=None, flatten = True):
		if gold is None:
			gold = self.gold
		v = (gold / 4.0)

		if flatten:
			v = floor(v)

		return 2**(v+1)

	@classmethod
	def gilToGold(ffx, gil):
		return (log(gil, 2) - 1)*4

def runtime():
	ffx.user_input()

	print '='*80
	for name, gold in ffx.calcPrecent():
		print ("{:0.2f}% Chance to fail! {:0.2f}% to {charName}!".format(gold, 100.0-gold, charName=name))
		print ("{:10.0f} REQUIRED GOLD!!".format(ffx.goldToGil()))
		
		print '-'*80

	print "_"*80

	for name, gold in ffx.calcGold():
		print name
		print "Compatibility : ", ffx.compat

		print ("{:02.1f}% chance with {} of gold motivation".format(ffx.targetPrecent*100, gold))

		if gold > 112:
			print "LARGER THEN MAX!! More then {:13.0f} gil requred".format(ffx.goldToGil(112))

		print ("{:20.2f} REQUIRED GOLD!!\n".format(ffx.goldToGil(gold)))

		print '-'*80

	print "="*80
	print
	print
		




if __name__ == '__main__':
	while True:
		runtime()





"""
( ( 80 - ( 20 + ( ( X + (   Y / 4 ) ) * 0.4 ))) / 63 ) * 100
Put the 20 between the 80 and the formula.
That should do it.
I don't know what I find so enjoyable about making and debugging these formulas, I just do.

calc = lambda character, gold, compat : ((character - (((compat / 4.0) + gold) * (0.8 if level < 4 else 0.4) + (20.0 if overdrive else 0.0)) / 63.0 ) *100.0
(0.8 if level < 4 else 0.4) + (20 if overdrive else 0)
(character - (compat / 4.0))
	( 80 - ((( X + (   Y / 4 ))  0.4 ) + 20)) / 63 )  100

((( character - ( gold + ( compat / 4.0 )) * (0.8 if level < 4 else 0.4) + (20 if overdrive else 0))) / 63.0) * 100

(((character - ((compat / 4.0) + gold) * (0.8 if level < 4 else 0.4)) + (20.0 if overdrive else 0.0)) / 63.0 ) *100.0

"""

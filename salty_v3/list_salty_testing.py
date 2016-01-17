#incoming message

for alt in ["glacials", "bated", "bomb"]:
	if alt == 'bated':
		message = "I am bated and I hate emotes"

	elif alt == 'glacials':
		message = "I am glacials and I'm pretty cool CatBag"

	else:
		message = "Hello world I am bombmask FrankerZ BibleThump ZreknarF"

	message_list = message.split(' ')
	message_list_lowered = message.lower().split(' ')

	#resources
	##I think you know how all this works
	emotes = "FrankerZ BibleThump ZreknarF".split(' ')
	ffz_emotes = "ZreknarF LilZ CatBag".split(' ')
	users = 'Bombmask batedurgonnadie glacials'.lower().split(' ')

	#lambda of the function to test
	any_in_lambda = lambda x, y: any(i in y for i in x)

	def any_in_func(a,b):
		return any(i in b for i in a)

		#expanded form
		for i in b:
			if i in a:
				return True

	print "Incoming message is :",message
	print "Message as list     :",message_list

	print

	print "Were there users in the message?( lambda ) :",any_in_lambda(message_list_lowered, users) 
	print "Were there users in the message?(function) :",any_in_func(message_list_lowered, users) 

	print 

	print "Were there emotes in the message?( lambda ) :",any_in_lambda(message_list, emotes)
	print "Were there emotes in the message?(function) :",any_in_func(message_list, emotes)

	print

	print "Were there ffz emotes in the message?( lambda ) :",any_in_lambda(message_list, ffz_emotes)
	print "Were there ffz emotes in the message?(function) :",any_in_func(message_list, ffz_emotes)

	print
font = {
	"filename": "FontAwesome.ttf"
}
with open(font["filename"]) as fin:
	count = 0
	LINE_LENGTH = 5
	for line in fin:
		for byte in line:
			count += 1
			print str(hex(ord(byte)))+'\t'
			if count%LINE_LENGTH == 0:
				print

Dedvar = raw_input()
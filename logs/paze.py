# remove the Asterix line seperator in the vbMail.log ( vb == Verbose )


cap = []
i = 0
with open('vbMail.log', 'r') as f:
	for line in f:
		if line.strip() == '******************************************************************':
			i = i + 1
			newFile = open('./parsed/{}_m.txt'.format(i), 'w')
			newFile.write("".join(cap))
			newFile.close()
			cap = []
		else:
			cap.append(line)

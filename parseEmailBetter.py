from email.message import EmailMessage
import email

def openMail(path):
	content = None
	with open(path, 'r') as f:
		content = f.readlines()

	return content


def parseEmailText(content):
	_ret = []
	_msg = email.message_from_string(content)
	if _msg.is_multipart():
		for payload in _msg.get_payload():
			_ret.append(payload)
	else:
		_ret.append(_msg.get_payload)

	return _ret

def getTextBody(emailMessages):
	for emailMsg in emailMessages:
		if  emailMsg.get_content_type() == 'text/plain':
			return emailMsg.get_payload()
	return None
	
def cleanEmailText(emailText):
	_clean = emailText.replace('\n', ' ')
	return _clean

def run(path):
	emailText = openMail(path)
	emailMessages = parseEmailText(''.join(emailText))
	emailText = getTextBody(emailMessages)
	emailText = cleanEmailText(emailText)
	return emailText




if __name__ == '__main__':
	text = run("./logs/parsed/63_m.txt")
	print(text)



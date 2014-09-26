import re, os

chat = {}

# use this path when it is hooked up with the app
# chat_history = open('app/uploads/upload.txt', 'r')

# use this path when running parser.py alone
# chat_history = open('uploads/upload.txt', 'r')

# define message object with two attributes

# message.time = timestamp
# message.data = data

# convo = [{sender: [message, message... ]}, {sender: [message, message... ]]}

# read file line by line and save to array accordingly

def parse():
	chat_history = open('app/uploads/upload.txt', 'r')
	for line in chat_history:
		string = line
		line = re.split(r'\t+', string)
		date = line[0]
		time = line[1]
		timestamp = date + " " + time
		participant = line[4]
		direction = line[2]
		if direction == 'in':
			sender = participant
		else:
			sender = 'You'
		data = line[5]
		data = data[:-2]
		if chat.has_key(sender):
			message = [timestamp, data]
			chat[sender].append(message)
		else:
			chat[sender] = []
			message = [timestamp, data]
			chat[sender].append(message)
	return chat
import requests

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox6e009863be434327b106ca08fa1cf103.mailgun.org/messages",
		auth=("api", "YOUR_API_KEY"),
		data={"from": "Excited User <mailgun@sandbox6e009863be434327b106ca08fa1cf103.mailgun.org>",
			"to": ["jenny_essery@hotmail.co.uk", "jennifer.m.essery@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})


send_simple_message()

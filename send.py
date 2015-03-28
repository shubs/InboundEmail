# {{description}}
import requests, json

def send(frm, to, subject, text):
	url = "https://api.mailjet.com/v3/send/message"
	pl = {
		"from": frm,
		"to": to,
		"subject": subject,
		"text": text
		}
	r = requests.post(url, data=pl, auth=('bceadfaa7964918eac0a078383166e75', '58a9b89dd1b8e2fba9dc91bf63ab4225'))

	print json.dumps(r.json());

send("Shubham SHllMA <shubham+v3@mailjet.com>", "shubs92@gmail.com", "cool guy", "hey man")
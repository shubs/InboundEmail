import os
import pprint
import time
from flask import Flask, request, render_template
from firebase import firebase
firebase = firebase.FirebaseApplication('https://parseapi.firebaseio.com/', None)
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html',
                           title='Home',
                           requestData=request,
                           mainText='Here is just the home page',
                           data=request.form)

@app.route("/inbound/", methods=['GET', 'POST'])
def inbound():
    if request.method == 'POST':
        data = parse(request.form)
        return render_template('index.html',
                                title='Inbound',
                                requestData=request,
                                mainText='Got it !',
                                data=request.form)
    else:
        data = listingInbounds()
        return render_template('list.html',
                                title='Inbound',
                                mainText='list of mail recieved on this url',
                                data=data)

def listingInbounds():
    data = firebase.get('/mails', None)
    return data

def parse(data):
    pusableData = data.copy()
    pusableData.add('time', time.strftime("%c"))
    snapshot = firebase.post('/mails', pusableData)
    pprint.pprint(pusableData)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
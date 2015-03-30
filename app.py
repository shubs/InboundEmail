import os
import pprint
import time
import json
from flask import Flask, request, render_template
from firebase import firebase
firebase = firebase.FirebaseApplication('https://parseapi.firebaseio.com/', None)
app = Flask(__name__)

def fwdPost(data):
    return data

#this function just convert a dict in list for beter template handling
def dictolist(dico):
    l = []
    for key in dico:
        dico[key]['id'] = key;
        l.append(dico[key]);
    return l

# No real use
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/inbound/", methods=['GET', 'POST'])
def inbound():
    if request.method == 'POST':
        data = parse(json.loads(request.data))
        return render_template('index.html',
                                title='Inbound',
                                requestData=request,
                                mainText='Got it !',
                                data=data)
    elif request.method == 'GET':
        data = listingInbounds()
        return render_template('list.html',
                                title='Inbound',
                                mainText='List of emails on the parse API',
                                data=data,
                                length=len(data))

def listingInbounds():
    dico = firebase.get('/mails', None)
    l = dictolist(dico)
    return l

def parse(data):
    pusableData = data
    snapshot = firebase.post('/mails', pusableData)
    return pusableData

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
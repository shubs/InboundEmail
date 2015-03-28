import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Parse API Server!"

@app.route("/inbound/", methods=['GET', 'POST'])
def inbound():
    if request.method == 'POST':
        parse()
    else:
        listingInbounds()

def listingInbounds():
    return "list of inbounds"

def parse():
    dump(request)
    return "thx"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
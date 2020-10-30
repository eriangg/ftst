from flask import Flask
application = Flask(__name__)
import socket
import datetime
import os
import pprint

@application.route("/")
def hello():
    e = pprint.pformat(os.environ)    
    return "Hejsan Världen from %s at %s!!!\n<br>%s" % (
     socket.gethostname(), str(datetime.datetime.now()), e)

if __name__ == "__main__":
    application.run()

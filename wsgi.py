from flask import Flask
application = Flask(__name__)
import socket
import datetime

@application.route("/")
def hello():
    return "Hejsan Världen from %s at %s!\n" % (socket.gethostname(), str(datetime.datetime.now()))

if __name__ == "__main__":
    application.run()

from flask import Flask
application = Flask(__name__)
import socket

@application.route("/")
def hello():
    return "Hejsan Världen from %s!" % socket.gethostname()

if __name__ == "__main__":
    application.run()

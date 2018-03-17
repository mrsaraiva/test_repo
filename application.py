from flask import Flask


application = Flask(__name__)
application.debug = True
@application.route('/', methods=['GET'])

def hello():
    VERSION = '0.14'
    str = '<p>Hello, world!<br><br> This is version {}</p>'.format(VERSION)
    return str


if __name__ == "__main__":
    application.run()
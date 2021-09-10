from flask import Flask

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def rotaGet():
    return u'olá mundo!'


@app.route('/post', methods=['POST'])
def rotaPost():
    return u'olá mundo!'


@app.route('/postget', methods=['POST', 'GET'])
def rotaPostEGet():
    return u'olá mundo!'


if __name__ == '__main__':
    try:
        app.run()
    except:
        pass

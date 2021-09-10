from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/<int:id>')
def rota(id="undefined"):
    return jsonify(
        {
            'id': id,
            'nome': 'wayne'
        })


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except:
        pass

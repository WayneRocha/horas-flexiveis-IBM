from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        'id': 0,
        'nome': 'Wayne',
        'habilidades': [
            'Javascript',
            'Python',
            'Flask',
            'HTML',
            'CSS'
        ]
    },
    {
        'id': 1,
        'nome': 'Duda',
        'habilidades': [
            'Java',
            'HTML',
            'CSS'
        ]
    },
    {
        'id': 2,
        'nome': 'Nayara',
        'habilidades': [
            'UX/UI',
            'HTML',
            'CSS',
            'JS'
        ]
    }
]


@app.route('/dev/<int:id>/', methods=["GET", "PUT", "DELETE"])
def dev(id):
    try:
        if request.method == "GET":
            return jsonify(developers[id])
        elif request.method == "PUT":
            response = json.loads(request.data)
            developers[id] = response
            return jsonify({"status": "sucess"})
        elif request.method == "DELETE":
            developers.pop(id)
            return jsonify({"status": "sucess"})
    except IndexError:
        return jsonify({"status": "IndexError"})


@app.route('/dev/all/', methods=["GET", "POST"])
def allDevs():
    try:
        if request.method == "POST":
            response = json.loads(request.data)
            response["id"] = (developers[-1]["id"]) + 1
            developers.append(response)
        elif request.method == "GET":
            return jsonify(developers)
    except Exception as e:
        print(f'log: {e}')
        return jsonify({"status": 404})
    else:
        return jsonify({"status": 200})


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except:
        pass

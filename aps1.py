from flask import Flask, redirect, url_for, request, Response
from flask_restful import Api, Resource
import json

app = Flask(__name__)

dic={}
count=0
class Tarefas:
    def __init__(self,id,task):
        self.id = id
        self.task = task

@app.route('/Tarefa', methods=['GET', 'POST'])
def Tarefa():
    global dic
    global count
    if request.method == 'POST':
        data = json.loads(request.data)
        dic[count] = Tarefas(count,data['task'])
        count += 1
        return json.dumps({'status': 200}), 200
    else:
        return json.dumps([task.__dict__ for task in list(dic.values())])

@app.route('/Tarefa/<id>', methods=['GET', 'PUT', 'DELETE'])
def tarefa_id(id):
    global dic
    global count
    id = int(id)

    if request.method == 'PUT':
        data = json.loads(request.data)
        if id in dic:
            dic[id] = Tarefas(id, data['task'])
            return json.dumps({'status': 200}), 200
        else:
            return json.dumps({'status': 204}), 204
    elif request.method == 'DELETE':
        if id in dic:
            del dic[id]
            return json.dumps({'status': 200}), 200
        else:
            return json.dumps({'status': 204}), 204
    else:
        return json.dumps(dic[id].__dict__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return Response(status=200)

app.run(host='0.0.0.0', port=5000)
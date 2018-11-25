from flask import Flask, redirect, url_for, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)

dic={}
count=0
class Tarefas:
    def __init__(self,id,nome):
        self.id = id
        self.task = task

@app.route('/Tarefa', methods=['GET', 'POST'])
def Tarefa():
    global dic
    global count
    if request.method == 'POST':
        data = json.loads(request.data)
        dict[count] = Tarefas(count,data['task'])
        count += 1
        return json.dumps({'status': 200}), 200
    else:
        return json.dumps(dic)

@app.route('/Tarefa/<id>', methods=['GET', 'PUT', 'DELETE'])
def tarefa_id(id):
    global dic
    global count
    id = int(id)

    if request.method == 'PUT':
        data = json.loads(request.data)
        if id in dic:
            dic[id] = Tarefas(id, data['task'])
            return Response(status=200)
        else:
            return Response(status=404)
    elif request.method == 'DELETE':
        if id in dic:
            del dic[id]
            return Response(status=200)
        else:
            return Response(status=204)
    else:
        return json.dumps(Tarefas[id])

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return Response(status=200)

app.run(host='0.0.0.0', port=5000)
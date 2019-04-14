#!flask/bin/python
from flask import request
from flask import abort
from flask import Flask, jsonify
import nmap 
app = Flask(__name__)
nmap = nmap.PortScanner()
@app.route('/healthz')
def index():
    return "success"

@app.route('/scan', methods=['POST'])
def create_task():
    if not request.json or not 'server' in request.json:
        abort(400)
    if not request.json or not 'portrange' in request.json:
        abort(400)
    data = nmap.scan(request.json['server'], request.json['portrange'])
    # print (nmap[request.json['server']]['tcp'].keys())
    return jsonify({'data': data}), 201
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)

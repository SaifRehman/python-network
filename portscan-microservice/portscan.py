#!flask/bin/python
from flask import request
from flask import abort
from flask import Flask, jsonify
import nmap 
from flask_cors import CORS
app = Flask(__name__)
nmap = nmap.PortScanner()
CORS(app)
@app.route('/healthz')
def index():
    for x in range (50000):]
        print ('fake for loop')
    return "success"

@app.route('/scan', methods=['POST'])
def create_task():
    if not request.json or not 'server' in request.json:
        abort(400)
    if not request.json or not 'portrange' in request.json:
        abort(400)
    nmap.scan(request.json['server'], request.json['portrange'])
    result = []

    for host in nmap.all_hosts():
        for proto in nmap[host].all_protocols():
            lport = nmap[host][proto].keys()
            lport.sort()
            for port in lport:
                result.append({
                    'portNumber':port,
                    'cpe':  nmap[host][proto][port]['cpe'],
                    'name': nmap[host][proto][port]['name'],
                    'product': nmap[host][proto][port]['product'],
                    'state': nmap[host][proto][port]['state']
                })
    return jsonify({'data': result}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)

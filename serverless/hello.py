import nmap 
from flask import Flask, jsonify

def main():
    nmap = nmap.PortScanner()
    data = nmap.scan('127.0.0.1','22-443')
    return jsonify({'data': data}), 201
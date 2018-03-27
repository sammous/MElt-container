# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import subprocess
from tempfile import NamedTemporaryFile
import json

app = Flask(__name__)

@app.route('/pos', methods=['POST'])
def pos():
    try:
        json_data = request.json['data']
        with NamedTemporaryFile(mode='r+w', delete=False) as f:
            path = f.name
            f.write(json_data)
            f.read()
            ps = subprocess.Popen(('cat', path), stdout=subprocess.PIPE)
            output = subprocess.check_output(('MElt'), stdin=ps.stdout)
            f.close()
        return output
    except Exception as e:
	    return(str(e))

@app.route('/lemma', methods=['POST'])
def lemma():
    try:
        json_data = request.json['data']
        with NamedTemporaryFile(mode='r+w', delete=False) as f:
            path = f.name
            f.write(json_data)
            f.read()
            ps = subprocess.Popen(('cat', path), stdout=subprocess.PIPE)
            output = subprocess.check_output(('MElt', '-L'), stdin=ps.stdout)
            f.close()
        return output
    except Exception as e:
	    return(str(e))

@app.route('/pos_and_tokenize', methods=['POST'])
def pos_and_tokenize():
    try:
        json_data = request.json['data']
        with NamedTemporaryFile(mode='r+w', delete=False) as f:
            path = f.name
            f.write(json_data)
            f.read()
            ps = subprocess.Popen(('cat', path), stdout=subprocess.PIPE)
            output = subprocess.check_output(('MElt', '-t'), stdin=ps.stdout)
            f.close()
        return output
    except Exception as e:
	    return(str(e))

@app.route('/tokenize', methods=['POST'])
def tokenize():
    try:
        json_data = request.json['data']
        f = NamedTemporaryFile(delete=False)
        f.write(json_data)
        ps = subprocess.Popen(('cat', f.name), stdout=subprocess.PIPE)
        output = subprocess.check_output(('sxpipe-light'), stdin=ps.stdout, shell=True)
        f.close()
        return output
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def seedNumber():
   if request.method == 'GET':
      return socket.gethostname()
   elif request.method == 'POST':
        cmd = ['python3', 'stress_cpu.py']
        proc = subprocess.Popen(cmd)
        return 'posted'
   else:
      return 'Not supported'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

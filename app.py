from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flasik!'

@app.route('/github-deploy', methods=['POST'])
def github_deploy():
    return 'POST request to /github-deploy received', 200

if name == '__main__':
    app.run(debug=True, port=5002)

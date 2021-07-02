import os
from flask import Flask, json, request
import controller.AccountController
from model.AccountModel import Account
from model.AccountModel import Message
from flask_cors import CORS
import DbConnect

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    item = {
        'username': 'manh123',
        'password': 'manh',
        'id': '123'
    }
    return json.dumps(item)


@app.route('/login', methods=['GET', 'POST'])
def login_chat_app():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    s = controller.AccountController.login_chat_app(username, password)
    return s


@app.route('/home', methods=['GET', 'POST'])
def POST_message_chat_app():
    data = request.json
    id_user = data.get('id_user')
    messages = data.get('messages')
    time = data.get('time')
    s = controller.AccountController.POST_message_chat_app(id_user, messages, time)
    return s



if __name__ == '__main__':
    app.run()

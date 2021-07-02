from flask import Flask, json, request
from model.AccountModel import Account
from model.AccountModel import Message


def login_chat_app(username, password):
    return Account.login(0, username, password)


def POST_message_chat_app(id_user, messages, time):
    mes = Message(id_user, messages, time)
    return mes.post_message()




import json

from DbConnect import getConnection


class Account:
    id = 0
    username = ''
    pass_word = ''

    def __init__(self, id, uname, pword):
        self.id = id
        self.username = uname
        self.pass_word = pword

    def login(self, user, pw):
        myConnect = getConnection()
        sql_query = 'SELECT * ' \
                    'FROM app_chat.user ' \
                    'where user.username like %s and user.password like %s'
        cursor = myConnect.cursor()
        cursor.execute(sql_query, (user, pw))
        record = cursor.fetchone()
        item = {
            'id': record[0],
            'username': record[1],
            'password': record[2]
        }
        myConnect.close()
        cursor.close()
        return json.dumps(item)


class Message:
    id = '',
    id_user = '',
    messages = '',
    time = ''

    def __init__(self, id_user, messages, time):
        self.id_user = id_user
        self.messages = messages
        self.time = time

    def post_message(self):
        myConnect = getConnection()
        sql_query = 'INSERT INTO app_chat.message (id_user,messages,time) VALUES (%s,%s,%s)'
        cursor = myConnect.cursor()
        cursor.execute(sql_query, (self.id_user, self.messages, self.time))
        myConnect.commit()
        myConnect.close()
        myConnect = getConnection()
        sql_query_out = 'SELECT * FROM app_chat.message'
        cursor_out = myConnect.cursor()
        cursor_out.execute(sql_query_out)
        arr = []
        for record in cursor_out.fetchall():
            data = {
                'id_user': record[1],
                'messages': record[2],
                'time': record[3]
            }
            arr.append(data)
        cursor_out.close()
        myConnect.close()
        list = {"data_chat": arr}
        return json.dumps(list)

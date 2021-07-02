import json

import mysql.connector


def getConnection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0975842314a",
        auth_plugin='mysql_native_password'
    )
    return db

# def login(user, pw):
#     myConnect = getConnection()
#     sql_query = 'SELECT * ' \
#                 'FROM bkav_chat._account acc ' \
#                 'where acc.user_name like "huynqn" and acc.pass_word like "1"'
#     cursor = myConnect.cursor()
#     cursor.execute(sql_query)
#     record = cursor.fetchall()
#     # item = {
#     #     'id': record[0],
#     #     'username': record[1],
#     #     'password': record[2]
#     # }
#     cursor.close()
#     myConnect.close()
#     return json.dumps('item')

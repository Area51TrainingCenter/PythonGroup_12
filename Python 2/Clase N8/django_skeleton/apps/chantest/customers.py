from channels import Group
import threading
import random

def sendmsg(num):
    Group('stocks').send({'text': num})

t = 0

def periodic():
    global t
    n = random.randint(10, 200)
    sendmsg(str(n))
    t = threading.Timer(5, periodic)
    t.start()

def ws_message(message):
    global t
    print(message.content['text'])
    if message.content['text'] == 'start':
        periodic()
    else:
        t.cancel()

def connect(message):
    Group('stocks').add(message.reply_channel)
    Group('stocks').send({'text': 'connected'})


def disconnect(message):
    Group('stocks').send({'text': 'disconnected'})
    Group('stocks').add(message.reply_channel)

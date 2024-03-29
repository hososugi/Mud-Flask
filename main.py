#

from flask import Flask, render_template
from flask_socketio import SocketIO

from app.DataManager import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


def message_received(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=message_received)


if __name__ == '__main__':
    DataManager.load_data()
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)

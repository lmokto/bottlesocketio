#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from gevent import monkey
import time

monkey.patch_all()
app = bottle.Bottle()

class TestNamespace(BaseNamespace):
    def on_join(self, msg):
        if msg == "segundo":
          while True:
            self.emit('recive', 'segundo')
            time.sleep(10)
        elif msg == "quinto":
          while True:
            self.emit('recive', 'quinto')
            time.sleep(10)

@app.get('/')
@app.get('/quinto')
def root():
    return bottle.template('quinto')

@app.get('/segundo')
def root():
    return bottle.template('segundo')

@app.get('/_static/<filepath:path>')
def get_static(filepath):
    return bottle.static_file(filepath, root='./static/')

@app.get('/socket.io/<path:path>')
def socketio_service(path):
    socketio_manage(bottle.request.environ,
                    {'/test': TestNamespace}, bottle.request)

if __name__ == '__main__':
    bottle.run(app=app,
               host='127.0.1.1',
               port=8081,
               server='geventSocketIO',
               debug=True,
               reloader=True,
              )

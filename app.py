#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from gevent import monkey
import time
import os

monkey.patch_all()
app = bottle.Bottle()

try:
    zvirtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'],
                            'virtenv', 'bin', 'activate_this.py')
    execfile(zvirtenv, dict(__file__=zvirtenv))
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
except:
    ip = "0.0.0.0"
    port = 8080

class TestNamespace(BaseNamespace):
    def on_recive(self, msg):
        if msg == "segundo":
          while True:
            self.emit('send', 'segundo')
            time.sleep(10)
        elif msg == "quinto":
          while True:
            self.emit('send', 'quinto')
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
                    {'/connection': TestNamespace}, bottle.request)

if __name__ == '__main__':
    bottle.run(app=app,
               host=ip,
               port=port,
               server='geventSocketIO',
               debug=True,
               reloader=True,
              )

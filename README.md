#####Instalacion

```sh
pip install bottle gevent gevent-socketio
```
#####Start the web server.

```sh
python setup.py install
python app.py
```
Open web browser to http://127.0.1.1:8080/

#####Start in OpenShift Cloud.

```sh
rhc app create bottlesocketio python-2.7
rhc app stop -a bottlesocketio
rhc app start -a bottlesocketio

curl http://bottlesocketio-<yourdomain>.rhcloud.com/
```

Open web browser to http://bottlesocketio-yourdomain.rhcloud.com/

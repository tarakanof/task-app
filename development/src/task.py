from flask import Flask
from flask_prom import monitor

simple_http = Flask("Task")

@simple_http.route("/")
def index():
    return "<h2>Hello, world!</h2>"

simple_http.wsgi_app = monitor(simple_http, path="/metrics")
simple_http.run(host="0.0.0.0", port=80, debug=False)

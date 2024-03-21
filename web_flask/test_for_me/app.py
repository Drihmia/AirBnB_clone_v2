#!/usr/bin/python3
"""this modulefor testing and discovring flask library for web framwork porposes"""
from flask import Flask, escape, url_for
import os


app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<p>Hello Word!</p><div>This a div <h1>That contains a h1 title</h1></div>"

@app.route("/<int:num>")
def html_int(num):
    if not os.path.exists("../../web_static/{}-index.html".format(num)):
        return "int page not found", 404
    with open("../../web_static/{}-index.html".format(num), "r", encoding="utf-8") as html_file:
        content = html_file.read()
        return content

@app.route("/<float:n>")
def html_float(n):
    return "float not foundd", 404

@app.route("/<path:path>")
def html_path(path):
    if not os.path.exists("../../{}".format(path)):
        return "path not found", 404
    with open("../../{}".format(path), "r", encoding="utf-8") as html_file:
        content = html_file.read()
        return content

@app.route("/<string:name>")
def hello_name(name):
    return "hello, {}!".format(escape(name))

@app.route("/dri")
def dri_to_red():
    return "<a href={}>Click to red</a> to visit red's page".format(url_for('hello_name', name="redouane drihmia"))


# witout "/" make it unique, if it's being used with a "/", it gives 404.
@app.route("/yas")
def test_slash_1():
    return "<h1>/yasmine</h1>!"


# forwarding the 1st URL to the 2nd one, response of: 308 PERMANENT REDIRECT.
@app.route("/red", strict_slashes=False)
@app.route("/red/")
def test_slash():
    return f"<h1>{url_for('test_slash')}</h1>"


# being used with "/" makes it accessible with or without "/", response of:
# +308 PERMANENT REDIRECT.
#
# using strict_slashes=False, make response always as 200.
# Note: strict_slaches by default set to FALSE
@app.route('/projects/', strict_slashes=False)
def projects():
    return 'The project page, + "/" + strict_slashes=False'

# strict_slashes being set to True, repspond with 308 if no "/" 
@app.route('/project/', strict_slashes=True)
def project():
    return 'The project page, + "/" + strict_slashes=True'

with app.test_request_context():
    print("------------------------------")
    print("------------------------------")
    print("------------------------------")
    print("------------------------------")
    print("------------------------------")

if __name__ == "__main__":
    app.run(debug=True)

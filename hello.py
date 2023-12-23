from flask import Flask, render_template
app = Flask(__name__)

FLASKQUICKSTART = "https://flask.palletsprojects.com/en/3.0.x/quickstart/"

@app.route("/")
def hello_world():
  return "<p><a href=/resources>Hello, World!</a></p>"

@app.route("/resources")
def resources():
  return render_template("linkbutton.html", link=FLASKQUICKSTART, 
                         text="Get started with Flask")

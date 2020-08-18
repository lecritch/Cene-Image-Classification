from flask import Flask, render_template, url_for
import os
import random

demo_images = os.listdir('static/images')

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    images = list(map(lambda x: url_for('static', filename='images/' + x), demo_images))
    random.shuffle(images)
    return render_template("home.html", images=images)

if __name__ == "__main__":
    app.run(debug = True)
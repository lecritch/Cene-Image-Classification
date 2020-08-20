from flask import Flask, render_template, url_for
import os
import random
import pickle
import time

demo_images = list(filter(lambda x: '.jpg' in x, os.listdir('static/images/imgs/')))

with open('predictions/demo_preds.pickle', 'rb') as f:
    predictions = pickle.load(f)

app = Flask(__name__)

@app.route("/home", methods=['GET'])
@app.route("/")
def home():
    images = list(map(lambda x: url_for('static', filename='images/imgs/' + x), demo_images))
    random.shuffle(images)
    return render_template("home.html", images=images)

@app.route("/sort", methods=['POST'])
def sort():
    time.sleep(1)
    return render_template("sort.html", image_preds = predictions)


if __name__ == "__main__":
    app.run(debug = True)
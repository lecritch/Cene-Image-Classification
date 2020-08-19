from flask import Flask, render_template, url_for
import os
import random

demo_images = os.listdir('static/images/imgs')

pred_dict = {'building': demo_images[:10], 'forest': demo_images[10:20], 'glacier': demo_images[20:]}

app = Flask(__name__)

@app.route("/home", methods=['GET'])
@app.route("/")
def home():
    images = list(map(lambda x: url_for('static', filename='images/imgs' + x), demo_images))
    random.shuffle(images)
    return render_template("home.html", images=images)

@app.route("/sort", methods=['POST'])
def sort():
    return render_template("sort.html", image_preds = pred_dict)


if __name__ == "__main__":
    app.run(debug = True)
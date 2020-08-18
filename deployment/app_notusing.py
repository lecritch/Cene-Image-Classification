from flask import Flask, request, redirect, url_for, render_template
from keras.preprocessing.image import load_img
import os
import sys

module_path = os.path.abspath(os.path.join(os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)

from src import preprocessing as pp

parent_dir = '../'

twenty_images = pp.get_paths(parent_dir + 'data/seg_test')[:20]

test_img = twenty_images[0]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    start_body = """
    <html>
    """

    title_bar = """
    <head>
        <title>Cene</title>
    </head>
    """

    header = """
    <body>
    	<div class="container">
            <h1>Cene - An Image Organisation Application</h1>
        </div>
    """

    # print out images
    images = f"""
    <div class="images">
        <image src="{{ url_for('static', filename='images/38.jpg') }}">
    """
    # for img in twenty_images:
    #     images += f"""
    #     <img src={img} alt='Test Image' width='150' height='150'>
    #     """

    button = """
    <input class="button" type="submit" value="Sort Photos">
    """

    end_body = """
            </div>
        </body>
    </html>
    
    """
    # opening html tag
    body = start_body

    # concat all body content variables
    body += title_bar + header + images + button

    # closing html tag
    body += end_body


    # tests:
    for img in twenty_images:
        print(img)

    return body


if __name__ == '__main__':
    app.run(debug = True)
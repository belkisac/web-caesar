from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="rot">
                Rotate by:
                <input type="text" id="rot" value="0" name="rot />
            </label>
            <label for="text">
            <textarea id="text" name="text"></textarea>
            </label>
            <input type="submit" />
        </form>
    </body>

</html>
"""
@app.route('/')
def index():
    return form

@app.route('/', methods=['POST'])
def encrypt():
    

app.run()
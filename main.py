from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="rot">
                Rotate by:
                <input type="text" id="rot" value="0" name="rot" />
            </label>
            <label for="text">
            <textarea id="text" name="text">{0}</textarea>
            </label>
            <input type="submit" />
        </form>
    </body>

</html>
"""
@app.route('/')
#renders form
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    plaintext = request.form['text']

    encrypted = rotate_string(plaintext,rotation)

    return form.format(encrypted)

app.run()
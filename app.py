from flask import Flask

app = Flask(__name__)
# you can write what every key you perfer in here
app.config['SECRET_KEY'] = 'secret-key'

from routes import *

if __name__ == "__main__":
    app.run(debug=True)

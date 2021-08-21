from flask import Flask 

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'welcome to <h1>My World</h1> using flask framework'

if __name__ == "__main__":
    app.run(debug=True)

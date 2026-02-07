import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nome')
def exibir_nome():
    return "Willian Gouveia!"


if __name__ == '__main__':
    app.run(
        host=os.getenv("FLASK_HOST"),
        port=os.getenv("FLASK_PORT"),
        debug=os.getenv("FLASK_DEBUG") == "1"
        )
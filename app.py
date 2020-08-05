#to run this, simply run 'python app.py' in terminal and then go to localhost:5000 on your browser

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True) #debug MUST be turned off for production

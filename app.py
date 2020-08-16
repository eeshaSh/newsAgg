#to run this, simply run 'python app.py' in terminal and then go to localhost:5000 on your browser

from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

@app.route('/')
def index():
    #from https://medium.com/@toivo1996/flask-and-tweepy-library-59cbce13c101 ####
    auth = tweepy.OAuthHandler('ppFASgcc3BMiq3ylMp59PGwE1', 'jRYK3p6uj2D6VehbfbWEkOgQgHs8lBD1Dh5TFjNQCTtrAXAIZs')
    auth.set_access_token('1294176965893787649-AzuydqVxGkdJUd2OGJLNRHeylSL3I4', 'b3QrJOwDua8twHu8QaPELOzwMU3lL2u5AjEO0TQz7OIa0')
    api = tweepy.API(auth)
	
    search = request.args.get('q')	
    #public_tweets = api.user_timeline(search)
    return render_template('index.html', tweets=api.user_timeline(search))

if __name__ == "__main__":
    app.run(debug = True) #debug MUST be turned off for production

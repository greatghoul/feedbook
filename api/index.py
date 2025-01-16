from flask import Flask, Response
from .feeds import feedbooks

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/feed/<string:key>')
def feed(key):
    if key in feedbooks:
        feed = feedbooks[key].fetch_feed()
        rss_feed = feed.rss_str(pretty=True)
        return Response(rss_feed, mimetype='application/rss+xml')
    else:
        return 'Feed not found', 404

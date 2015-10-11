#!/usr/bin/python
import json
from flask import Flask, request, Blueprint
import flask
from extractEntities2 import tag_tweets

api_endpoint = dict(
    host='localhost',
    port=9011,
    base_url='/twitner/api',
    bp_name='twitner'
)

bp = Blueprint(api_endpoint['bp_name'], __name__)
app = Flask(__name__)

@bp.route('/get_tags', methods=['GET', 'POST', 'OPTIONS'])
def get_tweet_tags():
    tweets = request.args.getlist('tweets')
    status = 0
    res = dict()
    try:
        res.update({"result": tag_tweets(tweets)})
        status = 1
    except Exception, e:
        print e

    res.update({'status': status})
    return flask.jsonify(res)

if __name__ == "__main__":
    app.register_blueprint(bp, url_prefix=api_endpoint['base_url'])
    app.run(host=api_endpoint['host'], port=api_endpoint['port'])

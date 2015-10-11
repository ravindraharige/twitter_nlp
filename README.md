Twitter NLP Named Entity Recognition HTTP Service
====================
Added a simple HTTP API to get NER tagged tweets using @ritter's twitter_nlp library (https://github.com/aritter/twitter_nlp)

Example Usage:
--------------

	export TWITTER_NLP=./
	python python/ner/service.py

Note: this takes a minute or so to read in models from files. The api endpoint settings like hostname, port number, application name, etc. can be configured in service.py file itself. To include classification, pos, chunk feature - there are boolean flags in extractEntities2.py module, please change the values accordingly and run the service.py.

Example function on how to invoke the service.

	   def get_tagged_tweets(list_of_tweets):
    		data = {'tweets': list_of_tweets}
    		headers = {'content-type': 'application/json'}
    		url = "http://localhost:9011/twitner/api/get_tags"
    		resp = requests.get(url, params=data, headers=headers)
    		js_resp = json.loads(resp.text).get('result')
    		return js_resp


Output of the API is in JSON format.



Twitter NLP Named Entity Recognition HTTP Service
====================
Added a simple http api to get NER tagged tweets. These changes were made mainly to make use of Twitter NER in non-python based projects.

Forked from https://github.com/aritter/twitter_nlp.

Example Usage:
--------------

	export TWITTER_NLP=./
	python python/ner/service.py

Note: this takes a minute or so to read in models from files. The api endpoint settings like hostname, port number, application name, etc. can be configured in service.py file itself. To include classification, pos, chunk feature - there are boolean flags in extractEntities2.py module, please change the values accordingly and run the service.py.

	payload = {'tweets': list_of_tweet_texts_to_be_tagged}
	just use this paylod variable as value of API's 'data' argument.


Output of the API is in JSON format. 

	{'status': 0}  -- in case of API call failure, please cheack back again.
	{'status': 1, result: [{entities: [], tagged_tweet: '', tweet_text: ''}]  
	--- in case of API call success, returns status code 1 where entities is empty array if no NER specific texts found, 		otherwise contains named entitied that are found in tweets in payload



build:
	docker build --no-cache -t tweepy .

container:
	docker run --env-file .env --rm -it tweepy /bin/bash

run:
	docker run --env-file .env --rm -it tweepy python tweet_liked.py

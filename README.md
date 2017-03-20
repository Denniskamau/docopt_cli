docopt command line application
=====================

This repository contains example of a docopt command line application.

Using the Twitter API
---------------------

To use the example programs you will need to register a new client application
with Twitter. To do this, login into https://dev.twitter.com/ with your Twitter
account and browser to 'My Applications'. Now click 'Create New App' and
complete the form. Once the application is created you will need to generate
your access token from the API tab. You will have the necessary API Key, API
Secret, Access Token and Access Secret necessary to continue.

The command line
----------------

All sample applications will fetch the necessary API and access tokens from the
current environment. The environment variables are ``API_KEY``,
``API_SECRET``, ``ACCESS_TOKEN`` and ``ACCESS_SECRET``. Alternatively the API
and access tokens can be passed using command line arguments.

Each application accepts 3 sub-commands, ``timeline``, ``mentions`` and
``retweets``. Each of these selects a different timeline for the authenticated
user and prints the last 20 tweets from it.

The program
-------------
install the requirements from the requirements.txt file
Run the tw_docopt file


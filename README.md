#h1 Lol vs Lol (Leauge of legends)
This project uses champion.gg api to create to fetch information of either the win-rates of certain Leauge of Legends role, or stats for a matchup for a certain champion in a certain role.

### To do list:
*  Create a concurrent running thread which will periodically gets the win-rates stats for each role and stores that data in a database.  So that when requests for win-rates in role a coming, you read from a database instead of waiting for a response from the api.

*  Automatic handle patch updates and champion switching roles, i.e update id.py

# Installation
Install dependencies into virtualenv:
    pip3 install -r requirements.txt

## Setup
*  You need to setup a local key.py file, which will contain a variable named 'key' which stores your unique api key as a string.

*  Now you run the flask server by:
    source flask/bin/activate
    flask run
    
# Usage
Screen dumps:
![Index](./resources/index_dump.jpg)

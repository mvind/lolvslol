This project uses champion.gg api to create to basic api request for either winrate of certian Leauge of Legends role, or a matchup for a certain champion in a certain role
### To do list:
*  Create a concurrent running thread which will periodicly get winrate stats for each store data in a database,  so that when requests for winrates in role a coming, you eliminate having to do 50 get requests.

*  Automatic handle patch updates and champion switching roles, i.e update id.py

# Installation
Install dependcies into virtualenv:
    pip3 install -r requirements.txt

## Setup
You need to setup a local key.py file, which will contain a variable named 'key' which stores your unique api key as a string.

# Usage
Screen dumps:
![Index](./resources/index_dump.jpg)

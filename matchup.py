import requests, json, id
from key import api_key

base_urL = 'http://api.champion.gg/champion?'
#/champions/:id/:role/matchups
match_url = 'http://api.champion.gg/v2/champions/'

# r = requests.get(url)
# url2 = 'http://api.champion.gg/champion/draven?api_key='+api_key
# print(api_key)
#
# r2 = requests.get(url2)
#
# print(r2.json())
# #print(r.json())
# #/champion/:name?api_key=<API_KEY>


def convert(d):
    '''convert name into id or id into name

    Args:
        d: type either int or str
    returns:
        id = 13
        name = 'Annie'
    '''
    #res = {'status': None, 'value': None}

    if type(d) == int:
        for c in id.li:
            if c['id'] == d:
                return str(c['name'])
        return 'No ID match', 0
    elif type(d) == str:
        for c in id.li:
            if c['name'] == d:
                return str(c['id'])
        return 'No name match', 0
    else:
        return 'Nothing found', 0


test_data = {'Name': 'Draven', 'Roles': 'DUO_CARRY'}

def matchup(res):
    '''return matchup data from  user response

    Args:
        res: {'Name': ['Draven'], 'Roles': ['adc']}

    returns: whatever
    '''
    url = match_url + str(convert(res['Name'])) + '/' + str(res['Roles']) + '/matchups?api_key=' + api_key
    r = requests.get(url)
    r = r.json()
    return r

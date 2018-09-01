import requests, json, id
from key import api_key

base_urL = 'http://api.champion.gg/champion?'


# r = requests.get(url)
# url2 = 'http://api.champion.gg/champion/draven?api_key='+api_key
# print(api_key)
#
# r2 = requests.get(url2)
#
# print(r2.json())
# #print(r.json())
# #/champion/:name?api_key=<API_KEY>

test_data = {'Name': ['Draven'], 'Roles': ['adc']}

def matchup(res):
    '''return matchup data from  user response

    Args:
        res: {'Name': ['Draven'], 'Roles': ['adc']}

    returns: whatever
    '''


def getChampId(name):
    '''return champion Id from champ name

    Args:
        name: 'Draven'
    returns:
        champId = '13'
        or none found = 0

    '''
    for c in id.li:
        print(c)
        if c['name'] == name:
            return c['id']
    return 0

print(getChampId('Draven'))

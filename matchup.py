import requests, json, id
from key import api_key

base_urL = 'http://api.champion.gg/champion?'
#/champions/:id/:role/matchups
match_url = 'http://api.champion.gg/v2/champions/'

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

#
# def parse(s):
#     r = ''
#     for matchup in s:
#         id = matchup['_id']
#         print(convert(id['champ1_id']), 'vs.', convert(id['champ2_id']))
#



test_data = {'Name': 'Draven', 'Roles': 'DUO_CARRY'}

def role_winrate(role):
    '''
        args:
            role: string i.e 'TOP'
        returns:
            winrate of all champs played in given role

    '''
    champDB = id.li2
    idlist = []
    # First we create a idlist of champions which play in the args role
    for champ in champDB:
        for r in champ['role']:
            if r == str(role):
                idlist.append([champ['id'], champ['name']])
                break # Early break because roles are unique

    # Now request winrate for each id in list and
    counter = 0
    for i in idlist:
        r = requests.get('http://api.champion.gg/v2/champions/'+str(i[0])+'?api_key=0a4d02ca842ecb20033591ba4987a34d')
        data = r.json()

        for entry in data: # champions can be played in more than one role
            if entry['_id']['role'] == str(role):
                idlist[counter].append(str(entry['winRate'])[:5]) # Shorten the winrate int to 3 digits
                counter += 1

    # Now we sort the list by winrate in descending order
    resObj = sorted(idlist, key= lambda champ: champ[2], reverse=True)
    return resObj

import requests, json, id
from key import api_key
from operator import itemgetter

base_urL = 'http://api.champion.gg/champion?'
#/champions/:id/:role/matchups
match_url = 'http://api.champion.gg/v2/champions/'
matchup_url = 'http://api.champion.gg/v2/champions/1/MIDDLE/matchups?'

test_data = {'Name': 'Draven', 'Roles': 'DUO_CARRY'}

def nameToId(name: str):
    for i in id.li:
        if i['name'] == name:
            return i['id']

def idToName(champ_id: int):
    for i in id.li:
        if i['id'] == champ_id:
            return i['name']

def role_matchups(res):
    """
    Gets role matchup data from api
        args:

    """
    return_list = []
    name = res['Name']
    role = res['Roles']
    champ_id = nameToId(name)

    url = 'http://api.champion.gg/v2/champions/' + str(champ_id) + '/' + str(role) + '/matchups?limit=200&api_key=' + api_key
    response = requests.get(url)
    data = response.json()

    if data == []:
        return 404

    temp_list = []
    # request format is a list containing dictonaries with json formatted match data
    for res_dict in data: # Loop over each dict and extract values needed
        # Only used for meta data like what champs is in the match up
        champ = res_dict['champ1']

        # Get values
        opponent1_id = res_dict['_id']['champ1_id']
        opponent2_id = res_dict['_id']['champ2_id']

        matchup_id = int
        pointer = 0 # points to which dict contains the champ requested by the user
        relevant = False

        if opponent1_id == champ_id:
            matchup_id = opponent2_id
            pointer = 1
        elif opponent2_id == champ_id:
            matchup_id = opponent1_id
            pointer = 2

        # We filter out matchups vs. opponents not playing the user specified role
        for i in id.li2:
            if i['id'] == matchup_id and role in i['role']:
                relevant = True
                break

        if not relevant:
            continue

        # Use pointer to get the correct dictonary for information
        userChamp = res_dict['champ' + str(pointer)]

        # Extract
        matchup_name = idToName(matchup_id)
        winrate = userChamp['winrate']
        deaths = userChamp['deaths']
        assists = userChamp['assists']
        kills = userChamp['kills']

        # format decimal places
        n = 4 # n-1 number digits after decimal point

        li = [winrate, deaths, assists ,kills]
        li = ['{0:.{1}}'.format(float(el),n) for el in li]

        # Just store the data in a temporary list
        temp_list.append([matchup_name] + li)

    # Now we clean up the data and format it into a return dictonary
    ################################################################

    # Remove entries with a winrate == 1
    for i, val in enumerate(temp_list):
        if val[1] == 1 or val[1] == 0:
            temp_list.pop(i)

    # Now we sort the list by winrate
    sorted_temp_list = sorted(temp_list, key=itemgetter(1), reverse=True)

    for element in sorted_temp_list:
        data_entry = {
            'opponent_name': element[0],
            'winrate': element[1],
            'deaths': element[2],
            'assists': element[3],
            'kills': element[4]
        }
        return_list.append(data_entry)

    return return_list

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

    # Now request winrate for each id in list
    counter = 0
    for i in idlist:
        r = requests.get('http://api.champion.gg/v2/champions/'+str(i[0])+'?api_key='+api_key)
        data = r.json()

        for entry in data: # champions can be played in more than one role
            if entry['_id']['role'] == str(role):
                idlist[counter].append(str(entry['winRate'])[:5]) # Shorten the winrate int to 3 digits
                counter += 1

    # Now we sort the list by winrate in descending order
    print(idlist, str(counter), str(len(idlist)))
    resObj = sorted(idlist, key= lambda champ: champ[2], reverse=True) # Causes bug when role is jungle????
    return resObj

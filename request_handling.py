import requests
key = "RGAPI-6dee6018-3914-471c-855f-71eede6a7c56"


def getID(summoner_name):
    url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + \
          "?api_key=" + key
    r = requests.get(url=url)
    data = r.json()
    accountID = data["accountId"]
    return accountID

class request_handler:
    def __init__(self,data):
        self.data = data

class request_handler_dynamic(request_handler):
    def __init__(self,req_type,summoner_name):
        if req_type == "summonerID":
            self.data = getID(summoner_name)

    def getID(summoner_name):
        url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + \
              "?api_key=" + key
        r = requests.get(url=url)
        data = r.json()
        accountID = data["accountId"]
        return accountID

    def getMatchHistory(summonerID):
        url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summonerID + \
              "?api_key=" + key
        r = requests.get(url=url)
        data = r.json()
        return data
    
    def get_gameID(summonerID):
        gameId_list = []
        match_history = request_handler_dynamic.getMatchHistory(summonerID)
        for match in match_history['matches']:
            gameId_list.append(match['gameId'])
        return gameId_list

    def get_Match(gameID):
        url = "https://euw1.api.riotgames.com/lol/match/v4/matches/"+ str(gameID) + \
            "?api_key="+ key
        r = requests.get(url=url)
        data = r.json()
        return data



class request_handler_static(request_handler):
    def getChampinfo():
        url = "http://ddragon.leagueoflegends.com/cdn/10.3.1/data/en_US/champion.json"
        r = requests.get(url=url)
        data = r.json()
        return data['data']

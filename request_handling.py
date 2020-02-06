import requests
key = "RGAPI-0bee46db-cc6c-425c-9577-ac0b49665436"


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
class request_handler_static(request_handler):
    def getChampinfo():
        url = "http://ddragon.leagueoflegends.com/cdn/10.2.1/data/en_US/champion.json"
        r = requests.get(url=url)
        data = r.json()
        return data['data']

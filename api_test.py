import requests

url = "http://ddragon.leagueoflegends.com/cdn/10.2.1/data/en_US/champion.json"
key = "RGAPI-0df6636e-54fa-44e7-a164-d8a23c19c42e"

r = requests.get(url=url)
data = r.json()
# accountID = data["accountId"]



def getID(summonerName,key):
    url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName+\
          "?api_key=" + key
    r = requests.get(url=url)
    data = r.json()
    accountID = data["accountId"]
    return accountID

def getChampion(championID):
    url = ""

def getMatchHistory(summonerID,key):
    url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+summonerID+\
          "?api_key="+ key
    r = requests.get(url= url)
    data = r.json()
    return data

print(data)

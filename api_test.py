from request_handling import request_handler_dynamic
from request_handling import request_handler_static



summonerID = request_handler_dynamic.getID("Eryuna")
match_history = request_handler_dynamic.getMatchHistory(summonerID)



def getChampion(championID):
    url = ""




#Logic for getting champ name from the static API
champ_id = match_history['matches'][0]['champion']
champ_id = str(champ_id)
print(champ_id)
champs = request_handler_static.getChampinfo()

for champ in champs:
    if champs[champ]['key'] == champ_id:
        print(champs[champ]['name'])

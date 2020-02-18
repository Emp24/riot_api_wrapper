from request_handling import request_handler_dynamic as request


SummonerID = request.getID("Eryuna")
Match_History = request.getMatchHistory(SummonerID)

gameIDs = request.get_gameID(SummonerID)

# Match = request.get_Match(gameID)
match_list = []

for i in range(10):
    match_list.append(request.get_Match(gameIDs[i]))
    # print(match_list[i]['gameId'])


print(match_list[0]['participants'])
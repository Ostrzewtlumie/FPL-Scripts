import requests
import time

def get_json_key_present(json, key):
    try:
        value = json[key]
    except KeyError:
        return
    return value

start_time = time.time()
id = input("Provide your FPL ID: ")
player_map = {}

fpl_data = get_json_key_present(requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json(), 'elements')

print("Loading...")

for x in range(1, 39):
	players = get_json_key_present(requests.get('https://fantasy.premierleague.com/api/entry/' + id + '/event/' + str(x) + '/picks/').json(), 'picks')
	if players == None:
		continue
	
	for i, player in enumerate(players):
		if player['multiplier'] == 0:
			continue
		player_id = str(player['element'])	
		player_history = get_json_key_present(requests.get('https://fantasy.premierleague.com/api/element-summary/' + player_id + '/').json(), 'history')
		for i, player_history_x in enumerate(player_history):
			if player_history_x['round'] != x:
				continue;
			player_name = ""
			for i, player_data in enumerate(fpl_data):
				if str(player_data['id']) == player_id:
					player_name = player_data['second_name']
			if player_name not in player_map:
				player_map[player_name] = 0
			player_map[player_name] = player_map[player_name] + player_history_x['yellow_cards']
			
print(player_map)
print("--- %s seconds ---" % (time.time() - start_time))			
	
import requests
import sys
from matplotlib import pyplot as plt

import matplotlib.ticker as ticker
from enum import Enum

class Options(Enum):
    OVERALL_RANK = ('overall_rank', 'Overall rank')
    RANK = ('rank', 'Gameweek rank')
    POINTS = ('points', 'Gameweek points')
    TOTAL_POINTS = ('total_points', 'Total points')

    def __init__(self, command, desc):
        self.command = command
        self.desc = desc

def plot_diagram(command):

	figure = plt.figure()
	data = []
	oponent_data = []
	number_of_events = []
	for i, event in enumerate(fpl_data['current']):
		number_of_events.append(event['event'])
		data.append(event[command])
		
	for i, event in enumerate(oponent_fpl_data['current']):
		oponent_data.append(event[command])
	
	ax = figure.add_subplot(1, 1, 1)
	ax.plot(number_of_events, data, marker='o', label = 'Your data')
	ax.plot(number_of_events, oponent_data, marker='o', label = 'Oponent data')

	add_legend(ax, command)
	for i,j in zip(number_of_events, data):
		ax.annotate(str(j),xy=(i+0.1,j-2))
	for i,j in zip(number_of_events, oponent_data):
		ax.annotate(str(j),xy=(i+0.1,j-2))
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())

	plt.show()


def set_y_label(command):
	for option in Options:
		if option.command == command:
			return option.desc
	return ""


def add_legend(ax, command):
	y_label = set_y_label(command)
	
	ax.set_xlabel("GW Number")
	ax.set_ylabel(y_label)
	ax.set_title(y_label + " data set. ")
	for axis in [ax.xaxis, ax.yaxis]:
		axis.set_major_locator(ticker.MaxNLocator(integer=True))
	ax.legend()


id = input("Enter your FPL id: ")
oponent_id = input("Enter your oponent FPL id: ")

fpl_data = requests.get('https://fantasy.premierleague.com/api/entry/' + id +'/history/').json()
oponent_fpl_data = requests.get('https://fantasy.premierleague.com/api/entry/' + oponent_id +'/history/').json()

plot_diagram('rank')
plot_diagram('overall_rank')
plot_diagram('points')
plot_diagram('total_points')


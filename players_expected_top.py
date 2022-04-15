from selenium import webdriver
import functools
#playersData.sort((a, b) => (parseFloat(a.xG) + parseFloat(a.xA)) - (parseFloat(b.xG) + parseFloat(b.xA)))
def compare( item1, item2 ) :
	expectedItem1 = float(item1["xG"]) + float(item1["xA"])
	expectedItem2 = float(item2["xG"]) + float(item2["xA"])

	if expectedItem1 > expectedItem2 :
		return -1
	elif expectedItem1 == expectedItem2 :
		return 0
	else:
		return 1
	
	
def check_inputs(begin, end) :
	if begin > end :
		print("End number can not be bigger than begin number.")
		exit()
	if begin < 1 :
		print("Begin number need to be bigger or equal than 1.")
		exit()	


def print_data(begin, end, data) :
	print("TOP {}-{} by expected returns:\n".format(begin, end))
	for player in data[begin-1:end]:
		xG = format(float(player["xG"]),".2f")
		xA = format(float(player["xA"]),".2f")
		name = player["player_name"]
		print("Name: {}, xG: {}, xA: {}, Goals: {}, Assists: {}\n"
		.format(name, xG, xA, player["goals"], player["assists"]))


begin = input("Enter the number of begin: ")
end = input("Enter the number of end: ")
begin = int(begin)
end = int(end)
check_inputs(begin, end)

driver = webdriver.Firefox()
URL = ("https://understat.com/league/EPL/2021")
driver.get(URL)
data = driver.execute_script("return window.playersData;")

if end > len(data)-1 :
	print("End number need to be lower than number of players in Premier League: {}".format(len(data)))
	exit()
	
sortedData = sorted( data, key=functools.cmp_to_key(compare) )
print_data(begin, end, sortedData)
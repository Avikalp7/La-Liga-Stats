import requests
from bs4 import BeautifulSoup
import time


def is_number(s):
    """
    Check and parse entered value as a number
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def connect(fname, url_to_scrape):
	try:
		r = requests.get(url_to_scrape) 
		soup = BeautifulSoup(r.text, "html.parser")
		with open(fname, "w") as text_file:
			text_file.write("{}".format(soup))
		with open(fname) as f:
			content = f.readlines()
		return content
	except Exception:
		print "ConnectionError"
		print "Retrying...."
		connect()


def get_top_three_scorers(content):
	"""
	Prints the top three goal scorers in current La Liga season.
	"""

	print "----------------"
	print "Top Goalscorers"
	print "----------------"
	index = 2000
	top_goalscorers_index = 0

	for line in content[2000:3000]:
		if line.find("<h3><span class=\"mw-headline\" id=\"Top_goalscorers\">Top goalscorers</span></h3>") != -1:
			top_goalscorers_index = index
			break
		index += 1

	podium = [" top ", " second highest ", " third highest "]
	number_found = 0

	for line in content[top_goalscorers_index:]:
		if number_found >= 3:
			break
		if line.find("Cristiano Ronaldo") != -1:
			print "Cristiano Ronaldo is the" + podium[number_found] + "goalscorer."
			goal_line = content[index + 2]
			goals = find_goals(goal_line)
			print "Goals : " + str(goals)
			number_found += 1
		elif line.find("Luis S") != -1 and line.find("Uruguay") != -1:
			print "Luis Suarez is the" + podium[number_found] + "goalscorer."
			goal_line = content[index + 2]
			goals = find_goals(goal_line)
			print "Goals : " + str(goals)
			number_found += 1
		elif line.find("Lionel Messi") != -1:
			print "Lionel Messi is the" + podium[number_found] + "goalscorer."
			goal_line = content[index + 2]
			goals = find_goals(goal_line)
			print "Goals : " + str(goals)
			number_found += 1
		elif line.find("Karim Benzema") != -1:
			print "Karim Benzema is the" + podium[number_found] + "goalscorer."
			goal_line = content[index + 2]
			goals = find_goals(goal_line)
			print "Goals : " + str(goals)
			number_found += 1
		elif line.find("Gareth Bale") != -1:
			print "Gareth Bale is the" + podium[number_found] + "goalscorer."
			goal_line = content[index + 2]
			goals = find_goals(goal_line)
			print "Goals : " + str(goals)
			number_found += 1
		elif line.find("Neymar") != -1:
			print "Neymar is the" + podium[number_found] + "goalscorer."
			goal_line = content[index + 2]
			goals = find_goals(goal_line)
			print "Goals : " + str(goals)
			number_found += 1
		index += 1


def get_top_three_assists(content):
	print ""
	print "-------------"
	print "Top Assists"
	print "-------------"
	podium = [" top ", " second highest ", " third highest "]
	index = 2000
	number_found = 0
	
	while  number_found < 3:
		index = 2000
		for line in content[2000:]:
			if line.find("Top assists") != -1:
				assist_line = index
				break
			index += 1

		for line in content[assist_line:]:
			if line.find("<td>" + str(number_found + 1) + "</td>") != -1:
				name_line = content[index + 1]
				end_index = name_line.find("</a></td>")
				start_index = end_index
				while name_line[start_index - 1] != ">":
					start_index -= 1
				name = name_line[start_index : end_index]
				print name + " is the" + podium[number_found] + "assist provider."
				assists = find_goals(content[index + 3])
				print "Assists : " + str(assists)
				number_found += 1
				break
			index += 1


def find_goals(line):
	goal_str = ""
	for char in line:
		if is_number(char):
			goal_str += char
	return goal_str




if __name__ == "__main__":
	content = connect("score.txt", 'https://en.wikipedia.org/wiki/2015-16_La_Liga#Top_goalscorers')
	get_top_three_scorers(content)
	get_top_three_assists(content)
	key = raw_input("Press Enter to Exit")

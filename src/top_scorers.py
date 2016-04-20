import requests
from bs4 import BeautifulSoup
import time

url_to_scrape = 'https://en.wikipedia.org/wiki/2015-16_La_Liga#Top_goalscorers'
fname = "score.txt"

def is_number(s):
    """
    Check and parse entered value as a number
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_top_three_scorers():
	"""
	Prints the top three goal scorers in current La Liga season.
	"""
	try:
		r = requests.get(url_to_scrape) 
		soup = BeautifulSoup(r.text, "html.parser")
		with open(fname, "w") as text_file:
			text_file.write("{}".format(soup))
		with open(fname) as f:
			content = f.readlines()

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

	except Exception:
		print "ConnectionError"
		print "Retrying...."
		get_top_three_scorers()

def find_goals(line):
	goal_str = ""
	for char in line:
		if is_number(char):
			goal_str += char
	return goal_str

get_top_three_scorers()
key = raw_input("Press Enter to Exit")

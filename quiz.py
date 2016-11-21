#encoding=utf-8
# :=:> module imports
import sys, os, time, random
from colorama import init, Fore, Back, Style
from termcolor import colored

#termcolor 
init(autoreset=True)
# name, time, and level selection
print (Fore.YELLOW + "\n" * 3 + "Program initialized: " + time.ctime() + "  " + '...' + ("\n" * 3))
print (Fore.CYAN + "Ahem, Hi!")
#.   user input field
user_name = raw_input(Fore.CYAN + "\n\nWhat is your name?\n\n\n")
if len(user_name) == 0:
	user_name = raw_input("\n\n\nWhat is your name? \n\nAnswer must be a string of at least 1 character" )

print (Fore.CYAN + '\n' * 2 + 'Hi ' + user_name + "!!" + '\n' * 2 )
# user input field 
level = raw_input(Fore.GREEN + "\nChoose level of difficulty:" + Fore.RESET + Fore.MAGENTA + "\n--a, easiest to c, most difficult\n\t If you need extra information type \'help\' ")
if level == 'help' or level == 'Help':
	print (Fore.GREEN + "(a) -- Quiz that can only end if a 100% score. Question repeats until correct answer is provided.\n")
	print (Fore.YELLOW + "(b) -- Quiz that allows two wrong attempts. If user leaves 2nd attempt blank there is no penalty for incorrect answer.\n")
	print (Fore.RED + "(c) -- Quiz which subtracts 1 point for each wrong response. No second attempts allowed.\n")
	level = raw_input(Fore.GREEN + "\nChoose level of difficulty:" + Fore.RESET + Fore.MAGENTA + "\n--a, easiest to c, most difficult\n\t If you need extra information type \'help\' ")


quiz_data = [


          ("What type of element must begin with __DEF__?", "function"),
          #
          ("A ___?___ must be encapsulated between quotes", "string"),
          #
          ("What method returns a scalar value of the # of expressions within any given element?", "len()"),
          #
          ("whats the fewest amount of parameters a function must hold to do work?", "0"),
              #
          ("an if statement can be comprised of \'if\', \'elif\', and what other keyword?",'else'),
          #
          ("If one invoked the .find() method on a string what value would result from a non-find?","-1"),
          #
          ("The opposite of False?", "True"),
          #
          ("If two terms were evaluated for truthiness one being True the other False, \'AND\' connects the two booleans", "False"),#
          #
          ("When functions are actually called parameters become?",'arguments'),
          #
          ("How many arguments should be used with the following function\ndef random(pocket, dot): .. \t \t?", "2"),#
          #
          ("Given the list = [\"Foxboro\", \"Attleboro\", \"Memphis\"], list[1] returns ?",'<Attleboro></Attleboro>'),
          #
          ("(Boolean) Would the following be an infinite loop?: \n \quote = \'sun rises in the east\'\nwhile quote == \'Sun rises in the east.\'", "False"),
          #
          ("For int in range(3) returns?","0 1 2"),
          #
          ("How many elements will be returned from the generic procedure : len(len(len(len(len(len(...))))))","1"),
          #
          ("Is True and False true?","False")


                 ]
  #2. Create positive response pool for correct answers
yays = [
		'Yay!', 'Correct!', 'You\'re Amazing!', '+1!', \
    	'How did you know!?', 'We got a genius here!', \
     	'PERFECTO!', 'Udacity did you well!']
def randYay():
  rY = random.randint(0, 7)
  return yays[rY]


#3 And the nays
nays = [
			'Nope!', 'Try Again!', 'Loser!', 'Go home, wrong!', '-1!', \
		    'Try one more time', 'You got this! ...incorrect', 'Study!']
def randNay():
  rN = random.randint(0, 7)
  return nays[rN]

#4 finally, determine what functions should be prepared for the evaluation
high_level = 'Wow! Congrats! You are well on your way to programming great structures, apps, and apis. Good word! '
med_level =  'You surely are on the way to the top. Please focus more on crucial details that will prevent your code from being as great as it could be. Try harder!'
low_level = 'Do not pass go, do not collect $200, go study'

def evaluate_score(score):
	if score <= 11:
		print high_level
	elif 7 < score < 10: 
		print med_level
	else: 
		print low_level
'''
'''
def hard_logic():
	index = 0
	score = 0

	if userResponse == trueAnswer or userResponse.lower() == trueAnswer:
		print '\n\n\n\t' + randYay() + '\n\n\n'
		score = score + 1
		index = index + 1
	else: 
		print randNay()
		score = score - 1
		index = index + 1
	return score
	return index
	print score 
def medium_logic():
	index = 0
	score = 0
	for p in range(2):
		if userResponse != trueAnswer and userResponse != "": 
			print 'Try one more time! (If wrong again -1 score!)'
			print 'To avoid -1 score, leave answer blank'
		elif p == 2 and userResponse  == "":
			index = index + 1
		elif p == 2 and userResponse != "":
			index = index + 1
			print randNay()
			score = score - 1
	if userResponse == trueAnswer:
		score = score + 1
		index = index + 1
		print randYay()
	return score
	return index
	print score 
def easy_logic():
	index, score = 0
	while userResponse != trueAnswer:
		userResponse = raw_input(question)
	if userResponse == trueAnswer:
		print randYay()
		score = score + 1 
	 	index = index + 1
	return score
	return inde
	print score 

for question, trueAnswer in quiz_data:
		userResponse = raw_input(question)
		if level == 'a':
			easy_logic()
		elif level == 'b':
			medium_logic()
		else:
			hard_logic()

	evaluate_score(score)

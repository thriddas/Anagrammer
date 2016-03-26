import csv
import os
import time
import random
from collections import defaultdict 
import sys

def readFile (fileName) : 
	with open(fileName) as file:
		dataDump = file.readlines()

		tempDictWords = {}

	for line in dataDump:
		splitLine = line.split('\t')
		tempDictWords[splitLine[0]] = splitLine[1]

	return tempDictWords

path = os.path.abspath(os.path.dirname(sys.argv[0]))
os.system('cls')

print """
Greetings! And Welcome to the Anagrammer. 
You may choose to do one of the following word lists
	1. Threes 
	2. Fours
	3. Fives 
	4. 7s - Type 1 (easy)
	5. 8s - Type 1 (easy)
	6. 7s - Type 2 (medium)
	7. 8s - Type 2 (medium)
	8. 7s - Type 3 (hard)
	9. 8s - Type 3 (hard)
	10. Vowel Heavy words

	So pick a number!
"""
fileList = {
	'1' : 'threes.txt',
	'2' : 'fours.txt',
	'3' : 'fives.txt',
	'4' : 'type 1 7s.txt',
	'5' : 'type 1 8s.txt',
	'6' : 'type 2 7s.txt',
	'7' : 'type 2 8s.txt',
	'8' : 'type 3 7s.txt',
	'9' : 'type 3 8s.txt',
	'10' : 'vowelHeavy.txt'}

option = raw_input('>')
validOption = False

while not validOption:
	if option in fileList:
		validOption = True
		fileName = path+"\\words\\"+fileList[option]
	else:
		print "Please pick a reasonable input"
		option = raw_input('>')

dictWords = readFile(fileName)

questionAnswer = defaultdict(list)

for word in dictWords.iterkeys():
	questionAnswer[''.join(sorted(list(word)))].append(word)

while(len(questionAnswer) > 0) : 
	os.system('cls')
	upper = len(questionAnswer)
	enumerator = random.randint(1, upper)
	question = questionAnswer.keys()[enumerator] 
	print "\n\nAnagram %s" %(question)
	print "There are %s anagrams" %(len(questionAnswer[question]))
	print "Instead of answering, you may also\n\t1 - Shuffle\n\t2 - Answers\n\t3 - Clue\n\t4 - Quit"
	unAnswered = True
	clue = 1
	while unAnswered :
		answer = raw_input('\n\t>').upper()
		if answer == "1":
			print "\t\t", ''.join(random.sample(question,len(question)))
		elif answer == "2":
			print " ".join(questionAnswer[question])
			for word in questionAnswer[question]:
				print "\t", word, " - ", dictWords[word]
			unAnswered = False
			time.sleep(2)
		elif answer == "3":
			print "\t\t", questionAnswer[question][0][:clue]
			clue = clue + 1
			if clue >= len(question):
				print "\t\t\tReally? You still don't have an answer?"
		elif answer == "4":
			exit()		
		else:
			if answer in questionAnswer[question]:
				print "\t\tCorrect"
				print "\t\t%s" %dictWords[answer]
				questionAnswer[question].remove(answer)
				left = len(questionAnswer[question])
				print "There are %s anagrams left" %left
				clue = 1 
				if left == 0:
					unAnswered = False
					time.sleep(2)
			else:
				print "\t\tNope"
	questionAnswer.pop(questionAnswer.keys()[enumerator])


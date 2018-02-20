from nltk.tag import pos_tag
import re
import sys

'''
A text-processing tool that will read through a given text file, process its contents, and
output your findings in text format.

Input:
	The file name to a text file.
	eg: python text_engine.py text.txt

Output:
	Five lines of output for each given article.
	First line -> number of occurrences of 'a'.
	Second line -> number of occurrences of 'an'.
	Third Line -> number of occurrences of 'the'.
	Fourth Line -> number of occurrences of date information.
	Fifth Line -> number of occurrences of proper nouns
	
	eg:
		number of occurrences of 'a': 0
        number of occurrences of 'an': 2
        number of occurrences of 'the': 2
        number of occurrences of dates: 4
        number of occurrences of proper nouns: 8
'''
# Class for text processing
class nlp:
	def __init__(self, filename):
		# Reads the contents of text file stores it in data variable
		with open(filename, 'r') as myfile:
			self.data=myfile.read().replace('\n', '')

	def get_data(self):
		# Returns text data as string
		return self.data

	def get_propernouns(self):
		# Using nltk tagging find out the pronouns in data. Returns length
		# of pronouns
		tagged_sent = pos_tag(self.data.split())
		propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
		return len(propernouns)

	def get_dates(self):
		# using regex find out dates in data. Return length of dates
		dates_with_numbers = re.findall(r'\d+\S\d+\S\d+', self.data)
		dates_with_text = re.findall(r'[A-Z]\w+\s\d+', self.data)
		return len(dates_with_numbers) + len(dates_with_text)

	def get_articles(self):
		# finds out the frequency of 'a' 'an' and 'the'
		# Returns dict of lengths
		tokens = pos_tag(self.data.split())
		articles = [word for word,pos in tokens if pos == 'DT']
		a_len = articles.count('a')
		an_len = articles.count('an')
		the_len = articles.count('the')
		return {'a': a_len, 'an': an_len, 'the': the_len}

	def __str__(self):
		#function for printing the final output as string
		articles = self.get_articles()
		propernouns = self.get_propernouns()
		dates = self.get_dates()
		return_string = '''		number of occurrences of 'a': {} \n \
		number of occurrences of 'an': {} \n \
		number of occurrences of 'the': {} \n \
		number of occurrences of dates: {} \n \
		number of occurrences of proper nouns: {} \n'''
		return return_string.format(articles['a'], articles['an'], articles['the'], dates, propernouns)

filename = sys.argv[1]
text = nlp(filename)
print(text)

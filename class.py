
# A Word Smerger: 

def reverse_a_word(the_word): # global recursive function
	if len(the_word) == 1:
		return the_word[0]
	return the_word[-1] + reverse_a_word(the_word[:-1])

class BasicWordSmerger: # super class that reverses the word
	def __init__(self, word):
		self.word = word

	def reverse_me(self):
		self.word = reverse_a_word(self.word)

class AdvancedWordSmerger(BasicWordSmerger): # sub class that adds additional functionality, extra "o" and reverse
	def __init__(self, word, extension):
		super().__init__(word)
		self.extension = extension

	def extend_o(self):
		self.word = self.word.replace("o", "o" * self.extension)

	def reverse_me(self):
		self.word = "sophie"
		super().reverse_me()

	def extend_o_and_reverse(self):
		self.reverse_me()
		self.extend_o()

bas_word_smerger = BasicWordSmerger("sophie") # an instance of the class BasicWordSmerger
bas_word_smerger.reverse_me() # accessing a class function from the instance
print(bas_word_smerger.word)

adv_word_smerger = AdvancedWordSmerger("sophie", 7) # an instance of the class AdvancedWordSmerger
adv_word_smerger.extend_o_and_reverse() # accessing a class function from the instance
print(adv_word_smerger.word)

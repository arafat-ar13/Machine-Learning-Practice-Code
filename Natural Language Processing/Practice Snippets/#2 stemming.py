from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Creating a stem object
ps = PorterStemmer()

# Example words to use
example_words = ["python", "pythoning", "pythoned", "pythoner", "pythonly"]
# Stemming the words
stemmed_words = [ps.stem(word) for word in example_words]

# Let's take a look at a sentence and stem that down
example_sentence = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once"

# First we will tokenize the sentence
tokenized = word_tokenize(example_sentence)
# Then stem it
stemmed = [ps.stem(word) for word in tokenized]

print(stemmed_words)
print(stemmed)
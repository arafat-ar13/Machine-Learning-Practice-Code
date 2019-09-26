# Very first machine learning program
from nltk.tokenize import word_tokenize, sent_tokenize

text = "This is a very beautiful day to go out and go places, such as Saint St. in Louisville. We do not know when the weather will go bad. So have fun kids!"

# Words and sentence in the text above
sentences = sent_tokenize(text)
words = word_tokenize(text)

print(sentences)
print(words)
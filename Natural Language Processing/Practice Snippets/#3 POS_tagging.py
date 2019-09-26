from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from lyrics_data import false_god, senorita

song1 = false_god

# First step, tokenize
tokenized = word_tokenize(song1)

lemmatize = WordNetLemmatizer()
lemmatized = [lemmatize.lemmatize(word) for word in tokenized]

pos_tagged = pos_tag(lemmatized)

print(pos_tagged)
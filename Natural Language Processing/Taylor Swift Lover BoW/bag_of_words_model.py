from collections import Counter

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

from custom_stopwords import custom_stopwords

song_lyrics = str()
with open(r"lyrics.txt", "r") as file:
    song_lyrics = file.read()


stopwords = stopwords.words('english')

tokenized = word_tokenize(song_lyrics)

lemmatize = WordNetLemmatizer()
lemmatized = [lemmatize.lemmatize(word) for word in tokenized]

words_to_removed = []
for word in lemmatized:
    if word in custom_stopwords or word in [str(num) for num in range(10)] or word in stopwords:
        words_to_removed.append(word)

for word in words_to_removed:
    lemmatized.remove(word)

word_counts = Counter(lemmatized)
print(word_counts)

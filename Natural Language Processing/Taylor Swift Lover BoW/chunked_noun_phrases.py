from nltk import RegexpParser, pos_tag
from nltk.tokenize import word_tokenize

from custom_stopwords import custom_stopwords

with open(r"lyrics.txt", "r") as file:
    data = file.read()

tokenized = word_tokenize(data)
for word in tokenized:
    if word in custom_stopwords or word in [",", "'s"]:
        tokenized.remove(word)

# Starting chunking of Noun Phrases
pos_tagged = pos_tag(tokenized)

def chunk_it_up(cleaned_data):
    chunk_pattern = r"""NP: {<DT>?<JJ>*<NN>}"""
    chunk = RegexpParser(chunk_pattern)
    chunked = chunk.parse(cleaned_data)
    return chunked

print(chunk_it_up(pos_tagged))

from nltk import RegexpParser, pos_tag
from nltk.tokenize import word_tokenize

from lyrics_data import miss_americana, false_god, senorita

songs_data = miss_americana + false_god + senorita

song_tokenized = word_tokenize(songs_data)
pos_tagged = pos_tag(song_tokenized)

def chunk_it_up(tagged_text):
    chunk_pattern = "Chunk: {<DT>?<JJ>*<NN>}"
    chunk_parser = RegexpParser(chunk_pattern)
    chunked = chunk_parser.parse(tagged_text)
    chunked.draw()

chunk_it_up(pos_tagged)
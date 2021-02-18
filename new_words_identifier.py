from get_words_from_db import get_words_from_db
import spacy
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

nlp = spacy.load("de_core_news_sm")


def get_steem_from_verb(word):
    doc = nlp(word)
    for token in doc:
        if token.pos_ == "VERB" or token.pos_ == "AUX":
            return token.lemma_
        return word


def get_clean_words_from_text():
    de_stop_words = set(stopwords.words("german"))

    path = "./input.txt"

    text_file = open(path, "r")
    text = text_file.read()

    punct_remover = RegexpTokenizer(r"\w+")
    de_vocabulary = punct_remover.tokenize(text)
    de_words = {}
    for w in de_vocabulary:
        w_lower = w.lower()
        wd = get_steem_from_verb(w_lower)
        if w_lower not in de_stop_words and wd not in de_words:
            de_words[wd] = w

    return de_words.values()


def get_words_not_in_db(db_words):
    text_words = set(get_clean_words_from_text())
    not_in_db = []

    for word in text_words:
        if word not in db_words:
            not_in_db.append(word)

    return not_in_db

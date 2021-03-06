import os

from gensim.models import Word2Vec, Phrases
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from DataHandler.utils import get_corpus


def train_n_gram(data, n):
    bigram = Phrases(sentences=data)

    if n == 2:
        model = Word2Vec(
            sentences=bigram[data],
            size=100, window=5, min_count=1,
            workers=os.cpu_count()
        )

    else:
        trigram = Phrases(bigram[data])
        model = Word2Vec(
            sentences=trigram[bigram[data]],
            size=100, window=5, min_count=1,
            workers=os.cpu_count()
        )

    return model


def train_tfidf(data):
    """

    Ref - https://radimrehurek.com/gensim/models/tfidfmodel.html
    :param data: data
    :return: trained TF-IDF model
    """
    dct = Dictionary(data)
    corpus = [dct.doc2bow(line) for line in data]
    print(corpus)
    model = TfidfModel(corpus)

    return model


def load_model(path):
    model = Word2Vec.load(path)

    return model


def train_word2vec(data):
    model = Word2Vec(sentences=data,
                     size=100, window=5,
                     min_count=1)

    return model


def transfer_word2vec(trained_model, corpus):
    # Update Vocab
    trained_model.build_vocab(corpus, update=True)

    print("Word2Vec train by using Title data ")
    result = trained_model.train(corpus,
                                 total_examples=trained_model.corpus_count,
                                 epochs=trained_model.epochs)
    print("Complete train")
    return result


if __name__ == '__main__':
    pass
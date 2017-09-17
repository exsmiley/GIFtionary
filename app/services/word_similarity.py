from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity


class WordSimilarityFinder(object):

    def __init__(self):
        self.model = KeyedVectors.load_word2vec_format('model.bin', binary=True)

    def calc_similarity(self, w1, w2):
        """Calculates the similarity between 2 phrases"""
        w1 = w1.split()
        w2 = w2.split()
        a = self.model.wv[w1[0]]
        b = self.model.wv[w2[0]]

        for w in w1[1:]:
            try:
                a += self.model.wv[w]
            except:
                pass
        for w in w2[1:]:
            try:
                b += self.model.wv[w]
            except:
                pass

        a = a/sum(a)
        b = b/sum(b)
        return cosine_similarity([a], [b])[0][0]


if __name__ == '__main__':
    finder = WordSimilarityFinder()
    print(finder.calc_similarity('poop', 'cookie dough'))
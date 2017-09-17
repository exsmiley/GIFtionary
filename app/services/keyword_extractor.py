from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import RAKE
import random

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from giftest import get_gif
from wikitest import *


class KeywordExtractor(object):
    """Wrapper around rake for reuse as library"""

    def  __init__(self):
        self.rake = RAKE.Rake('stop.txt')

    def get_keywords(self, sentence):
        """Gets a key phrase from a sentence"""
        keywords = self.rake.run(sentence)

        # TODO maybe have a scheme to choose more words?
        max_score = keywords[0][1]
        keywords = [tup[0] for tup in keywords if tup[1] == max_score]
        return random.choice(keywords)

    def paragraph_to_sentence(self, para):
        """Use if there are too many paragraphs"""
        LANGUAGE = "english"
        SENTENCES_COUNT = 2
        parser = PlaintextParser.from_string(para, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        return list(summarizer(parser.document, SENTENCES_COUNT))


def get_gifs_from_story(story_text, extractor):
    if story_text.count('.') > 15:
        paragraphs = story_text.split('\n')
        sentences = map(extractor.paragraph_to_sentence, paragraphs)
    else:
        sentences = story_text.split('.')
    kw_list = map(extractor.get_keywords, sentences)
    gif_urls = map(get_gif, kw_list)
    return list(gif_urls)


def get_gifs_wiki(wiki_topic, extractor):
    text = '\n'.join(get_paragraphs_from_wiki(wiki_topic))
    return get_gifs_from_story(text, extractor)


def get_gifs_urban_dictionary(term, extractor):
    text = '\n'.join(get_urban_dictionary(term))
    return get_gifs_from_story(text, extractor)


if __name__ == '__main__':
    text = 'the mouse jumps up and down with the elephant in the sky while eating cookies'
    ke = KeywordExtractor()
    para = "Beep first appeared in the comic strip Doctor Who and the Star Beast, written by Pat Mills and John Wagner and drawn by Dave Gibbons, which ran in issues #19-#26 of Doctor Who Weekly. The Meeps were an advanced and peaceful race, who lived in harmony and happiness until their natures were radically altered by their planet's orbit passing close to the Black Sun. The radiation from the black star mutated them into an aggressive, expansionist species who began to mercilessly conquer and subjugate other planets."

    print(ke.get_keywords(text)) # prints 'mouse jumps' or 'eating cookies'
    print(ke.paragraph_to_sentence(para)) # prints 2nd sentence
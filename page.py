from nltk.corpus import stopwords
from string import punctuation
from pydash import get,pull
import nltk
nltk.download('stopwords')


class WebPage(object):
    def __init__(self, url, description):
        self._url = url
        self._description = description
        self._words = {}
        self._extract_words()

    def __repr__(self):
        return str(self.__dict__)

    @property
    def url(self):
        return self._url

    @property
    def description(self):
        return self._description

    @property
    def words(self):
        return self._words


    @staticmethod
    def is_empty_word(word):
        """
        Can recognize an empty word in english and french
        :param word: un mot
        :return: true if empty word false
        """
        stop_fr = set(stopwords.words('french'))
        stop_en = set(stopwords.words('english'))

        return word.lower() in stop_en or (word.lower() in stop_fr)

    @staticmethod
    def count_number_of_occurence(one_word, list_of_words):
        """
        Count the number of occurence of a word in a given list
        :param one_word:
        :param list_of_words:
        :return: number of occurences
        """
        count = 0
        for w in list_of_words:
            if one_word == w:
                count += 1
        return count

    def _extract_words(self):
        clean_desc = self._description
        for punct in punctuation:
            clean_desc = clean_desc.replace(punct, " ")
        words = clean_desc.split()
        for w in words:
            if w not in self._words:
              if not self.is_empty_word(w): #appel de la fonction empty word
                  if not get(words,w):
                    self._words[w] =  self.count_number_of_occurence(w, words)





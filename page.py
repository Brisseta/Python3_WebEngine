from string import punctuation
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


class WebPage(object):
    def __init__(self, url, description):
        self._url = url
        self._description = description
        self._words = []
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

    def _extract_words(self):
        clean_desc = self._description
        for punct in punctuation:
            clean_desc = clean_desc.replace(punct, " ")
        words = clean_desc.split()
        for w in words:
            if w not in self._words:
              if not self.is_empty_word(w): #appel de la fonction emptyword
                    self._words.append(w.lower())

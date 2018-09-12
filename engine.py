from page import WebPage
from pydash import intersection_with, union_with, get, for_in, order_by, pull, pull_all_with
import pickle
class WebSearchengine(object):
    def __init__(self):
        self._search_count = 0
        self.indexed_urls_list = []
        self.search_dictionary = {}

    @property
    def search_count(self):
        return self.search_count

    def reset_search_count(self):
        self._search_count = 0

    def increment_search_count(self):
        self._search_count += 1

    def increment_search_count_by_nb(self,number):
        self._search_count += number

    def index(self, webpage):
        """

        :param webpage:
        :return:
        """

        def parse_desc(count, word):
            if not get(self.search_dictionary, word):
                self.search_dictionary[word] = []
            self.search_dictionary[word].append({
                'url': webpage.url,
                'count': count
            })

        for_in(webpage.words, parse_desc)
        self.indexed_urls_list.append(webpage.url)
        pickle.dump(self, open("save.p", "wb"))

    def indexed_urls(self):
        """
        Return all indexed urls
        :return: list of urls
        """
        index_lists = self._index.values()
        urls = set()
        for pages in index_lists:
            pages_urls = [p.url for p in pages]
            urls = urls.union(pages_urls)
        return list(self._index.keys())

    def single_search(self, word):
        """
        Return urls of page containing word
        :param words:
        :return:
        """
        self.increment_search_count()
        if word not in self._index:
            return []
        else:
            pages = self._index[word]
            return [p.url for p in pages]

    def multi_search(self, words, and_mode=True):
        """
        Return urls of pages containing words
        :param words:
        :return:
        """
        if len(words) != 0:
            urls_found = set(self.single_search(words[0]))
            for word in words[1:]:
                single_result = self.single_search(word)
                urls_found = urls_found.intersection(single_result) if and_mode else urls_found.union(single_result)
                self.increment_search_count_by_nb(len(urls_found))
            return list(urls_found)
        else:
            return None

    def print_info_page(self, page):
        print("Url de la page %s" % self.index(page).url)
        print("Description de la page %s" % self.index(page).description)
        print("Mots de la page %s " % self.index(page).words)

    def all_urls(self):
        return self.indexed_urls_list

    def removekey(d, key):
        r = dict(d)
        del r[key]
        return r

    def de_index(self, webpage):
        # if webpage.url in self.indexed_urls_list:
        #     self.indexed_urls_list.remove(webpage.url)
        #     words_to_remove = webpage.words
        #     print(words_to_remove)
        #     for w in words_to_remove:

        comparator = lambda a, b: a['url'] == b

        if webpage.url in self.indexed_urls_list:
            pull(self.indexed_urls_list, webpage.url)
            for word in self.search_dictionary:
                pull_all_with(self.search_dictionary[word], [webpage.url], comparator)
            print("Désindexation terminée\n")
        else:
            print("Cet url n'est pas indexé\n")









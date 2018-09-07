class WebSearchengine(object):
    def __init__(self):
        self._index = dict()
        self._search_count = 0

    @property
    def search_count(self):
        return self.search_count

    @property
    def reset_search_count(self):
        self._search_count = 0

    def index(self, webpage):
        """

        :param webpage:
        :return:
        """
        for word in webpage.words:
            if word in self._index:
                pages = self._index[word]
                pages.append(webpage)
            else:
                self._index[word] = [webpage]

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
        if word not in self._index:
            return []
        else:
            pages = self._index[word]
            return [p.url for p in pages]
        # return [p.url for p in self._index[word]] if word in index else []

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
            return list(urls_found)
        else:
            return None

    def print_info_page(self, page):
        print("Url de la page %s" % self.index(page).url)
        print("Description de la page %s" % self.index(page).description)
        print("Mots de la page %s " % self.index(page).words)

    def all_urls(self):
        return self.indexed_urls()

    def de_index(self, url):
        if url in self.indexed_urls():
            self._index.remove()

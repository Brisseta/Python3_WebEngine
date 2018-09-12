from urllib.parse import urlparse
from requests import get
from bs4 import BeautifulSoup
from sys import argv, exit
from page import WebPage
from engine import WebSearchengine


def extract_description(soup_object):
    meta_items = soup_object.find_all('meta', {'property', 'og:description'})
    if len(meta_items) != 0:
        meta_item = meta_items[0]
        if meta_item.has_attr("content"):
            meta_content = meta_item.get("content")
            stripped_content = meta_content.strip()
            if len(stripped_content) != 0:
                return stripped_content
    return None


def download(url):
    url_parsed = urlparse(url)
    if url_parsed.scheme in ["http", "https"] and url_parsed.netloc != '':
        response = get(url)
        soup_object = BeautifulSoup(response.text, 'html.parser')
        description = extract_description(soup_object)
        return description
    return None


if __name__ == '__main__':
    if len(argv) != 2 :
        print("Utilisation du fichier")
        exit(0)

filename = argv[1]
file = open(filename)
for url in file :
    description = download(url)
    if description is not None:
       webPage = WebPage(url, description)
       engine = WebSearchengine(webPage)
       engine.print_info_page(webPage)

    else:
        print("No description foud pour ", url)
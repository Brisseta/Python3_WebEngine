from page import WebPage
from engine import WebSearchengine
page1 = WebPage("https://whippet.telecom-lille.fr/course/search.php?search=projet","this is the whippet help page of IMT lille douai whippet")
page2 = WebPage("http://indexerror.net/4492/initialisation-dun-attribut-par-une-fonction-dans-__init__","page d'aide pour le python")
page3 = WebPage("https://myservices.imt-lille-douai.fr/portail/","page principale de whippet")
engine = WebSearchengine()
engine.index(page1)
engine.index(page2)
engine.index(page3)
retour_single_s = engine.single_search("aide")
print(retour_single_s)
retour_multiple_s = engine.multi_search(["aide","page"], False)
print(retour_multiple_s)
print(engine.all_urls())
print("resultat de la de indexage", engine.de_index(page1))
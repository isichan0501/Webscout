from webscout import WEBS

# Translation of the keyword 'school' to German ('hi') using DuckDuckGo.com
with WEBS() as WEBS:
    keywords = 'school'
    r = WEBS.translate(keywords, to="hi")
    print(r)


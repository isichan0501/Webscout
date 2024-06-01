from webscout import WEBS

# Instant answers for the query "sun" using DuckDuckGo.com 
with WEBS() as WEBS:
    for r in WEBS.answers("sun"):
        print(r)


from webscout import WEBS

# Suggestions for the keyword 'fly' using DuckDuckGo.com
with WEBS() as WEBS:
    for r in WEBS.suggestions("fly"):
        print(r)


from webscout import WEBS

# Image search for the keyword 'butterfly' using DuckDuckGo.com 
with WEBS() as WEBS:
    keywords = 'butterfly'
    WEBS_images_gen = WEBS.images(
      keywords,
      region="wt-wt",
      safesearch="off",
      size=None,
      type_image=None,
      layout=None,
      license_image=None,
      max_results=10,
    )
    for r in WEBS_images_gen:
        print(r)


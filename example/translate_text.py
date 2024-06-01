from webscout import WEBS

def translate_text(keywords, to_language="hi"):
    with WEBS() as WEBS:
        r = WEBS.translate(keywords, to=to_language)
        return r

def main():
    keywords = 'school'
    translated_text = translate_text(keywords, to_language="hi")
    print(translated_text)

if __name__ == "__main__":
    main()

from webscout import WEBS

def get_suggestions(keywords):
    with WEBS() as WEBS:
        suggestions = [r for r in WEBS.suggestions(keywords)]
        return suggestions

def main():
    keywords = 'fly'
    suggestions = get_suggestions(keywords)
    for suggestion in suggestions:
        print(suggestion)

if __name__ == "__main__":
    main()

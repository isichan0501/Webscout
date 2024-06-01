from webscout import WEBS
import datetime

def fetch_news(keywords, timelimit):
    news_list = []
    with WEBS() as webs_instance:
        WEBS_news_gen = webs_instance.news(
            keywords,
            region="wt-wt",
            safesearch="off",
            timelimit=timelimit,
            max_results=20
        )
        for r in WEBS_news_gen:
            # Convert the date to a human-readable format using datetime
            r['date'] = datetime.datetime.fromisoformat(r['date']).strftime('%B %d, %Y')
            news_list.append(r)
    return news_list

def _format_headlines(news_list, max_headlines: int = 100):
    headlines = []
    for idx, news_item in enumerate(news_list):
        if idx >= max_headlines:
            break
        new_headline = f"{idx + 1}. {news_item['title'].strip()} "
        new_headline += f"(URL: {news_item['url'].strip()}) "
        new_headline += f"{news_item['body'].strip()}"
        new_headline += "\n"
        headlines.append(new_headline)

    headlines = "\n".join(headlines)
    return headlines

def main():
    # Example usage
    keywords = 'latest AI news'
    timelimit = 'd'
    news_list = fetch_news(keywords, timelimit)

    # Format and print the headlines
    formatted_headlines = _format_headlines(news_list)
    print(formatted_headlines)

if __name__ == "__main__":
    main()

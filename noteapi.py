import requests

# 話題記事一覧
# notes_response = requests.get('https://note.com/api/v2/notes')
# print(notes_response.json())





import requests
import json


import pandas as pd


def analyze_json_schema(data):
    if isinstance(data, dict):
        return {key: type(value).__name__ for key, value in data.items()}
    elif isinstance(data, list):
        return [analyze_json_schema(item) for item in data]
    else:
        return type(data).__name__
    

import os

def save_json_from_url(data, file_name):
    if not isinstance(data, dict):
        print('this is not dict')
        return None

    # JSONファイルとして保存
    from pathlib import Path
    file_name+=".json"
    file_path = Path(os.getcwd()) / "json" / file_name
    with open(file_path, 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"データは {file_path} に保存されました。")


# # 関数の使用例
# url = 'https://note.com/api/v2/categories'
# file_path = 'categories.json'
# save_json_from_url(url, file_path)



class NoteAPIFetcher:
    BASE_URL = "https://note.com/api"

    def __init__(self):
        self.session = requests.Session()

    def fetch_categories(self):
        response = requests.get(f'{self.BASE_URL}/v2/categories')
        return response.json()

    def fetch_users(self):
        response = requests.get(f'{self.BASE_URL}/v2/users')
        return response.json()

    def fetch_contests(self):
        response = requests.get(f'{self.BASE_URL}/v2/contests')
        return response.json()

    def fetch_hashtags(self):
        response = requests.get(f'{self.BASE_URL}/v2/hashtags')
        return response.json()

    def fetch_tech_articles(self):
        params = {'note_intro_only': 'true', 'sort': 'new', 'page': '1'}
        response = requests.get(f'{self.BASE_URL}/v1/categories/tech', params=params)
        return response.json()

    def fetch_user_info(self, username):
        response = requests.get(f'{self.BASE_URL}/v2/creators/{username}')
        return response.json()

    def fetch_user_articles(self, username):
        params = {'kind': 'note', 'page': '1'}
        response = requests.get(f'{self.BASE_URL}/v2/creators/{username}/contents', params=params)
        return response.json()

    def fetch_note_details(self, note_id):
        response = requests.get(f'{self.BASE_URL}/v3/notes/{note_id}')
        return response.json()

    def fetch_likes(self, note_id):
        response = requests.get(f'{self.BASE_URL}/v1/note/{note_id}/likes')
        return response.json()

    def fetch_comments(self, note_id):
        response = requests.get(f'{self.BASE_URL}/v1/note/{note_id}/comments')
        return response.json()





# NoteAPIFetcherのメソッド
# fetch_categories: カテゴリ一覧を取得
# fetch_users: ユーザー一覧を取得
# fetch_contests: コンテスト一覧を取得
# fetch_hashtags: ハッシュタグ一覧を取得
# fetch_tech_articles: 技術記事一覧を取得
# fetch_user_info: ユーザー情報を取得
# fetch_user_articles: ユーザー記事一覧を取得
# fetch_note_details: 記事詳細を取得
# fetch_likes: お気に入り一覧を取得
# fetch_comments: コメント一覧を取得

# NoteAPIFetcherの使用例
fetcher = NoteAPIFetcher()
# categories = fetcher.fetch_categories()
# users = fetcher.fetch_users()
# contests = fetcher.fetch_contests()
# hashtags = fetcher.fetch_hashtags()
# tech_articles = fetcher.fetch_tech_articles()

# for name, data in [('categories', categories), ('users', users), ('contests', contests), ('hashtags', hashtags), ('tech_articles', tech_articles)]:
#     save_json_from_url(data, file_name="{}".format(name))
    

username="hagure_melon"
note_id="66584562"
user_info = fetcher.fetch_user_info(username)
user_articles = fetcher.fetch_user_articles(username)
note_details = fetcher.fetch_note_details(note_id)
likes = fetcher.fetch_likes(note_id)
comments = fetcher.fetch_comments(note_id)
for name, data in [('user_info', user_info), ('user_articles', user_articles), ('note_details', note_details), ('likes', likes), ('comments', comments)]:
    save_json_from_url(data, file_name="{}".format(name))

breakpoint()

# フォローする
# follow_response = requests.post('https://note.com/api/v1/followings/2603882', data={'user_id': 'your_user_id'})  # POST request example
# print(follow_response.json()))






def fetch_notes():
    response = requests.get('https://note.com/api/v2/notes')
    return response.json()

def fetch_categories():
    response = requests.get('https://note.com/api/v2/categories')
    return response.json()

def fetch_users(page=1):
    response = requests.get('https://note.com/api/v2/users', params={'page': page})
    return response.json()

def fetch_contests():
    response = requests.get('https://note.com/api/v2/contests')
    return response.json()

def fetch_hashtags():
    response = requests.get('https://note.com/api/v2/hashtags')
    return response.json()

def fetch_hashtag_details(hashtag):
    response = requests.get(f'https://note.com/api/v2/hashtags/{hashtag}')
    return response.json()


def fetch_articles_by_category(category, page=1):
    params = {'note_intro_only': 'true', 'sort': 'new', 'page': str(page)}
    response = requests.get(f'https://note.com/api/v1/categories/{category}', params=params)
    return response.json()

def fetch_user_info(username):
    response = requests.get(f'https://note.com/api/v2/creators/{username}')
    return response.json()

def fetch_user_articles(username, page=1):
    params = {'kind': 'note', 'page': str(page)}
    response = requests.get(f'https://note.com/api/v2/creators/{username}/contents', params=params)
    return response.json()

def fetch_note_details(note_id):
    response = requests.get(f'https://note.com/api/v1/notes/{note_id}')
    return response.json()

def fetch_likes(note_id):
    response = requests.get(f'https://note.com/api/v1/note/{note_id}/likes')
    return response.json()

def fetch_comments(note_id):
    response = requests.get(f'https://note.com/api/v1/note/{note_id}/comments')
    return response.json()


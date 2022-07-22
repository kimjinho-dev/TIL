import json
from pprint import pprint


def movie_info(movie, genres):
    dict_movie = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_ids': movie.get('genre_ids'),
        'genre_names': [],
    }
    for genre_id in dict_movie['genre_ids']:
        for genre in genres:
            if genre_id == genre['id']:
                dict_movie['genre_names'].append(genre['name'])
    del dict_movie['genre_ids']
    return dict_movie


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

import json
from pprint import pprint


def movie_info(movies, genres):
    dict_movies = []
    for movie in movies:
        dict_movies.append(
            {
                'id': movie.get('id'),
                'title': movie.get('title'),
                'poster_path': movie.get('poster_path'),
                'vote_average': movie.get('vote_average'),
                'overview': movie.get('overview'),
                'genre_ids': movie.get('genre_ids'),
                'genre_names': [],
            }
        )

    for dict_movie in dict_movies:
        for genre_id in dict_movie['genre_ids']:
            for genre in genres:
                if genre_id == genre['id']:
                    dict_movie['genre_names'].append(genre['name'])
        del dict_movie['genre_ids']
    return dict_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

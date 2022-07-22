import json


def dec_movies(movies):

    release_12 = []

    for movie in movies:
        movie_json = open(f'data/movies/{movie["id"]}.json', encoding='utf-8')
        movie_val = json.load(movie_json)
        if "12" == movie_val["release_date"][5:7]:
            release_12.append(movie_val["title"])
    return release_12


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))

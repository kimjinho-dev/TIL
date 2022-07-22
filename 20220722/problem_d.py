import json


def max_revenue(movies):

    high_revenue = {
        "revenue": 0,
        "movie_name": "",
    }
    for movie in movies:
        movie_json = open(f'data/movies/{movie["id"]}.json', encoding='utf-8')
        movie_val = json.load(movie_json)
        if high_revenue["revenue"] < movie_val["revenue"]:
            high_revenue["revenue"] = movie_val["revenue"]
            high_revenue["movie_name"] = movie_val["title"]
    return high_revenue["movie_name"]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))

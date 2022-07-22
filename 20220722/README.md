# PJT 01

### 이번 pjt 를 통해 배운 내용

* open 함수를 통해 파일을 코드로 통해서 내용을 확인하고 값을 사용하는 방법. 이를 통해 많은 데이터 사용시 편리함.
* 실제 웹사이트에 사용되는 기능을 유사하게 코딩으로 구현화


## A. 제공되는 영화 데이터의 주요내용 수집

* 요구 사항 : 제공 되는 파일값에서 필요한 데이터 내용을 수집하는 함수 제작

* 결과 : movie_json 아규먼트 값을 가지고 movie_info 함수에서 문제에서 요구하는 내용을 저장하여 return 해주어서 정상 작동 확인.
  
* 문제 접근 방법 및 코드 설명

먼저 받아온 파일값이 어떻게 저장되어있는지 print()로 확인한다.
딕셔너리에 key,value를 확인하고 키값에 맞는 값을 반환하기위해 get메소드를 사용하기로 했다.
새로운 딕셔너리에 이를 저장하고, 리턴하여 pprint를 통해 출력되도록 한다. 
  
  ```python
  def movie_info(movie):
    dict_movie = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_ids': movie.get('genre_ids'),
    }
    return dict_movie
  ```
  
* 이 문제에서 어려웠던점

open, json 처음 사용해보는 것이여서 기존에 아는 딕셔너리 추출이 실제로 문제없이 되는지부터 확인해야했다.
정상적으로 작동된다는것을 안되에는 어떻게 값을 가져오는것이 효율적인지 고민하게되었다.


* 내가 생각하는 이 문제의 포인트

movie_json를 아규먼트로 가져온 movie_info에서 어떻게 key값과 value값을 가져올지 생각하는것같다.
get 메소드를 통하여 편리하고 빠르게 이해할 수 있는 코드를 작성하는것을 알게되었다.


## B. 제공되는 영화 데이터의 주요내용 수정

* 요구 사항 : A 문제에서 받아온 영화정보에서 genres.json 파일에 있는 genre_ids에 알맞는 genre_names의 값으로 변환하여 저장하여라

* 결과 : A에서 만든 값과 다르게 genre_ids에 저장된 키값이 사람이 이해하기 편한 단어의 형태로 바뀌어 출력된다.
  
* 문제 접근 방법 및 코드 설명

먼저 genres 에서 ids가 일치한것을 확인하여 해당 단어형태로 바꾸어서 저장하도록한다.
genres는 리스트 형태로 되어있기때문에 for문을 사용하여 딕셔너리형태를 하나씩 확인한다.
키값이 같다면 영화 장르명을 리스트형으로 저장하고, 이 값을 출력한다.

  ```python
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
  ```
  
* 이 문제에서 어려웠던점

open, json 처음 사용해보는 것이여서 기존에 아는 딕셔너리 추출이 실제로 문제없이 되는지부터 확인해야했다.
정상적으로 작동된다는것을 안되에는 어떻게 값을 가져오는것이 효율적인지 고민하게되었다.


* 내가 생각하는 이 문제의 포인트

movie_json를 아규먼트로 가져온 movie_info에서 어떻게 key값과 value값을 가져올지 생각하는것같다.
get 메소드를 통하여 편리하고 빠르게 이해할 수 있는 코드를 작성하는것을 알게되었다.

-----


## C. 다중 데이터 분석 및 수정

* 요구 사항 : 하나가 아닌 20개의 영화데이터를 problem_b 함수를 재사용하여 저장하려 반환하라

* 결과 : 20개의 영화 데이터가 딕셔너리 형태로 정상적으로 저장되고 반환됨.
  
* 문제 접근 방법 및 코드 설명

problem_b의 함수를 재사용하여 for문을 통해 리스트형에 20개의 딕셔너리형 영화데이터를 넣고자 하였다.
하나의 딕셔너리를 넣는 코드는 problem_b를 재사용하였고, 이를 for문을 사용하여 딕셔너리 한개씩 순차적으로 저장하도록 하였다.
다만, 리스트에 데이터 추가이다보니 append 메소드를 사용하였고 이후에 있는 장르리스트로 변경하는 for문에도 하나를 추가하여 모든 값에대해서 작동하도록 작성하였다.
  
  ```python
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
  ```
  
* 이 문제에서 어려웠던점

problem_b의 함수를 재사용하고자 하니 데이터값이 하나만 나온다는점과, 장르키->장르명으로 변환하는데에서 어떻게 모든 딕셔너리값에서 작동할지 고민하였다.
이를 해결하기위해 for문을 각각 하나씩 더 중첩시켜주었고, 단순 입력이 아닌 append 메소드 사용 / for문 중첩에 따른 변수명 통일을 하였다. 

* 내가 생각하는 이 문제의 포인트

하나가 아닌 여러개의 딕셔너리가 들어있는 리스트에 대해서 어떻게 처리를 하는지. 그리고 함수를 재사용시 크게 변경점없이 깔끔하게 사용하는 방법에 대한것같다.    

## D. 알고리즘을 사용한 데이터 출력

* 요구 사항 : 영화 정보 내 수입 정보를 통하여 영화 정보내에서 가장 높은 수익인 영화를 출력하라.

* 결과 : movies.json 영화데이터 내에 가장 높은 수익의 영화 출력 
  
* 문제 접근 방법 및 코드 설명

최대값을 저장하는 변수 하나를 만들고, 모든 영화정보의 수익정보를 검색하면서 비교하여 더 큰값을 넣고 그 영화이름도 저장하는 함수를 제작한다.
movies 폴더에 있는 모든 파일을 확인해야하기때문에, open으로 파일을 열때 받는 값이 문자열인점을 이용하여, 영화 id값으로 파일을 열어서 확인한다.
모든 파일을 그렇게 열어서 확인하여, 최대 수익인 영화값을 출력한다.

  ```python
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
  ```
  
* 이 문제에서 어려웠던점

movies 파일을 모두 열어서 확인한다, 라는 점을 어떻게 코딩해야하는지 잘 떠오르지 않았다. 그러다 open으로 받는 값은 문자열이며
movies.json에는 id가 들어있고 movies폴더안에 있는 값들은 id.json이라는 것을 떠올려서 모든 파일을 열수 있는 for문을 만들었다.
open 함수에 대한 이해도가 부족해서 어려웠던것같다.

* 내가 생각하는 이 문제의 포인트

모든 파일의 이름이 저장된 파일이 있다면 open함수에서 문자열 포맷을 통해서 간단하게 원하는 파일을 여는 코드를 작성할 수 있다.
open함수에 대한 이해도가 중요하다.

## E. 알고리즘을 사용한 데이터 출력

* 요구 사항 : 개봉월이 12월인 영화를 찾아 그 영화 제목 리스트를 출력하라.

* 결과 : 개봉월이 12월인 영화들이 출력된다.
  
* 문제 접근 방법 및 코드 설명
 
 D 문제의 코드를 재사용한다. 이번에는 영화제목을 담을 리스트를 만들어두고, 파일을 하나씩 확인하면서 개봉날짜가 담긴 값을 찾아오고 그중 월이 적혀있는 위치만 찾아서 12월이 맞는지 확인한다. 맞다면 그 영화의 제목을 리스트에 담는다.
 코드의 형식은 D에서 사용한것을 거의 사용했고, 차이점은 개봉일자 값에서 [5:7]로 개봉월만 검색을 한것이다. 이를 리스트에 담고 출력한다.
  
  ```python
  def dec_movies(movies):

    release_12 = []

    for movie in movies:
        movie_json = open(f'data/movies/{movie["id"]}.json', encoding='utf-8')
        movie_val = json.load(movie_json)
        if "12" == movie_val["release_date"][5:7]:
            release_12.append(movie_val["title"])
    return release_12
  ```
  
* 이 문제에서 어려웠던점
  
가운데 월이 12월인것을 어떻게 찾아야 하는지에 대해서 고민하였다.
개봉일자는 yyyy-mm-dd 이기때문에, [5:7] 을 한다면 정확하게 월만 슬라이싱 된다는것을 생각해냈다. 이를 통해 비교하여 12월이 개봉월인 영화를 찾을 수 있다.

* 내가 생각하는 이 문제의 포인트
  
이전 D문제에서 사용한것을 재사용한다. 단순히 값을 비교만 하면되었던 D와 달리 그 값에서 특정 부분을 추출하는 슬라이싱을 사용해야한다.
추출된 값을 통해 D와 마찬가지로 문제를 해결한다.   

-----

....


# 후기

* 그동안 배운 코딩이 실제로 파일의 내용을 사용하고, 이를 통해 영화 리뷰가 있는 웹사이트의 데이터 출력을 할 수 있다는 생각이 들었다.
* 점점 배운 코딩이 실체화를 시킬수 있다는것을 느꼇다.
* open 함수에 대해 좀더 범용성 있게 사용하는 방법을 보고, 함수를 사용할때 한가지 방식에 얽매이지 말고 여러방법으로 사용하는것에 대해 생각해야겠다.

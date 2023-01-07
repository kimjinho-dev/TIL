# 인프런_김영한강사님_스프링 입문

## view 환경설정

### controller

장고 mvc중 m의 역활을 하는것이 controoller이다. 좀더 간단하게 예기하면 url쪽이다.  
그 외에도 url패턴에서 변수를 받아서 해당 url에서 사용할 수 있는것까지도 비슷하다.  
controller는 일반적으로 기본도메인(main.java...프로젝트명)에서 .controller.컨트롤러명.java 형식으로 작성되면 자동으로 인식한다.  
controller 내부 코드는 아래와 같다  
```java
@Controller  //controller 라는것을 명시하는 어노테이션
public class FirstController {
    @GetMapping("/hi")  //url 패턴. /은 루트위치이므로 뒤에 붙는것은 주소
    public String hello(Model model) {  // 변수를 넘기기 위해선 Model
        model.addAttribute("name", "김진호"); // 앞은 변수명, 뒤는 값
        return "hello3";  // resources/templates에서 찾을 파일.
    }
}
```

### mustache

인프런 김영한님 강의에서는 .html파일을 thymeleaf 템플릿 엔진을 사용했지만, 찾아보니 mustache이 사용이 쉽고 호환성도 좋아보여서 사용중이다. 이후에 프로젝트 인원의 사용에 따라 변경될 가능성이 있다.

보통 스프링은 thymeleaf를 사용하지만, vue.js 용법과 비슷한 방식이여서 배우기에 어려울 수 있다.   
JSP는 스프링에서 권장하지는 않지만, 많이 사용하신다.  
mustache는 스프링부트에서 공식으로 지원한다.  


❗ 단 처음 mustache 인식이 안되는 문제점이 있어서 아래와 같은 설정을 진행하였다

```java
//application.properties
spring.mustache.suffix=.mustache  // mustache를 인식하게 하는것같다.
server.servlet.encoding.force=true // 한글 깨짐 현상
//build.gradle
implementation 'org.springframework.boot:spring-boot-starter-mustache' // 의존성 추가
```

mustache는 전달 받은 변수 사용시 `{{변수명}}` 형식을 사용하면된다.  
thymeleaf의 경우 html 속성을 이용하는 방식이여서 설정해야하는것이 좀 불편해 보이는데, mustache경우에는 보기에는 깔끔해보인다.  



++ 
devtool을 설치하면 html만 컴파일하면 서버 재부팅없이 즉각적으로 된다고한다.
하지만 mustache나 jsp 사용시에도 가능한가?

## 빌드하고 실행하기

### build

인텔리제이에서 실행버튼으로 서버를 키지 않고, 터미널에서 build가 가능하며 대체로 이쪽을 권장한다.  
터미널에서 빌드할 폴더까지 접근하고, `.gradlew build`를 입력한다.  
이제 build/libs 에 jar 파일이 생성된다.  
해당 폴더까지 이동을 한 후 `java -jar jar파일이름.jar`을 입력하면 성공적으로 서버가 실행된다.  
이 jar 파일이 서버 배포시에 사용되는 서버실행파일이다.  
만약 빌드한 파일을 없애려고 한다면, `.gradlew clean build` 로 제거 할 수 있다.

### 정적 컨텐츠

정적컨텐츠(static content)는 기존 html과 같이 컨텐츠를 그대로 가져다가 보여주는것.  
스프링 부트는 처음 요청을 받은 요청에 대해 컨트롤러를 찾아보고, 만약 없다면 static 폴더에서 찾고 있다면 이를 반환한다.

### MVC와 템플릿 엔진
MVC = Model, View, Controller  

View는 말 그대로 화면에 나타냄  
controller는 비즈니스 로직을 처리  
Model은 

```java
//controller
@GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "helloMvc";
    }
```
이렇게 컨트롤러를 만든다면, 이제 `localhost:8080/hello-mvc?name=내이름` 으로 접근 할 수 있다.  
이것은 정적컨텐츠와 달리, controller에서 name에 대한 정보를 가지고 템플릿 엔진이 hello-mvc를 그에맞게 변환되어 보여지게 하는것이다.  
즉 이 일련의 과정이 MVC이고 Controller가 요청받고, 데이터를 model을 가지고 템플릿 엔진에서 변환된 html(여기선 mustache)가 view로서 사용자에게 보여지는것이다.

## API

### API
정적컨텐츠를 제외하고서 데이터를 옮길때는 html로 내리냐, API로 내리냐의 차이가 있다.

```java
@GetMapping("hello-string")
@ResponseBody
    public String helloString(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello" + name;
    }
```
이전 코드와의 제일 큰 차이는 ResponseBody이다. 이는 html과 다른 방식인데 위의 방식은 view로서 보여준다고하면, api는 순수 데이터만 전달한다.

좀더 api스러운 용법을 보자면 
```java
@GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name, Model model) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }

    static class Hello {
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
```
로 만들고 접근하면 json방식으로 출력되는것을 볼 수 있다.

api의 진행방식은 이와같다  
먼저 controller에서 찾는다.  
reponsebody가 있다면, html에 담아서 보내는것이 아니라 데이터 그자체로 보내려한다. 대부분 전달해야할 데이터는 객체이기때문에 json 형식으로 반환한다.

## 20230110

### GET API

백엔드쪽에서는 별도의 페이지 없이 api통신을 한다.  
통신은 controller에서 지정된 url에 요청이 들어왔을때, return으로 필요한 값을 반환해준다.  
직접 주소에 들어오는 값을  
`@RequestParam` `@PathVariable` 등으로 파라미터값처럼 넘겨서 사용할 수 있다.  
하지만 이런 방식보다는, dto로 미리 받을 데이터 형식을 정해주고 형식에 맞게 들어온 값을 dto로 반환함으로써 반복없이 구현한다.  

### POST API

GET이 조회라면 POST는 리소스를 저장할때 사용된다. GET은 url경로다 파라미터에 변수를 넣어 요청을 보내지만, POST는 리로스나 값을 HTTP body에 담아 서버에 전달한다.  
기초적인 형식은 GET과 같으며, 어노테이션만 `@PostMapping`인점이 다르다. 마찬가지로 `@PostMapping` 을 사용하면 메서드 입력은 필요없다.  

+ DTO 사용과 MAP 사용의 차이
DTO는 정해진 형식일때, Map은 어떤 변수로 들어올지 모를때 사용한다.

+ public String 과 public Dto 의 차이
String으로 선언시 `return dto.toString();` 형식으로 작성되며, 따라서 이미 지정된 형식으로 출력된다.(test/plain)  
하지만 dto로 선언시, `return dto;` 형식으로 작성되며, 이는 json형태로 출력된다(application/json)   

+
그럼 일일히 POST,GET,PUT.. 하나씩 다 만들어야하는걸까?  
이전처럼 한번에 다 만들 수는 없나?

### PUT API

put는 저장보다는 업데이트시에 사용한다. 형태는 POST와 같다. body에 데이터를 담아서 보내는 형태도 마찬가지다.  

+ `ResponseEntity`  
`ResponseEntity`를 사용하면 응답코드, Header와 Body를 더욱 쉽게 작성할 수 있게한다.  

### DELETE API

delete는 저장소에 있는 리소스를 삭제하는데 사용한다. delete는 저장소의 리소스를 조회하고, 삭제하기때문에 GET 메서드와 같은 형식이 사용된다.  


### JPA

JPA는 자바 진영의 ORM 기술 표준으로 채택된 인터페이스 모음이다. ORM이 큰 개념이여서 온전한 서비스를 구현하기 어려운점이 있는데, JAP는 좀더 구체화된 스펙을 포함하여 이를 보완한다.  
JDBC, 하이버네이트가 JPA를 사용할때 자주 듣게된다. 
``` 
이러한 JPA를 사용할때 Spring Data JPA 라이브러리를 사용한다. 하지만 해당 라이브러리는 DB가 비어있을때 오류가 발생하므로, DB를 구성후에 추가하는것이 좋다.
```

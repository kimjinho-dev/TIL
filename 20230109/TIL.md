[mysql]  
1. 스키마를 생성  
2. 테이블 우클릭->create  
3. 컬럼네임과 데이터 타입 입력가능  
4. PK는 PK, NN은 not null, AI는 자동증가(보통 아이디값같은곳)  
5. apply 하면 sql 쿼리문이 나오고 다시 apply  

[db설정]  

<properties>  
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver  
spring.datasource.username=root  
spring.datasource.password=1234  
spring.datasource.url=jdbc:mysql://localhost:3306/board  

<gradle>
implementation 'mysql:mysql-connector-java'  
와 같은 설정값을 입력해준다.   

GetMapping은 주소 위치  
RespinseBody는 return 그대로 반환한다는 뜻  


[코드 진행]
1. 컨트롤러로 form 진입  
2. submit 시 board/writedo로 진입, 컨트롤러에서 찾아서 실행  
3. boardService.write 메서드 진입  
4. boardRepository로 세이브(mysql에 저장)  
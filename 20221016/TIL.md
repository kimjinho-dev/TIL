# SQL문 변환(한글문장 -> sql)
SELECT exam FROM all
SELECT exam FROM 

# ORM문 변환(한글문장 -> orm)
exam.objects.all()
exam.objects.get(pk=colum_1)

# 관계형 데이터 베이스 이론


## RDB

## PK
테이블의 행의 고유성을 식별할때 사용되는 컬럼. 암시적으로 NOT NULL 제약조건이 있다.

## 스키마

## 테이블

## 행

## 열

# SQL 이론
모든 SQL은 SELECT 같은 키워드로 시작하며, ;으로 구분한다.  
SQL은 대소문자를 구분하지않지만, 대문자로 작성을 권장한다.  
`SELECT colum_name FROM table_name;`  
은 하나의 statement이며  
`SELECT column_name` 과 `FROM table_name` 2개의 clause로 구성된다.  
(clause는 statement 하위개념)  

SQL은 정적 데이터타입이 아닌, 동적 데이터 타입을 사용한다. 컬럼에 선언된 데이터 타입을 사용은 하지만, 실제로는 컬럼에 저장된 값에 따라 데이터 타입이 결정된다.  

## DDL
데이터 '정의' 언어 : 생성, 수정, 삭제 등 데이터 베이스를 정의
ex) create(생성), drop(삭제), alter(수정)

## DML
데이터 '조작' 언어 : 데이터를 추가, 조회, 변경, 삭제  
ex) insert, select(조회), update, delete  
SELECT의 ORDER BY clause  
: 결과를 정렬함


## DCL
데이터 '제어' 언어 : 데이터 보안, 제어, 권한 부여 등
ex) grant, revoke, commit, rollback

## 간단하게 셋 차이점으로 구분하기
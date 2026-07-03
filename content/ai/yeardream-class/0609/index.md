---
title: "0609 수업 정리"
date: 2026-06-09
description: "이어드림 스쿨 0609 수업 내용을 정리한 글입니다."
categories: ["수업 내용 정리"]
tags: ["이어드림", "수업정리"]
draft: false
---

# 0609 수업 정리

MY구글드라이브 : https://drive.google.com/drive/u/0/folders/1-L7BjitGN8LNbRHYPv1lBbzIZca2mRlo

---

강의주제: 2주차-05-SQL함수와서브쿼리

날짜: 2026년 6월 9일

구글드라이브: https://drive.google.com/drive/folders/1reoyT3pAy1cpYDHK4v74XP2CvaxUG6Nz?usp=sharing

상태: 완료

전화번호: 01072072163

게시-URL: https://torch-law-f0b.notion.site/260609-370d0b4d457380e5aa8cc6903b547140?source=copy_link

# 시험

- 파일명 : `Day01-quiz.sql` 파일 생성 후 다음 문제를 붙여 넣어주세요
- 파일 위치는 `04_SQL시작하기` 폴더 내

```sql
/*============================================================
  Chinook SQL 퀴즈 20문제 (정답 포함)
  - 실행 대상: chinook.db
  - 범위: SELECT / DISTINCT / WHERE / 비교 / AND·OR·NOT
          / BETWEEN·IN·NOT IN / LIKE / ORDER BY
  - 풀이법: 문제(주석)를 읽고 직접 작성 -> 아래 정답과 비교
============================================================*/

/*------------ SELECT 기본 ------------*/

-- Q1. 마케팅팀이 우리가 보유한 모든 앨범의 제목 목록을 요청했습니다.
--     albums 테이블에서 제목(Title)만 보여주세요.
SELECT Title
FROM albums;

-- Q2. 고객 명부에서 이름/성/이메일만 추려 달라는 요청입니다.
--     customers 테이블에서 FirstName, LastName, Email 을 보여주세요.
SELECT FirstName, LastName, Email
FROM customers;

/*------------ DISTINCT ------------*/

-- Q3. 우리 고객이 어느 나라들에 분포하는지 "나라 목록"이 궁금합니다.
--     customers 의 Country 를 중복 없이 보여주세요.
SELECT DISTINCT Country
FROM customers;

/*------------ WHERE + 비교 연산자 ------------*/

-- Q4. 브라질(Brazil) 고객만 따로 확인하려 합니다.
--     customers 에서 Country 가 'Brazil' 인 고객을 모두 보여주세요.
SELECT *
FROM customers
WHERE Country = 'Brazil';

-- Q5. 재생 시간이 5분(=300000 밀리초)을 넘는 긴 곡을 찾으려 합니다.
--     tracks 에서 Milliseconds 가 300000 초과인 곡을 보여주세요. (앞 10건)
SELECT Name, Milliseconds
FROM tracks
WHERE Milliseconds > 300000
LIMIT 10;

-- Q6. 결제 금액이 큰 인보이스를 점검합니다.
--     invoices 에서 Total 이 15 이상인 건을 보여주세요.
SELECT *
FROM invoices
WHERE Total >= 15;

-- Q7. 단가가 0.99 가 아닌(특별 단가) 곡을 찾으려 합니다.
--     tracks 에서 UnitPrice 가 0.99 가 아닌 곡을 보여주세요. (앞 10건)
SELECT Name, UnitPrice
FROM tracks
WHERE UnitPrice != 0.99
LIMIT 10;

/*------------ 복합 조건 (AND / OR / NOT) ------------*/

-- Q8. 미국 캘리포니아(CA) 거주 고객을 찾습니다.
--     customers 에서 Country 가 'USA' 그리고 State 가 'CA' 인 고객을 보여주세요.
SELECT *
FROM customers
WHERE Country = 'USA' AND State = 'CA';

-- Q9. 미국 또는 캐나다 고객을 한 번에 보려 합니다.
--     customers 에서 Country 가 'USA' 이거나 'Canada' 인 고객을 보여주세요.
SELECT *
FROM customers
WHERE Country = 'USA' OR Country = 'Canada';

-- Q10. 미국이 아닌 해외 고객만 보려 합니다.
--      customers 에서 Country 가 'USA' 가 아닌 고객을 보여주세요.
SELECT *
FROM customers
WHERE NOT Country = 'USA';
-- (WHERE Country != 'USA' 와 동일)

/*------------ 기타 연산자 (BETWEEN / IN / NOT IN) ------------*/

-- Q11. 결제 금액이 5~10달러 사이인 인보이스를 보려 합니다. (5와 10 포함)
SELECT *
FROM invoices
WHERE Total BETWEEN 5 AND 10;

-- Q12. 독일/프랑스/포르투갈 고객만 한 번에 뽑으려 합니다.
--      customers 에서 Country 가 'Germany','France','Portugal' 중 하나인 고객.
SELECT *
FROM customers
WHERE Country IN ('Germany', 'France', 'Portugal');

-- Q13. 위 세 나라를 제외한 나머지 나라 고객을 보려 합니다.
SELECT *
FROM customers
WHERE Country NOT IN ('Germany', 'France', 'Portugal');

/*------------ LIKE — 유사한 값 찾기 ------------*/

-- Q14. 제목이 'The' 로 시작하는 곡을 찾으려 합니다.
--      tracks 에서 Name 이 'The' 로 시작하는 곡을 보여주세요. (앞 10건)
SELECT Name
FROM tracks
WHERE Name LIKE 'The%'
LIMIT 10;

-- Q15. 'Live' 로 끝나는(라이브) 앨범을 찾으려 합니다.
--      albums 에서 Title 이 'Live' 로 끝나는 앨범을 보여주세요.
SELECT *
FROM albums
WHERE Title LIKE '%Live';

-- Q16. 곡 제목 어딘가에 'Love' 가 들어간 곡을 찾으려 합니다. (앞 10건)
SELECT Name
FROM tracks
WHERE Name LIKE '%Love%'
LIMIT 10;

-- Q17. gmail 을 쓰는 고객을 찾으려 합니다.
--      customers 에서 Email 이 '@gmail.com' 으로 끝나는 고객을 보여주세요.
SELECT FirstName, LastName, Email
FROM customers
WHERE Email LIKE '%@gmail.com';

/*------------ ORDER BY — 정렬 ------------*/

-- Q18. 재생 시간이 가장 긴 곡부터 보고 싶습니다.
--      tracks 를 Milliseconds 내림차순으로 정렬해 보여주세요. (앞 10건)
SELECT Name, Milliseconds
FROM tracks
ORDER BY Milliseconds DESC
LIMIT 10;

-- Q19. 결제 금액이 가장 큰 인보이스 5건을 보려 합니다.
SELECT *
FROM invoices
ORDER BY Total DESC
LIMIT 5;

/*------------ 종합 (조건 + 정렬) ------------*/

-- Q20. 미국에서 발생한 인보이스 중 금액이 큰 순으로 상위 5건을 보려 합니다.
--      invoices 에서 BillingCountry 가 'USA' 인 건을 Total 내림차순으로 5건.
SELECT *
FROM invoices
WHERE BillingCountry = 'USA'
ORDER BY Total DESC
LIMIT 5;
```

## Having절

```sql
/* ===================  02. HAVING (그룹에 조건)  ==================== */

-- 문제 6.
-- 아티스트별 앨범 수를 구하되, 앨범이 5개 이상인 아티스트만 보여주세요.
-- 테이블 : albums
SELECT ArtistId, COUNT(*) AS album_cnt 
FROM albums 
GROUP BY ArtistId
HAVING COUNT(*) > 5
;

-- 문제 7.
-- 앨범별 트랙 수를 구하되, 트랙이 15개를 초과하는 앨범만 보여주세요.
-- 테이블 : tracks
SELECT AlbumId, COUNT(*) as track_cnt
FROM tracks 
GROUP BY AlbumId
HAVING COUNT(*) > 15
;

-- 문제 8.
-- 국가별 매출 합계를 구하되, 매출 합계가 100을 초과하는 국가만 보여주세요.
-- 테이블 : invoices
SELECT BillingCountry, SUM(Total) as total_sales
FROM invoices 
GROUP BY BillingCountry
HAVING SUM(Total) > 100
;

-- 문제 9.
-- 고객별(CustomerId) 인보이스 건수를 구하되,
-- 인보이스가 7건 이상인 고객만 보여주세요.
-- 테이블 : invoices
SELECT CustomerId, COUNT(*) as invoice_cnt
FROM invoices 
GROUP BY CustomerId
HAVING COUNT(*) >= 7
;

-- 문제 10.
-- 장르별 트랙 수를 구하되, 트랙이 100개 이상인 장르만
-- 트랙이 많은 순으로 보여주세요.
-- 테이블 : tracks
SELECT GenreId, COUNT(*) as track_cnt
FROM tracks 
GROUP BY GenreId
HAVING COUNT(*) >= 100
ORDER BY 2 DESC
;
```

## INNER JOIN

```sql
-- 문제 14.
-- 인보이스 상세(invoice_items)와 트랙(tracks)을 연결해
-- 인보이스 항목 ID, 트랙 이름, 단가(UnitPrice), 수량(Quantity)을 보여주세요.
SELECT invoice_items.InvoiceLineId,
       tracks.Name,
       invoice_items.UnitPrice,
       invoice_items.Quantity
FROM invoice_items
INNER JOIN tracks
  ON invoice_items.TrackId = tracks.TrackId;

-- 문제 15.
-- 고객(customers)과 담당 직원(employees)을 연결해
-- 고객 이름과 담당 직원 이름을 보여주세요.
-- (customers.SupportRepId = employees.EmployeeId)
SELECT customers.FirstName AS customer_name,
       employees.FirstName AS support_rep
FROM customers
INNER JOIN employees
  ON customers.SupportRepId = employees.EmployeeId;

-- 문제 16.
-- 트랙-앨범-아티스트 3개 테이블을 연결해
-- 트랙 이름, 앨범 제목, 아티스트 이름을 함께 보여주세요. (앞 20건)
SELECT tracks.Name AS track_name,
       albums.Title AS album_title,
       artists.Name AS artist_name
FROM tracks
INNER JOIN albums  ON tracks.AlbumId = albums.AlbumId
INNER JOIN artists ON albums.ArtistId = artists.ArtistId
LIMIT 20;
```

## RIGTH JOIN

```sql
-- 문제 19.
-- 모든 앨범(albums)을 기준으로 아티스트(artists)를 연결하세요.
-- (RIGHT JOIN 사용: 오른쪽 테이블 albums의 모든 행을 출력)
-- 주의: RIGHT JOIN은 SQLite 3.39.0 이상에서만 동작합니다.
SELECT artists.Name, albums.Title
FROM artists
RIGHT JOIN albums
  ON artists.ArtistId = albums.ArtistId;

-- 문제 20.
-- 19번과 '같은 결과'를 RIGHT JOIN 없이 LEFT JOIN으로 작성해 보세요.
-- (구버전 SQLite 호환: 테이블 순서를 뒤집어 왼쪽을 albums로 둡니다.)
SELECT artists.Name, albums.Title
FROM albums
LEFT JOIN artists
  ON artists.ArtistId = albums.ArtistId;

```

## 서브쿼리

- 문제 1번

```sql
-- 문제 1.
-- 'Balls to the Wall' 트랙보다 재생시간(Milliseconds)이 긴 트랙의
-- 이름과 재생시간을 조회하세요. (단일 행, > 연산자)
-- 메인쿼리 : 이름과 재생시간 조회
-- 서브쿼리 : 'Balls to the Wall'의 재생시간 조회 

-- 메인쿼리
SELECT Name, Milliseconds
FROM tracks
WHERE Milliseconds > 342562
;

-- 서브쿼리 
SELECT Milliseconds FROM tracks WHERE Name = 'Balls to the Wall';

-- 메인쿼리 + 서브쿼리

SELECT Name, Milliseconds
FROM tracks
WHERE Milliseconds > (
    SELECT Milliseconds FROM tracks WHERE Name = 'Balls to the Wall'
)
;
```

- 서브쿼리 문제 4-5번

```sql
-- 문제 4.
-- 앨범 'Let There Be Rock'에 수록된 트랙의 이름을 조회하세요.
-- 힌트: 앨범 1개의 AlbumId는 단일 행 → = 연산자 사용.
SELECT Name
FROM tracks
WHERE AlbumId = (
    SELECT AlbumId FROM albums WHERE Title = 'Let There Be Rock'
);

-- 문제 5.
-- 인보이스 총액(Total)이 전체 평균 총액보다 '작은'(<) 인보이스의
-- InvoiceId와 Total을 조회하세요.
SELECT InvoiceId, Total
FROM invoices
WHERE Total < (
    SELECT AVG(Total) FROM invoices
);
```

- 문제 6

```sql
-- 문제 6.
-- 'AC/DC'가 발매한 앨범에 속한 모든 트랙의 이름을 조회하세요.
-- 힌트: 아티스트→여러 앨범(다중 행)이므로 IN. (서브쿼리 중첩)
-- 메인쿼리 : 트랙의 이름 조회
SELECT Name FROM tracks;

-- 서브쿼리 : 'AC/DC'가 발매한 앨범ID
---- 서브쿼리의 메인쿼리 : AlbumID FROM Albums
SELECT AlbumId FROM albums;
---- 서브쿼리의 서브쿼리 : AC/DC의 ArtistID조회
SELECT ArtistId FROM artists WHERE Name = 'AC/DC';

-- 서브쿼리 합치기
SELECT AlbumId FROM albums
WHERE ArtistId = (
    SELECT ArtistId FROM artists WHERE Name = 'AC/DC'
);

-- 메인쿼리 : 트랙의 이름 조회
SELECT Name FROM tracks 
WHERE AlbumID IN (
    SELECT AlbumId FROM albums
    WHERE ArtistId = (SELECT ArtistId FROM artists WHERE Name = 'AC/DC')
);
```

- 문제 10번

```sql
-- 문제 10.
-- 'Rock' 장르의 트랙이 한 곡이라도 포함된 앨범의 제목을 조회하세요. (IN)
SELECT Title
FROM albums
WHERE AlbumId IN (
    SELECT AlbumId FROM tracks
    WHERE GenreId = (SELECT GenreId FROM genres WHERE Name = 'Rock')
);
```

# 0609 수업 정리

- [☀️ 오전 수업 내용 정리 - 보기 / 다운로드](files/260609_오전수업.pdf)
- [🌙 오후 수업 내용 정리 - 보기 / 다운로드](files/260609_오후수업.pdf)

## 수업 내용 필기 첨부 파일

- [0609필기 다운로드](files/0609_필기.txt)
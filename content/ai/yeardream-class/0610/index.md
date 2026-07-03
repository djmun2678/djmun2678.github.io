---
title: "0610 수업 정리"
date: 2026-06-10
description: "이어드림 스쿨 0610 수업 내용을 정리한 글입니다."
categories: ["수업 내용 정리"]
tags: ["이어드림", "수업정리"]
draft: false
---

# 0610 수업 정리

MY구글드라이브 : https://drive.google.com/drive/u/0/folders/1PNV7DXF5t99Eg4UhFwp6hH6FyzYF4Bud

---

강의주제: 3주차-01-집합연산자와계층형질의

날짜: 2026년 6월 10일

구글드라이브: https://drive.google.com/drive/folders/1DsR5DX1b1IW0qaM3mQ1ZVocqsBQ99DXk?usp=sharing

상태: 완료

전화번호: 01072072163

게시-URL: https://torch-law-f0b.notion.site/260610-377d0b4d4573803eb6b2c3ffc4042698?source=copy_link

# 서브쿼리

- 문제 11

```sql
-- 문제 11.  (강의자료의 ALL 개념)
-- 'Rock' 장르의 '모든' 트랙보다 재생시간이 긴 트랙의 이름을 조회하세요.
-- SQLite 미지원: WHERE Milliseconds > ALL (SELECT Milliseconds ...)
-- 대체: ALL → MAX (모든 값보다 크다 = 최댓값보다 크다)
SELECT Name, Milliseconds
FROM tracks
WHERE Milliseconds > (
    SELECT MAX(Milliseconds) FROM tracks
    WHERE GenreId = (SELECT GenreId FROM genres WHERE Name = 'Rock')
);

-- 문제 12.  (강의자료의 ANY 개념)
-- 'Jazz' 장르 트랙 중 '하나라도'보다 재생시간이 긴 트랙의 이름을 조회하세요.
-- SQLite 미지원: WHERE Milliseconds > ANY (...)
-- 대체: ANY → MIN (하나라도보다 크다 = 최솟값보다 크다)
SELECT Name, Milliseconds
FROM tracks
WHERE Milliseconds > (
    SELECT MIN(Milliseconds) FROM tracks
    WHERE GenreId = (SELECT GenreId FROM genres WHERE Name = 'Jazz')
);
```

# 시험

- 파일명 : `Day02-quiz.sql` 생성 하기

```sql
/* ===================================================================
   PART 1. GROUP BY (4문제)
   =================================================================== */

/* -------------------------------------------------------------------
   문제 1. [GROUP BY]
   시나리오:
   디지털 스토어는 MPEG, AAC 등 미디어 포맷별로 보유 트랙 수를 파악하려 합니다.
   tracks 테이블을 미디어 타입(MediaTypeId)별로 그룹지어
   포맷별 트랙 수(track_count)를 조회하세요.
   ------------------------------------------------------------------- */
SELECT MediaTypeId, COUNT(*) AS track_count
FROM tracks
GROUP BY MediaTypeId;

/* -------------------------------------------------------------------
   문제 2. [GROUP BY + ORDER BY]
   시나리오:
   물류·정산팀이 청구 도시(BillingCity)별 주문(인보이스) 건수를 분석합니다.
   invoices 테이블을 BillingCity별로 그룹지어 도시별 인보이스 건수를 구하고,
   주문이 많은 도시부터 내림차순으로 정렬하세요.
   ------------------------------------------------------------------- */
SELECT BillingCity, COUNT(*) AS invoice_count
FROM invoices
GROUP BY BillingCity
ORDER BY invoice_count DESC;

/* -------------------------------------------------------------------
   문제 3. [GROUP BY + HAVING]
   시나리오:
   고객 지원 센터는 담당 고객이 많은 직원의 업무 부담을 점검합니다.
   customers 테이블을 담당 직원(SupportRepId)별로 그룹지어
   직원별 담당 고객 수를 구하되, 담당 고객이 10명 이상인 직원만 출력하세요.
   ------------------------------------------------------------------- */
SELECT SupportRepId, COUNT(*) AS customer_count
FROM customers
GROUP BY SupportRepId
HAVING COUNT(*) >= 10;

/* -------------------------------------------------------------------
   문제 4. [GROUP BY + 집계 함수]
   시나리오:
   콘텐츠 기획팀이 장르별로 가장 긴 곡이 얼마나 되는지 비교하려 합니다.
   tracks 테이블을 장르(GenreId)별로 그룹지어
   장르별 최대 재생시간(max_ms)을 조회하고,
   재생시간이 긴 장르부터 내림차순으로 정렬하세요.
   ------------------------------------------------------------------- */
SELECT GenreId, MAX(Milliseconds) AS max_ms
FROM tracks
GROUP BY GenreId
ORDER BY max_ms DESC;

/* ===================================================================
   PART 2. JOIN (3문제)
   =================================================================== */

/* -------------------------------------------------------------------
   문제 5. [INNER JOIN]
   시나리오:
   트랙 상세 화면에 해당 곡의 미디어 포맷(예: MPEG audio file)을 표시해야 합니다.
   tracks 테이블과 media_types 테이블을 INNER JOIN하여
   트랙 이름(track_name)과 미디어 타입 이름(media_type)을 조회하세요.
   (연결 조건: tracks.MediaTypeId = media_types.MediaTypeId)
   ------------------------------------------------------------------- */
SELECT tracks.Name AS track_name, media_types.Name AS media_type
FROM tracks
INNER JOIN media_types
  ON tracks.MediaTypeId = media_types.MediaTypeId;

/* -------------------------------------------------------------------
   문제 6. [INNER JOIN — 판매·고객]
   시나리오:
   회계팀이 인보이스마다 어떤 고객에게 청구되었는지 확인하려 합니다.
   invoices 테이블과 customers 테이블을 INNER JOIN하여
   인보이스 ID(InvoiceId), 결제 금액(Total), 청구 국가(BillingCountry),
   고객 성(LastName), 고객 이름(FirstName)을 함께 조회하세요.
   ------------------------------------------------------------------- */
SELECT invoices.InvoiceId,
       invoices.Total,
       invoices.BillingCountry,
       customers.LastName,
       customers.FirstName
FROM invoices
INNER JOIN customers
  ON invoices.CustomerId = customers.CustomerId;

/* -------------------------------------------------------------------
   문제 7. [다중 INNER JOIN — 플레이리스트]
   시나리오:
   큐레이션 팀이 각 플레이리스트에 어떤 곡이 들어 있는지 목록을 뽑으려 합니다.
   playlists, playlist_track, tracks 세 테이블을 INNER JOIN하여
   플레이리스트 이름(playlist_name)과 트랙 이름(track_name)을 조회하세요.
   (playlist_track이 playlists와 tracks를 연결하는 중간 테이블입니다)
   ------------------------------------------------------------------- */
SELECT playlists.Name AS playlist_name,
       tracks.Name AS track_name
FROM playlists
INNER JOIN playlist_track
  ON playlists.PlaylistId = playlist_track.PlaylistId
INNER JOIN tracks
  ON playlist_track.TrackId = tracks.TrackId;

/* ===================================================================
   PART 3. 서브쿼리 (3문제)
   =================================================================== */

/* -------------------------------------------------------------------
   문제 8. [단일 행 서브쿼리 — WHERE + > / AVG]
   시나리오:
   VIP 고객 관리를 위해 평소보다 많이 결제한 '고액 주문' 인보이스를 찾습니다.
   결제 금액(Total)이 전체 인보이스 평균 총액보다 큰 인보이스의
   InvoiceId, CustomerId, Total을 조회하세요.
   힌트: 서브쿼리에서 AVG(Total)을 사용하면 단일 행이 반환됩니다.
   ------------------------------------------------------------------- */
SELECT InvoiceId, CustomerId, Total
FROM invoices
WHERE Total > (
    SELECT AVG(Total) FROM invoices
);

/* -------------------------------------------------------------------
   문제 9. [다중 행 서브쿼리 — IN]
   시나리오:
   브라질(BillingCountry = 'Brazil')로 청구된 주문이 한 번이라도 있는
   고객에게 지역 프로모션 메일을 내려 합니다.
   invoices에 브라질 청구 기록이 있는 고객의
   이름(FirstName), 성(LastName), 이메일(Email)을 조회하세요.
   힌트: 먼저 invoices에서 해당 국가의 CustomerId 목록을 구한 뒤 IN으로 연결합니다.
   ------------------------------------------------------------------- */
SELECT FirstName, LastName, Email
FROM customers
WHERE CustomerId IN (
    SELECT CustomerId FROM invoices WHERE BillingCountry = 'Brazil'
);

/* -------------------------------------------------------------------
   문제 10. [FROM 절 서브쿼리 — 파생 테이블]
   시나리오:
   경영진 보고용으로 국가별 매출 순위 상위 5개국만 뽑아야 합니다.
   먼저 invoices에서 국가(BillingCountry)별 매출 합계를 구한 뒤,
   그 결과를 파생 테이블로 사용해 매출이 높은 상위 5개 국가를 조회하세요.
   힌트: FROM 절 서브쿼리에는 반드시 별칭(AS ...)을 붙입니다.
   ------------------------------------------------------------------- */
SELECT BillingCountry, total_sales
FROM (
    SELECT BillingCountry, SUM(Total) AS total_sales
    FROM invoices
    GROUP BY BillingCountry
) AS country_sales
ORDER BY total_sales DESC
LIMIT 5;

```

# UNION

```sql
-- ──────────────────────────────────────────────────────────
-- 3-1. UNION - 합집합 (중복 제거)
-- ──────────────────────────────────────────────────────────

-- (a) 직원 이름 + 고객 이름 통합 목록
-- ref: https://www.sqlitetutorial.net/sqlite-union/
SELECT FirstName, LastName, 'Employee' AS Type 
FROM employees

UNION 

SELECT FirstName, LastName, 'Customer'
FROM customers

ORDER BY FirstName, LastName
;

-- (b) 구매 이력 유무별 고객 분류
-- 테이블명 : customers, invoices 
-- 출력 : CustomerId, FirstName + LastName 고객명 AS 고객명, 
--                 'Has Invoice' / 'No Invoice'
-- HINT : WHERE 절 Customer ID 활용해서 서브쿼리
SELECT 
    CustomerID
    , FirstName || ' ' || LastName AS 고객명
    , 'Has Invoice'
FROM customers
WHERE CustomerID IN (SELECT DISTINCT CustomerID FROM invoices)

UNION

SELECT 
    CustomerID
    , FirstName || ' ' || LastName AS 고객명
    , 'No Invoice'
FROM customers
WHERE CustomerID NOT IN (SELECT DISTINCT CustomerID FROM invoices)
;

-- ──────────────────────────────────────────────────────────
-- 3-2. UNION ALL - 합집합 (중복 포함, 더 빠름)
-- ──────────────────────────────────────────────────────────

-- (a) 연도별 매출 + 전체 합계 리포트 (소계 패턴)
SELECT 
    strftime('%Y', InvoiceDate) AS 연도
    , ROUND(SUM(Total), 2) AS 매출합계
FROM invoices
GROUP BY 연도

UNION ALL

SELECT '------전체합계' 
       , ROUND(SUM(Total), 1)
FROM invoices
;

-- (b) 장르별 트랙 수 + 전체 합계
-- 테이블명 : genres, tracks
-- LEFT JOIN 
SELECT 
    g.Name                AS 장르명
    , COUNT(t.TrackId)    AS 트랙수
FROM genres g
LEFT JOIN tracks t ON g.GenreId = t.GenreId
GROUP BY g.Name

UNION ALL

SELECT '------전체합계' 
       , count(*)
FROM tracks
;
```

## INTERSECT - 교집합

```sql
-- ──────────────────────────────────────────────────────────
-- 3-3. INTERSECT - 교집합
-- ──────────────────────────────────────────────────────────

-- (a) 청구서가 있는 고객 (INTERSECT 방식)
-- ref: https://www.sqlitetutorial.net/sqlite-intersect/
-- 현재 문제점.. Customers 59명, invoices 59명 모두 구매를 했음
-- 차집합을 하거나 할 때, 차이점이 존재하지 않는다. 

-- (b) 2009년과 2010년 모두 구매한 고객 ID
-- 2009년에 구매한 고객 ID 
-- 테이블 : invoices 

SELECT CustomerID 
FROM invoices 
WHERE strftime('%Y', InvoiceDate) = '2009'

INTERSECT

SELECT CustomerID 
FROM invoices 
WHERE strftime('%Y', InvoiceDate) = '2010'
;

-- 고객 이름 궁금함, 고객 ID FirstName, LastName
SELECT c.CustomerID, FirstName, LastName
FROM customers c
INNER JOIN (
    SELECT CustomerID 
    FROM invoices 
    WHERE strftime('%Y', InvoiceDate) = '2009'

    INTERSECT

    SELECT CustomerID 
    FROM invoices 
    WHERE strftime('%Y', InvoiceDate) = '2010'
) y
ON y.CustomerID = c.CustomerID
;

-- ──────────────────────────────────────────────────────────
-- 3-4. EXCEPT - 차집합
-- ──────────────────────────────────────────────────────────

-- (a) 청구서 없는 고객 (전체 - 청구서 있는 고객)
-- ref: https://www.sqlitetutorial.net/sqlite-except/

-- (b) 2009년 구매 고객 중 2010년에 구매 안 한 고객
SELECT CustomerID 
FROM invoices 
WHERE strftime('%Y', InvoiceDate) = '2009'

EXCEPT

SELECT CustomerID 
FROM invoices 
WHERE strftime('%Y', InvoiceDate) = '2010'
;

SELECT c.CustomerID, FirstName, LastName
FROM customers c
INNER JOIN (
    SELECT CustomerID 
    FROM invoices 
    WHERE strftime('%Y', InvoiceDate) = '2009'

    EXCEPT

    SELECT CustomerID 
    FROM invoices 
    WHERE strftime('%Y', InvoiceDate) = '2010'
) y
ON y.CustomerID = c.CustomerID
;
```

```sql
-- ============================================================
-- PART 4. 집계 함수 + 서브쿼리 + 집합 연산자 복합 활용
-- ============================================================

-- ──────────────────────────────────────────────────────────
-- 4-1. 집계 + INNER JOIN + UNION ALL
--      장르별 매출 통계 리포트 (합계 행 포함)
-- ──────────────────────────────────────────────────────────
-- 테이블명 : invoice_items, tracks, genres
-- 집합연산자 : UNION ALL 

SELECT 
    g.Name
    , COUNT(DISTINCT ii.InvoiceId)              AS 청구서수
    , SUM(ii.Quantity)                          AS 판매수량
    , ROUND(SUM(ii.UnitPrice * ii.Quantity), 2) AS 총매출
FROM invoice_items ii 
INNER JOIN tracks t ON ii.TrackId = t.TrackId 
INNER JOIN genres g ON t.GenreId = g.GenreId
GROUP BY g.Name

UNION ALL

SELECT '------전체합계' 
       , COUNT(DISTINCT InvoiceId)
       , SUM(Quantity)
       , ROUND(SUM(UnitPrice * Quantity), 2)
FROM invoice_items
;

```

# 계층형 질의

- 5-1

```sql
-- ──────────────────────────────────────────────────────────
-- 5-1. 기본 계층형 질의 - 보고 체계 전체 조회
-- ──────────────────────────────────────────────────────────
WITH RECURSIVE emp_hierarchy(
    EmployeeId, FirstName, LastName, Title, ReportsTo, lvl
) AS (
    -- Anchor: 최상위 직원 (Root)
    SELECT EmployeeId, FirstName, LastName, Title, ReportsTo,
           0 AS lvl
    FROM employees
    WHERE ReportsTo IS NULL

    UNION ALL

    -- Recursive: 직속 부하 반복 탐색
    SELECT e.EmployeeId, e.FirstName, e.LastName,
           e.Title, e.ReportsTo, h.lvl + 1
    FROM employees e
    JOIN emp_hierarchy h ON e.ReportsTo = h.EmployeeId
)
SELECT lvl                                                AS 계층레벨,
       EmployeeId                                         AS 직원ID,
       SUBSTR('                ', 1, lvl * 4)
           || FirstName || ' ' || LastName                AS 직원명,
       Title                                              AS 직책,
       ReportsTo                                          AS 관리자ID
FROM emp_hierarchy
ORDER BY lvl, EmployeeId;

-- ──────────────────────────────────────────────────────────
-- 5-2. 계층형 + 집계 - 직원별 담당 고객 수 포함 조회
-- ──────────────────────────────────────────────────────────
WITH RECURSIVE emp_hier(
    EmployeeId, FirstName, LastName, Title, ReportsTo, lvl
) AS (
    SELECT EmployeeId, FirstName, LastName, Title, ReportsTo, 0 AS lvl
    FROM employees
    WHERE ReportsTo IS NULL

    UNION ALL

    SELECT e.EmployeeId, e.FirstName, e.LastName,
           e.Title, e.ReportsTo, h.lvl + 1
    FROM employees e
    JOIN emp_hier h ON e.ReportsTo = h.EmployeeId
)
SELECT h.lvl        AS 계층레벨,
       h.EmployeeId AS 직원ID,
       SUBSTR('                ', 1, h.lvl * 4)
           || h.FirstName || ' ' || h.LastName AS 직원명,
       h.Title      AS 직책,
       COUNT(c.CustomerId)                     AS 담당고객수,
       ROUND(SUM(i.Total), 2)                  AS 담당매출합계
FROM emp_hier h
LEFT JOIN customers c ON h.EmployeeId = c.SupportRepId
LEFT JOIN invoices  i ON c.CustomerId  = i.CustomerId
GROUP BY h.EmployeeId, h.lvl, h.FirstName, h.LastName, h.Title
ORDER BY h.lvl, h.EmployeeId;

-- ──────────────────────────────────────────────────────────
-- 5-3. 경로(PATH) + 리프(Leaf) 노드 판별
-- ──────────────────────────────────────────────────────────
WITH RECURSIVE emp_path(
    EmployeeId, FirstName, LastName, Title, ReportsTo, lvl, path
) AS (
    SELECT EmployeeId, FirstName, LastName, Title, ReportsTo,
           0,
           FirstName || ' ' || LastName AS path
    FROM employees
    WHERE ReportsTo IS NULL

    UNION ALL

    SELECT e.EmployeeId, e.FirstName, e.LastName,
           e.Title, e.ReportsTo, p.lvl + 1,
           p.path || ' > ' || e.FirstName || ' ' || e.LastName
    FROM employees e
    JOIN emp_path p ON e.ReportsTo = p.EmployeeId
)
SELECT lvl        AS 계층레벨,
       EmployeeId AS 직원ID,
       path       AS 조직경로,
       Title      AS 직책,
       CASE
           WHEN EmployeeId NOT IN (
               SELECT ReportsTo
               FROM employees
               WHERE ReportsTo IS NOT NULL
           ) THEN 'Leaf'
           ELSE 'Branch'
       END AS 노드유형
FROM emp_path
ORDER BY path;

-- ──────────────────────────────────────────────────────────
-- 5-4. 계층형 + UNION ALL - 레벨별 인원 + 전체 합계
-- ──────────────────────────────────────────────────────────
WITH RECURSIVE emp_cte(
    EmployeeId, FirstName, LastName, Title, ReportsTo, lvl
) AS (
    SELECT EmployeeId, FirstName, LastName, Title, ReportsTo, 0
    FROM employees
    WHERE ReportsTo IS NULL

    UNION ALL

    SELECT e.EmployeeId, e.FirstName, e.LastName,
           e.Title, e.ReportsTo, c.lvl + 1
    FROM employees e
    JOIN emp_cte c ON e.ReportsTo = c.EmployeeId
)
SELECT 'Level ' || CAST(lvl AS TEXT) AS 계층레벨,
       COUNT(*)                      AS 직원수
FROM emp_cte
GROUP BY lvl

UNION ALL

SELECT '── 합계', COUNT(*)
FROM emp_cte

ORDER BY 계층레벨;
```

# 0610 수업 정리

- [☀️ 오전 수업 내용 정리 - 보기 / 다운로드](files/260610_오전수업.pdf)
- [🌙 오후 수업 내용 정리 - 보기 / 다운로드](files/260610_오후수업.pdf)

## 수업 내용 필기 첨부 파일

- [0610필기 다운로드](files/0610_필기.txt)
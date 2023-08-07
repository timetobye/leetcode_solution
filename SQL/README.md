LeetCode - SQL 50
-----

LeetCode 에서 제공하는 SQL 50을 풀이한 기록입니다.
- 사용 언어 : MySQL
- LeetCode 에서 정리한 순서대로 풀이를 하였습니다.

### Template

Q.

```sql

```

### Select

Q. 1757. Recyclable and Low Fat Products

```sql
select product_id
from Products
where low_fats = "Y" 
  and recyclable = "Y"
```

Q. 584. Find Customer Referee

```sql
select name
from Customer
where referee_id is null or referee_id != 2
```

학습 내용 from GPT 3.5
- NULL은 데이터베이스에서 값이 없거나 알 수 없는 값을 나타내는 특별한 값입니다. 
- 하지만 NULL은 숫자 0이나 빈 문자열 ""과는 다른 개념이며, 어떤 값과도 동일하지 않습니다. NULL 값은 비교 연산자를 사용할 때 특별한 주의가 필요한데, 이는 SQL에서 NULL과 관련된 3가지 주요 특성 때문입니다.
  - 비교 연산자와 NULL: NULL 값을 비교할 때 주의해야 합니다. 일반적인 숫자나 문자열과 다르게 NULL은 다른 값과 비교했을 때 결과가 항상 "알 수 없음(unknown)"이 됩니다. 예를 들어, NULL = 10 또는 NULL <> 'Hello'과 같은 비교는 모두 "알 수 없음"으로 평가됩니다.
  - 논리 연산자와 NULL: 논리 연산자 (AND, OR, NOT)를 사용할 때도 NULL 값에 주의해야 합니다. 논리 연산자는 NULL 값에 대해 논리적으로 결정을 내릴 수 없으며, 항상 "알 수 없음"을 반환합니다. 예를 들어, NULL AND TRUE는 "알 수 없음"으로 평가됩니다.
  - 집계 함수와 NULL: 평균, 합계, 카운트 등의 집계 함수를 사용할 때 NULL 값이 포함되는 경우도 주의해야 합니다. 집계 함수는 NULL 값을 무시하고 나머지 값들만 처리할 수 있으며, 이로 인해 예상치 못한 결과가 나올 수 있습니다.
- 이렇듯, NULL 값은 다른 값들과 동작이 다른 특수한 값이기 때문에 데이터베이스 쿼리를 작성할 때 NULL에 대한 처리를 명확하게 해야 합니다. IS NULL, IS NOT NULL과 같은 NULL 체크 연산자를 사용하거나 COALESCE() 함수를 사용하여 NULL 값을 다른 값으로 대체하는 등의 방법을 활용하여 적절하게 처리해야 합니다.


Q. 595. Big Countries

```sql
select name, population, area
from world
where area >= 3000000
  or population >= 25000000
```

Q. 1148. Article Views I

```sql
select distinct author_id as id
from Views
where author_id = viewer_id
order by id asc
```

Q. 1683. Invalid Tweets

```sql
select tweet_id
from Tweets
where length(content) > 15
```

### Basic Joins

Q. 1378. Replace Employee ID With The Unique Identifier 

```sql
select unique_id, name
from Employees
left join EmployeeUNI on EmployeeUNI.id = Employees.id
```

Q. 1068. Product Sales Analysis I

```sql
select product_name, year, price
from Sales
left join Product on Product.product_id = Sales.product_id
```

Q. 1581. Customer Who Visited but Did Not Make Any Transactions

```sql
select customer_id, count(customer_id) as count_no_trans
from Visits
left join (
     select distinct visit_id as dist_visit_id
     from Transactions
) as trs on trs.dist_visit_id = Visits.visit_id
where dist_visit_id is null
group by 1
```

Q. 197. Rising Temperature 

이 문제는 Join 으로 풀 수도 있지만, window function 을 쓰는 것이 더 직관적이라고 생각한다.

```sql
select id
from (
     select id, temperature, recordDate
          , lag(temperature) over (order by recordDate asc) as pre_temp
          , lag(recordDate) over (order by recordDate asc) as pre_recordDate
     from Weather
) as base
where temperature > pre_temp
  and pre_temp is not null
  and DATEDIFF(recordDate, pre_recordDate) = 1
```

```sql
select id
from Weather
inner join (
     select temperature as pre_temp
          , date_add(recordDate, interval 1 day) as pre_re_date
     from Weather
) as pre_tb on pre_tb.pre_re_date = Weather.recordDate
where temperature > pre_temp
```

Q. 1661. Average Time of Process per Machine

문제를 똑바로 읽자.

```sql
select machine_id, round(avg(end_timestamp - timestamp), 3) as processing_time
from (
     select machine_id, process_id
          , activity_type, timestamp
          , lead(timestamp) over (
               partition by machine_id, process_id order by activity_type asc
               ) as end_timestamp
     from Activity
) as base
where end_timestamp is not null
group by 1
order by 1
```

```sql
elect machine_id, round(avg(end_ts - timestamp), 3) as processing_time
from (
     select machine_id, process_id, timestamp
     from Activity
     where activity_type = "start"
) as st
inner join (
     select machine_id as end_m_id, process_id as end_p_id, timestamp as end_ts
     from Activity
     where activity_type = "end"
) as end on end.end_m_id = st.machine_id
        and end.end_p_id = st.process_id
group by 1
order by 1
```
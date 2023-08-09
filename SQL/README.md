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

Q. 577. Employee Bonus


```sql
select name, bonus
from Employee
left join Bonus as bns on bns.empId = Employee.empId
where bonus is null or bonus < 1000
order by 1
```

Q. 1280. Students and Examinations

풀이방법
- cross join 을 이용하여 Students, Subjects 를 조인한다.
- 이렇게 하는 이유는 원하는 결과에서 학생과 과목이 1대1이 되는 것을 원하기 때문이다.
- 일부 학생 중에는 시험을 보지 않는 경우도 있는데, 이 경우에 단순하게 inner, left 를 할 경우 과목 목록에서 제외가 된다.
- 그렇기 때문에 기본적으로 cross join 을 이용하여 전체 테이블을 만들고, 그 다음에 examinations 테이블을 별도 집계하여 붙이는 방향으로 처리
- cross join 을 생각 못 해서 조금 고생했다.

```sql
select base.student_id
     , base.student_name
     , base.subject_name
     , IFNULL(attended_exams, 0) as attended_exams
from (
     select student_id, student_name, subject_name
     from Students as st
     cross join Subjects
) as base
left join (
     select student_id, subject_name, count(subject_name) as attended_exams
     from Examinations
     group by 1, 2
) as ex on ex.student_id = base.student_id
       and ex.subject_name = base.subject_name
order by 1, 3
```

Q. 570. Managers with at Least 5 Direct Reports

```sql
select name
from Employee as emp
inner join (
    select managerId, count(*) as cnt
    from Employee
    where 1=1
      and managerId is not null
    group by managerId
    having cnt >= 5
) as cnt_manager on cnt_manager.managerId = emp.id
```

Q. 1934. Confirmation Rate

case when + sum 을 이용하면 비율을 구할 때 쉽고 빠르게 구할 수 있다.
- group by 를 빼먹었는데, IDE 에 너무 익숙해진 것은 아닐련지...

```sql
select sg.user_id
     , round(
          case when total_count is null then 0
               else confirm_count / total_count
          end
     , 2) as confirmation_rate
from Signups as sg
left join (
     select user_id
          , sum(case when action = "confirmed" then 1 else 0 end) as confirm_count
          , count(*) as total_count
     from Confirmations
     group by 1
) as cf on cf.user_id = sg.user_id
order by 1
```

### Basic Aggregate Functions

Q. 620. Not Boring Movies

`MOD` function 을 사용하거나 `%` 를 이용하면 된다.

```sql
select *
from Cinema
where description != "boring"
  and MOD(id, 2) != 0
order by rating desc


select *
from Cinema
where description != "boring"
  and id % 2 != 0
order by rating desc

select *
from Cinema
where description != "boring"
  and id % 2 = 1
order by rating desc
```

`!=` 와 `=` 를 사용하는 것에 대한 차이를 GPT 를 이용하여 확인

Ask > mysql 에서 쿼리 성능 관점에서 != 를 사용하는 것과 = 를 사용하는 것은 어떤 차이가 있니?

MySQL에서 쿼리의 성능을 고려할 때, !=와 =의 사용에 따른 차이가 있을 수 있습니다. 이 두 연산자는 비교 연산을 수행하는 데 사용되며, 성능 측면에서 고려해야 할 몇 가지 점이 있습니다.
- 인덱스 활용 : = 연산자는 인덱스를 최대한 활용하여 검색을 빠르게 할 수 있습니다. 반면에 != 연산자는 부정 연산이라서 인덱스를 효율적으로 활용하지 못할 가능성이 있습니다. 인덱스가 있는 열을 기반으로 조건을 걸 때는 =를 사용하는 것이 일반적으로 더 좋은 성능을 낼 수 있습니다.
- 쿼리 옵티마이저 최적화 : MySQL 옵티마이저는 = 연산자의 경우 일치하는 값을 찾는 데 더 효율적인 방법을 선택할 수 있습니다. 그러나 != 연산자의 경우 인덱스 효율성에 영향을 주기 때문에 조건에 따라 성능이 달라질 수 있습니다.
- 데이터 분포와 크기 : 데이터의 분포와 크기에 따라 != 연산자의 성능이 영향을 받을 수 있습니다. 만약 != 조건이 일반적으로 많은 레코드를 반환한다면 성능에 부정적인 영향을 줄 수 있습니다.
- 인덱스 유무 : =와 != 연산자의 성능은 해당 열에 인덱스가 있는지 여부에 따라 달라질 수 있습니다. 인덱스가 없는 열을 대상으로 연산을 수행하면 테이블을 풀 스캔해야 하므로 성능이 저하될 수 있습니다.
- 일반적으로는 = 연산자가 인덱스 활용과 옵티마이저 최적화 측면에서 더 유리한 경향이 있습니다. 하지만 성능을 평가할 때는 데이터베이스의 스키마, 데이터 분포, 인덱스 구성 등을 고려해야 합니다. 필요한 경우 쿼리 실행 계획을 분석하고, 인덱스를 적절하게 사용하여 성능을 최적화하는 것이 중요합니다.

Q. Average Selling Price

```sql
select UnitsSold.product_id
     , round(sum(price * units) / sum(units), 2) as average_price
from UnitsSold
left join Prices on Prices.product_id = UnitsSold.product_id
                and Prices.start_date <= UnitsSold.purchase_date
                and Prices.end_date >= UnitsSold.purchase_date
group by 1
order by 1

select UnitsSold.product_id
     , round(sum(price * units) / sum(units), 2) as average_price
from UnitsSold
left join Prices on Prices.product_id = UnitsSold.product_id
where Prices.start_date <= UnitsSold.purchase_date
  and Prices.end_date >= UnitsSold.purchase_date                
group by 1
order by 1

-- between 을 사용해도 된다. 가독성 측면
```

Q. 1075. Project Employees I

연산의 최적화를 위해서 avg 를 쓰는 것이 더 낫다.

```sql
select project_id
     , round(avg(experience_years), 2) as average_years
from Project as pj
left join Employee as emp on emp.employee_id = pj.employee_id
group by 1
order by 1


select project_id
     , round(sum(experience_years) / count(pj.employee_id), 2) as average_years
from Project as pj
left join Employee as emp on emp.employee_id = pj.employee_id
group by 1
order by 1
```

Q. 1633. Percentage of Users Attended a Contest

```sql
select contest_id
     , round(100.0 * cnt_user_id / total_user_count, 2) as percentage
from (
     select contest_id
          , count(user_id) as cnt_user_id
     from Register
     group by 1
) as base
cross join (
     select count(user_id) as total_user_count 
     from Users
     ) as usr_cnt
order by percentage desc, contest_id asc

-- 아래와 같이 작성할 수도 있는데, 내가 작성하는 스타일은 아니다.

select contest_id ,round (count(distinct user_id )*100/(select count( user_id )from Users ),2)as percentage from
register
group by contest_id
order by percentage desc , contest_id 
```

Q. 1211. Queries Quality and Percentage

IF를 사용해서 처리 할 수도 있다.

```sql
select query_name
     , round(avg(rating / position), 2) as quality
     , round(100.0 * avg(case when rating < 3 then 1 else 0 end), 2) as poor_query_percentage
from Queries
group by 1
order by 1
```

Q. 1193. Monthly Transactions I

```sql
select date_format(trans_date, "%Y-%m") as month
     , country
     , count(trans_date) as trans_count
     , sum(IF(state="approved", 1, 0)) as approved_count
     , sum(amount) as trans_total_amount
     , sum(IF(state="approved", amount, 0)) as approved_total_amount
from Transactions
group by 1, 2
order by 1, 2, 3 desc
```

Q. 

```sql

```

Q. 

```sql

```


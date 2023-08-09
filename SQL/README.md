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

Q. 1174. Immediate Food Delivery II

```sql
select round(100.0 * sum(IF(first_order_date = pref_date, 1, 0)) / count(customer_id), 2) as immediate_percentage
from(
    select customer_id
        , min(order_date) as first_order_date
        , min(customer_pref_delivery_date) as pref_date
    from Delivery
    group by 1
) as base
```

Q. 550. Game Play Analysis IV

null 을 처리하는 연산을 별도로 해주지는 않았다.
- null 과 연산을 하게 되면 null 로 나오기 때문에 의미를 지니지 않아서 그렇게 한 것이다.
- 그러나 연산 결과가 필요한 것이라면, 별도의 처리를 해줘야 한다.
- 예를 들어 `COALESCE` 또는 `IFNULL` 등을 이용하여 유효한 값으로 대체하고 연산을 해줘야 한다.

```sql
select round(sum(case when datediff(next_loging_event_date, first_login_event_date) = 1 then 1 else 0 end) / count(distinct player_id), 2) as fraction
from (
    select player_id
        , min(event_date) over(partition by player_id order by event_date asc) as first_login_event_date
        , lead(event_date) over(partition by player_id order by event_date asc) as next_loging_event_date
    from Activity
) as base
```

### Sorting and Grouping

Q. 2356. Number of Unique Subjects Taught by Each Teacher

```sql
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by 1
order by 1
```

Q. User Activity for the Past 30 Days I

서버 오류로 문제 페이지가 열리지 않음

```sql

```

Q. 1070. Product Sales Analysis III

문제를 다소 잘못 이해하고 접근하였다.
- 같은 해에 동일 product_id 라도 다른 레코드 값을 가질 수 있는 경우가 있다.
- 왜 이렇게 나올까?
- (sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
- 수량과 가격은 다를 수 있는 것을 간과 하였다.
- 그리고 row_number() 를 사용하는 것 대신에 Rank() 를 사용함으로써 이 문제를 해결하였다.
- Rank() 는 row_number() 와 다르게 중복일 경우 중복은 동일 순위로 처리하고, 다음에 오는 순위는 중복 개수만큼 더해서 순위를 설정
- row_number() 는 중복이 있으면 동일 순위로 처리하지 않고, 다음 순위로 처리를 한다.
- 참고 : https://www.mysqltutorial.org/mysql-window-functions/mysql-row_number-function/
- 참고 : https://www.mysqltutorial.org/mysql-window-functions/mysql-rank-function/
- DENSE_RANK() 의 경우 중복은 동일 순위로 처리하되, 다음에 오는 순위는 바로 다음 숫자로 설정한다.
- 참고 : https://www.mysqltutorial.org/mysql-window-functions/mysql-dense_rank-function/

```bash
| product_id | first_year | quantity | price |
| ---------- | ---------- | -------- | ----- |
| 34         | 1804       | 53       | 5393  |
| 34         | 1804       | 27       | 3767  |
```

```sql
select product_id, year as first_year, quantity, price
from (
    select product_id, year, quantity, price
        , rank() over(partition by product_id order by year asc) as rk_year
    from Sales
) as base
where rk_year = 1
order by product_id;


-- 오답
select product_id, year as first_year, quantity, price
from (
    select product_id, year, quantity, price
        , row_number() over(partition by product_id order by year asc) as rn_year
    from Sales
) as base
where rn_year = 1
order by product_id;

-- 여러 해답
select
    product_id,
    year as first_year,
    quantity,
    price
from Sales
where (product_id, year) in (select product_id, min(year) from Sales group by 1)
```

Q. 596. Classes More Than 5 Students

```sql
select class
from Courses
group by 1
having count(distinct student) >= 5
order by 1
```

Q. 1729. Find Followers Count

```sql
select user_id, count(follower_id) as followers_count
from Followers
group by 1
order by user_id asc
```

Q. 619. Biggest Single Number

```sql
select max(num) as num
from (
    select num
    from MyNumbers
    group by 1
    having count(num) = 1
) as base
```

Q. 1045. Customers Who Bought All Products

```sql
select customer_id
from Customer
group by 1
having count(distinct product_key) = (select count(product_key) from Product)
order by 1
```

### Advanced Select and Joins

Q. 1731. The Number of Employees Which Report to Each Employee

문제를 잘못 이해했음. 그리고 Join 키를 잘못 설정해서 약간의 시간을 소요함
- 어떤 키를 붙일 것인가에 대해서 명시적으로 작성을 해두고 진행을 하자. 그래야 헷갈리지 않는다.

```sql
select reports_to as employee_id
     , mn.name
     , count(distinct emp.employee_id) as reports_count
     , round(avg(age), 0) as average_age 
from Employees as emp
left join (
    select employee_id, name
    from Employees
    group by 1, 2
) as mn on mn.employee_id = emp.reports_to
where reports_to is not null
group by 1, 2
order by 1 asc
```

Q. 문제 서버 오류

```sql

```

Q. 610. Triangle Judgement

삼각형 조건을 찾는데 시간이 더 걸리는 문제

```sql
select x, y, z
     , case when (x + y) > z and (y + z) > x and (z + x) > y then "Yes"
            else "No"
       end as triangle
from Triangle
```


### 


Q. 180. Consecutive Numbers


```sql
-- 풀기는 했으나, 좋지 않은 답
select distinct num as ConsecutiveNums
from (
    select id, num, lag_num, cum_group
        , sum(value) over (partition by cum_group order by id) as result
    from (
        select id, num, lag_num
            , sum(case when lag_num = num then 0 else 1 end) over (order by id) as cum_group
            , 1 as value
        from (
            select id, num
                , IFNULL(lag(num) over(order by id), num) as lag_num
            from Logs
        ) as base
    ) as calc
) as res
where result >= 3

-- 3개 이상이기 때문에 lead, lag 를 이용해서 문제를 해결할 수도 있다. 가운데 있는 것을 기준으로 값 비교 하는 방식
select distinct num as ConsecutiveNums
from (
    select num
        , lead(num) over (order by id) as ld
        , lag(num) over (order by id) as lg
    from logs
) as base
where num = ld and num = lg

-- 테이블을 조인 2번을 더 해서 할 수도 있다.
```

Q. 1164. Product Price at a Given Date

window function 을 사용할 때 RANGE BETWEEN 에 대한 고민을 하지 못 했다.
- `RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` 을 사용하지 않을 경우, 기본값은 `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` 이므로 예상한 답이 안 나올 수 있다.

대부분의 해답들이 union을 쓴 것 같은데, union을 이용한 접근은 생각을 못 했었다.

문제가 생각보다 까다로웠다.

```sql
select pr.product_id, IFNULL(lv, 10) as price
from (
    select product_id, lv
    from (
        select product_id, new_price, change_date
            , LAST_VALUE(new_price) over (
                partition by product_id 
                order by change_date asc
                RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
                ) as lv
        from Products
        where change_date <= "2019-08-16"
    ) as base
    group by 1, 2
) as calc
right join (select distinct product_id from Products) as pr on pr.product_id = calc.product_id
```

Q. 1204. Last Person to Fit in the Bus

Moving Average, Moving Sum 등에 대한 경험이 있으면 쉽게 풀 수 있다.

limit 1은 문제에서 요구하는 바를 쉽게 처리하기 위함이다.

window function 을 사용하지 않을 경우에는 어떻게 해야 할까?
- 기준이 있다고 할 때 그 다음에 오는 모든 것을 붙이는 방식을 취하고
- 기준을 그룹화 해서 그 다음에 오는 모든 것의 합을 구하면 된다.
- 출처 : https://leetcode.com/problems/last-person-to-fit-in-the-bus/solutions/3634727/best-optimum-solution-with-explanation-using-joins/?envType=study-plan-v2&envId=top-sql-50

```sql
select person_name
from (
    select turn, person_name
        , IF(sum(weight) over (order by turn asc) <= 1000, 1, 0) as weight_limit_flag
    from Queue
) as base
where weight_limit_flag = 1
order by turn desc
limit 1


-- Solution From user

# Write your MySQL query statement below
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1
```

```bash
| person_id | person_name | weight | turn | person_id | person_name | weight | turn |
| --------- | ----------- | ------ | ---- | --------- | ----------- | ------ | ---- |
| 5         | Alice       | 250    | 1    | 5         | Alice       | 250    | 1    |
---------------------------- group 1 - totaol sum : 250
| 3         | Alex        | 350    | 2    | 5         | Alice       | 250    | 1    |
| 3         | Alex        | 350    | 2    | 3         | Alex        | 350    | 2    |
---------------------------- group 2 - totaol sum : 600
| 6         | John Cena   | 400    | 3    | 5         | Alice       | 250    | 1    |
| 6         | John Cena   | 400    | 3    | 6         | John Cena   | 400    | 3    |
| 6         | John Cena   | 400    | 3    | 3         | Alex        | 350    | 2    |
---------------------------- group 3 - totaol sum : 950
| 2         | Marie       | 200    | 4    | 5         | Alice       | 250    | 1    |
| 2         | Marie       | 200    | 4    | 2         | Marie       | 200    | 4    |
| 2         | Marie       | 200    | 4    | 3         | Alex        | 350    | 2    |
| 2         | Marie       | 200    | 4    | 6         | John Cena...
---------------------------- group 4 - totaol sum : ....
```

Q. 1907. Count Salary Categories

union all 을 사용하면 된다.
- union all 을 사용하는 이유는 세 가지 경우 중 특정 경우가 빠지게 되면 원하는 답의 형태가 안 나올 수 있어서이다.
- union all : 중복 제거 하지 않음 // union : 중복 제거함
- 중복 제거 작업을 하지 않으므로, union all 이 더 빠르다고 함 : https://jmkim.tistory.com/50
- 근데 꼭 이렇게 풀어야 하나 싶은데, 딱히 방법이 없다.

```sql
select type.category, IFNULL(accounts_count, 0) as accounts_count
from (
    select case when income < 20000 then "Low Salary"
                when income >= 20000 and income <= 50000 then "Average Salary"
                when income > 50000 then "High Salary"
            end as category
        , count(*) as accounts_count
    from Accounts
    group by 1
) as base
right join (
    select "Low Salary" as category
    union all
    select "Average Salary" as category
    union all
    select "High Salary" as category
) as type on type.category = base.category
order by 1
```

Q. 

```sql

```

Q. 

```sql

```

Q. 

```sql

```

Q. 

```sql

```

Q. 

```sql

```







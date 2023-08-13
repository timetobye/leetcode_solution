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

날짜 문자열 해결 방법 확인 할 것

```sql
select activity_date as day, count(distinct user_id) as active_users
from ACtivity
where activity_date > date_sub("2019-07-27", interval 30 day)
  and activity_date <= "2019-07-27"
group by 1
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

Q. 1789. Primary Department for Each Employee

아이디어 접근이 필요한 듯

```sql
select employee_id, department_id
from (
     select employee_id, department_id, primary_flag
          , count(*) over (partition by employee_id) as cnt
     from Employee
) as base
where cnt = 1 or (cnt != 1 and primary_flag ="Y")
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

### Subqueries

Q. 1978. Employees Whose Manager Left the Company

너무 어렵게 생각하면 쉽게 작성할 수 있는 것도 어려워진다.
- 기본적인 접근은 manager_id 가 employee_id에 존재하는지 여부를 어떻게 전개할 것인가이다.
- check 를 하는 방식도 가능은한데, 결국 subquery, join을 몇 번 잡아먹기 때문에 `in` 을 쓰는 것보다 직관성이 떨어진다.

```sql
select employee_id
from (
    select employee_id, manager_id, salary, check_id
    from Employees as emp1
    left join (
        select employee_id as check_id
        from Employees
    ) as emp2 on emp2.check_id = emp1.manager_id
) as base
where salary < 30000
  and check_id is null
  and manager_id is not null
order by 1


select employee_id
from Employees
where salary < 30000
  and manager_id not in (select employee_id from Employees)
order by 1
```

Q. 626. Exchange Seats

두 번째는 다른 사람의 해답을 참고하였다. 결국 id 스위칭이 핵심이고, 연속적인 것이 아이디어를 활용하는데 도움이 된 듯

첫 번째는 그룹을 만들고 그룹내에서 스위칭을 하는 것인데, 결국 서브쿼리가 두 번이나 먹어서, 썩 효율이 좋지 않을 수 있다.

너무 하나의 기능과 함수에 의존 하면 안 될 것 같다.


```sql
select sum(1) over(order by group_number, order_in_group) as id, student
from (
    select id, student, group_number
        , rank() over(partition by group_number order by id desc) as order_in_group
    from (
        select id, student, ceil(id/2) as group_number
        from Seat
    ) as base
) as ord
order by group_number, order_in_group


```조금 더 유연하게 접근하는 방법이다.
select row_number() over(order by new_id) as id, student
from (
    select id, student
        , IF(MOD(id, 2) = 1, id+1, id-1) as new_id
    from Seat
) as base

Q. 

```sql

```

Q. 1341. Movie Rating


```sql
with base as (
    select mr.*, title, name
    from MovieRating as mr
    left join Movies as mv on mv.movie_id = mr.movie_id
    left join Users as us on us.user_id = mr.user_id
)

select name as results
from (
    select user_id, name, count(*) as rate_count
    from base
    group by 1
    order by rate_count desc, name
    limit 1
) as usr

union all

select title as results
from (
    select title, avg(rating) as avg_rating
    from base
    where created_at between "2020-02-01" and "2020-02-28"
    group by 1
    order by avg_rating desc, title
    limit 1
) as mv
```

Q. 1321. Restaurant Growth

`문제 까다로움`

첫 번째 방법 : range BETWEEN interval 6 day preceding and current row
- range 에는 interval 6 day 와 같이 처리가 안 되는 것으로 알고 있었는데, 지원을 해준다.
- https://dev.mysql.com/doc/refman/8.0/en/window-functions-frames.html
- 지원을 해주는 것을 몰랐다면, 풀기 어렵지 않았을까?

두 번째 방법 : 날짜를 미리 생성하고 거기에 맞춘다.
- 이 방법은 날짜 간격이 크면 클수록 비효율성이 커질 것이다.
- 다만 직관적인 방법은 될 수 있다.

```sql


select visited_on, rolling_amount as amount, round(rolling_amount / 7, 2) as average_amount
from (
     select visited_on
          , total_amount
          , min(visited_on) over() as base_visited_on
          , sum(total_amount) over(order by visited_on
          range BETWEEN interval 6 day preceding and current row) as rolling_amount
     from (
          select visited_on, sum(amount) as total_amount
          from customer
          group by 1
     ) as base
) as calc
where visited_on >= date_add(base_visited_on, interval 6 day)
       
---------------------------
with recursive generate_date as (
     select min(visited_on) as generated_date from customer
     union all
     select date_add(generated_date, interval 1 day)
     from generate_date
     where generated_date < (select max(visited_on) from customer)
)

select generated_date as visited_on, rolling_total as amount, round(rolling_total/7, 2) as average_amount
from (
     select generated_date
          , sum(IFNULL(total_amount, 0)) over (
               order by generated_date 
               rows BETWEEN 6 preceding and current row
               ) as rolling_total
          , row_number() over(order by generated_date) as rn
     from generate_date as gd
     left join (
          select visited_on, sum(amount) as total_amount
          from customer
          group by 1
     ) as agg on agg.visited_on = gd.generated_date
) as base
where rn >= 7
order by 1    
```

Q. 602. Friend Requests II: Who Has the Most Friends

서로 받은 것을 합치는 방법으로 계산. 연산이 많이 들어갈 것으로 생각

두 번째 방법은 서로 id가 찍히면 되는 것을 이용해서 하나의 컬럼으로 처리한 다음에 갯수를 확인

```sql
with unique_id as (
     select distinct requester_id as user_id
     from RequestAccepted
     union
     select distinct accepter_id as user_id
     from RequestAccepted     
     ), 
     res_id as (
        select requester_id, count(distinct accepter_id) as res_cnt
        from RequestAccepted
        group by 1
   ),
     acc_id as (
        select accepter_id, count(distinct requester_id) as acc_cnt
        from RequestAccepted
        group by 1
   )


select user_id as id, IFNULL(res_cnt, 0) + IFNULL(acc_cnt, 0) as num
from unique_id
left join res_id on res_id.requester_id = unique_id.user_id
left join acc_id on acc_id.accepter_id = unique_id.user_id
order by num desc
limit 1

--------------------

select id, count(*) as num
from (
     select requester_id as id
     from RequestAccepted

     union all

     select accepter_id as id
     from RequestAccepted
) as base
group by 1
order by num desc
limit 1
```

**매우 중요한 내용**

MySQL의 윈도우 함수에서 RANGE와 ROWS는 윈도우 프레임을 정의하는 데 사용되는 두 가지 다른 옵션입니다. 이들은 윈도우 함수를 어떤 방식으로 적용할지 결정하는 데 영향을 미칩니다.

ROWS 프레임: ROWS 프레임은 로우(행)의 물리적인 순서를 기반으로 윈도우를 정의합니다. 예를 들어, ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING는 현재 로우를 포함하여 이전 로우와 다음 로우까지를 포함하는 윈도우를 만듭니다.

```sql
SELECT value,
       AVG(value) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_avg
FROM your_table;
```

RANGE 프레임: RANGE 프레임은 값의 순서를 기반으로 윈도우를 정의합니다. 값의 순서는 컬럼 데이터 유형에 따라 다르게 해석될 수 있습니다. 예를 들어, RANGE BETWEEN 1000 PRECEDING AND 1000 FOLLOWING는 현재 값에서 1000만큼 떨어진 범위 내의 값들을 포함하는 윈도우를 만듭니다.

    
```sql
SELECT value,
       AVG(value) OVER (ORDER BY date RANGE BETWEEN 7 PRECEDING AND CURRENT ROW) AS moving_avg
FROM your_table;
```

이 두 옵션의 주요 차이점은 윈도우의 정의 방식에 있습니다. ROWS는 로우의 물리적 순서를 기반으로 하며, RANGE는 값의 순서를 기반으로 합니다. 따라서 ROWS를 사용하면 로우의 순서에 따라 프레임을 정의하고, RANGE를 사용하면 값의 순서에 따라 프레임을 정의합니다.


Q. 585. Investments in 2016

영어 해석을 잘못해서 꼬였다. 두 번째 inner join 에 대한 조건이 좀 애매했음

```sql
with base as (
     select lat, lon, count(*) as cnt
     from Insurance
     group by 1, 2
     having cnt <= 1
),    calc as (
     select tiv_2015, count(*) as cnt
     from Insurance
     group by 1
     having cnt >= 2
)

select round(sum(tiv_2016), 2) as tiv_2016
from Insurance as ins
inner join base as bs on bs.lat = ins.lat
                     and bs.lon = ins.lon
inner join calc as cl on cl.tiv_2015 = ins.tiv_2015
```

Q. 185. Department Top Three Salaries

다른 사람의 풀이를 보면 where 절에 서브쿼리를 많이 해두었는데, 개인적으로는 그렇게 하는 스타일이 아니고, 성능적인 이슈도 있을 것으로 본다.

```sql
select Department, Employee, salary
from (
     select dep.name as Department, emp.name as Employee, salary
          , dense_rank() over(partition by departmentId order by salary desc) as rk
     from Employee as emp
     left join Department as dep on dep.id = emp.departmentId
) as base
where rk <= 3
order by 1, 3 desc
```

### Advanced String Functions / Regex / Clause

Q. 1667. Fix Names in a Table

```sql
select user_id, 
     concat(
          upper(left(name, 1)), 
          lower(substring(name, 2))
     ) as name
from Users
order by user_id asc
```

Q. 

```sql
select *
from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'

--- 다른 사람의 해답들
SELECT *
  FROM Patients
 WHERE conditions REGEXP '\\bDIAB1';
```
The expression conditions REGEXP '\\bDIAB1' is actually the same as conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%';, but it is obviously shorter. 😉

The reason they are the same is that \b matches either a non-word character (in our case, a space) or the position before the first character in the string. Also, you need to escape a backslash with another backslash, like so: \\b. Otherwise, the regular expression won't evaluate.

P.S. \b also matches the position after the last character, but it doesn't matter in the context of this problem.


Q. 196. Delete Duplicate Emails

이해를 돕기 위한 설명 자료
- https://leetcode.com/problems/delete-duplicate-emails/solutions/2627589/my-sql-solution/?envType=study-plan-v2&envId=top-sql-50

```sql
-- 이걸로 하면 안 된다. 문제 조건이 select 를 쓰지 말라고 한다.
select min_id as id, email
from (
     select email, min(id) as min_id
     from Person
     group by 1
) as base
order by 1

-- delete 로 접근하는 방법은 해본 적이 없어서 아래 쿼리를 참고하였음
delete p1 from person p1,person p2 
where p1.email=p2.email and p1.id>p2.id;
```

Q. 176. Second Highest Salary

where 조건에 some, any 를 쓰는 것은 잘 하지 않다보니, 접근이 어려웠다.

전체적으로 어려운 쿼리보다는 어떻게 풀어나가느냐를 많이 물어보는 것 같다.

참고
- https://leetcode.com/problems/second-highest-salary/solutions/3855660/beginner-friendly-solution/?envType=study-plan-v2&envId=top-sql-50

```sql
select ifnull(max(salary), null) as secondhighestsalary
from employee
where salary < some(select max(salary) from employee )


select IF(max(ds_rk)=1, null, salary) as SecondHighestSalary
from (
     select salary
          , dense_rank() over(order by salary desc) as ds_rk
     from employee
) as base
where ds_rk = 2

-- 가장 아이디어가 좋은 답?
select
(select distinct Salary 
from Employee order by salary desc 
limit 1 offset 1) 
as SecondHighestSalary;
```

Q. 1484. Group Sold Products By The Date

mysql 에서 제공하는 함수 중 `group_concat`을 이용하면 한 방에 풀 수 있다.

```sql
select sell_date, count(distinct product) as num_sold
     , group_concat(distinct product order by product) as products
from Activities
group by 1
order by 1
```

Q. 1327. List the Products Ordered in a Period

```sql
select product_name, total_unit as unit
from (
     select product_id, DATE_FORMAT(order_date, "%Y-%m") as order_month, sum(unit) as total_unit
     from Orders
     where DATE_FORMAT(order_date, "%Y-%m") = "2020-02"
     group by 1, 2
     having total_unit >= 100
) as base
left join Products on Products.product_id = base.product_id
```

Q. 1517. Find Users With Valid E-Mails

한 번에 처리하는 방법을 떠올리지 못해서, 우선 leetcode.com 부분을 걸러내고 그 후에 도메인 앞부분에 대한 문자열 처리를 진행

정규식 설명 with GPT3.5
- ^: 문자열의 시작을 나타냅니다.
- [A-Za-z]: 문자열의 첫 번째 문자는 알파벳(대문자 또는 소문자)이어야 합니다.
- [A-Za-z0-9_.-]*: 첫 번째 문자 이후에는 알파벳, 숫자, 밑줄 _, 점 . 또는 대시 -가 0회 이상 반복되어야 합니다.
- $: 문자열의 끝을 나타냅니다.

이 정규식을 사용하면 "prefix name"이 주어진 규칙에 따라 문자, 숫자, 밑줄, 점, 대시를 포함하되 첫 번째 문자는 알파벳으로 시작하는지 여부를 판단할 수 있습니다.

```sql
select *
from (
     select *
     from Users
     where mail like '%@leetcode.com'
) as base
where replace(mail, "@leetcode.com", '') REGEXP '^[A-Za-z][A-Za-z0-9_.-]*$'

-- 다른 사람의 해답
elect *
from users
where mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com'
```

정규식 추가 설명 with GPT3.5 

`^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com`를 단계별로 설명한 것입니다.
- ^: 문자열의 시작을 나타냅니다.
- [A-Za-z]: 첫 번째 문자는 알파벳(대문자 또는 소문자)이어야 합니다.
- [A-Za-z0-9_.-]*: 이어지는 문자들은 알파벳, 숫자, 밑줄 _, 점 . 또는 대시 -가 0회 이상 반복될 수 있습니다. 이 부분은 이메일 주소의 로컬 파트에 해당합니다.
- @: 이메일 주소의 로컬 파트와 도메인 파트를 구분하는 "at" 기호입니다.
- leetcode: 정확히 "leetcode"라는 문자열이 도메인 파트의 일부로 포함되어야 합니다.
- [.]: 도메인 파트의 마지막 부분에 오는 마침표 .를 의미합니다. (정규식 내에서 마침표를 일반 문자로 인식시키기 위해 이스케이프 처리)
- com: 도메인 파트의 마지막 부분으로 정확히 "com"이 와야 합니다.
- $: 문자열의 끝을 나타냅니다.

이 정규식은 이메일 주소 형식이 prefix@leetcode.com과 같은 패턴을 따라야 하며, prefix는 알파벳으로 시작하는 문자 및 숫자, 밑줄, 점, 대시로 이루어져야 합니다. 도메인 부분은 정확히 "leetcode.com"이어야 합니다. 이렇게 패턴에 맞는 이메일 주소를 찾아내기 위해 사용하는 정규식입니다.





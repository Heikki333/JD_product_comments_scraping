CREATE TABLE transactions (
    transanction_timestamp varchar(255),
    transaction_id bigint,
    customer_id bigint,
    product_id bigint
)

CREATE TABLE friends (
    friend1_id bigint,
    friend2_id bigint
)

-- Q1
-- number of payments each customer made
 --(I.E. 1 transaction — 100 customers, 2 transactions — 50 customers, etc...)

SELECT transaction_count,
        COUNT(DISTINCT customer_id) AS customer_count
FROM
    (
      SELECT customer_id,
              COUNT(DISTINCT transaction_id) AS transaction_count
      FROM transactions
      GROUP BY customer_id
    ) a
GROUP BY transaction_count

-- Q2 cumulative distribution

SELECT transaction_count,
        sum(customer_count) over (ORDER BY transaction_count ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS customer_cum_count
FROM
(
  SELECT transaction_count,
          COUNT(DISTINCT customer_id) AS customer_count
  FROM
      (
        SELECT customer_id,
                COUNT(DISTINCT transaction_id) AS transaction_count
        FROM transactions
        GROUP BY customer_id
      ) a
  GROUP BY transaction_count
) aa

-- Q3 mutual friends
SELECT COUNT(DISTINCT friend_id) AS num_mutual_friends
FROM
(
SELECT friend2_id as friend_id
FROM friends
WHERE friend1_id = '小明'
INTERSECT
SELECT friend2_id as friend_id
FROM friends
WHERE friend1_id = '小红'
)


SELECT COUNT(DISTINCT a.friend2_id) AS num_mutual_friends
FROM friends a JOIN FROM friends b ON a.friend2_id = b.friend1_id
WHERE a.friend1_id = '小明' and b.friend2_id = '小红'

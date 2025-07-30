
# SQL Query Optimization in Oracle and Teradata

## ✅ General Query Optimization Tips (Both Oracle & Teradata)

1. **SELECT only necessary columns**  
   Avoid `SELECT *`. Fetch only what you need.

2. **Use appropriate WHERE filters**  
   Restrict rows early to reduce data scans.

3. **Use joins wisely**  
   - Prefer `INNER JOIN` over `OUTER JOIN` if possible.
   - Make sure join columns are indexed or part of primary/foreign keys.

4. **Avoid functions on indexed columns in WHERE clause**  
   ❌ `WHERE UPPER(name) = 'JOHN'`  
   ✅ `WHERE name = 'John'` (with `UPPER(name)` pre-processed if needed)

5. **Use EXISTS instead of IN for correlated subqueries** (especially with large sub-lists)

6. **Avoid unnecessary DISTINCT or GROUP BY**

7. **Use bind variables or parameterized queries** to avoid parsing overhead (Oracle)

---

## 🟦 Oracle-Specific Optimization

### 1. **Execution Plan with EXPLAIN PLAN / AUTOTRACE**
```sql
EXPLAIN PLAN FOR
SELECT * FROM your_table WHERE column = 'value';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```

### 2. **Optimizer Hints**
```sql
SELECT /*+ INDEX(your_table your_index) */ ...
```

### 3. **Index Strategies**
- Use **bitmap indexes** for low-cardinality columns.
- Use **function-based indexes** if filtering on `TO_CHAR(date_column, 'YYYY-MM')` etc.

### 4. **Statistics Collection**
```sql
EXEC DBMS_STATS.GATHER_TABLE_STATS('schema', 'your_table');
```

---

## 🟧 Teradata-Specific Optimization

### 1. **Use EXPLAIN always before running complex queries**
```sql
EXPLAIN SELECT * FROM your_table WHERE ...
```

### 2. **Primary Index Selection**
- Primary Index (PI) determines data distribution.
- Choosing a good PI is **crucial for performance**, especially for joins and WHERE clause filtering.

### 3. **Avoid Skew**
- Check if data distribution is skewed on a node.
- Use `COLLECT STATISTICS` on frequently queried columns.

### 4. **Use Volatile/Global Temporary Tables** for staging
```sql
CREATE VOLATILE TABLE temp_tbl AS (
  SELECT ...
) WITH DATA PRIMARY INDEX (id) ON COMMIT PRESERVE ROWS;
```

### 5. **Query Banding** (for workload classification and resource management)
```sql
SET QUERY_BAND = 'Application=ReportApp;User=analyst1;' FOR SESSION;
```

---

## 🧪 Examples of Performance Gains

### Oracle: Rewrite with EXISTS
```sql
-- Slower
SELECT name FROM employees WHERE dept_id IN (SELECT id FROM departments WHERE region = 'EU');

-- Faster
SELECT name FROM employees e WHERE EXISTS (
  SELECT 1 FROM departments d WHERE d.id = e.dept_id AND d.region = 'EU'
);
```

### Teradata: Reduce Data Movement
```sql
-- Use joins on PI to avoid redistribution
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id  -- both should have customer_id as PI
```

---

## 📘 Tools & Tips

| Platform | Tools |
|---------|-------|
| Oracle  | SQL Developer, AWR/ASH Reports, TKPROF, DBMS_XPLAN |
| Teradata | Teradata Studio, EXPLAIN plans, Teradata Viewpoint, Statistics Advisor |


# 🔥 Introduction to Apache Spark

## 🚀 What is Apache Spark?

**Apache Spark** is an **open-source distributed computing system** designed for fast processing of large-scale data.

It provides:
- **In-memory computation**
- **Scalable architecture**
- Support for **batch**, **streaming**, **SQL**, **machine learning**, and **graph processing**

Originally developed at UC Berkeley, it’s now an Apache top-level project and widely used in industry (e.g., Netflix, Uber, Amazon).

---

## 🧱 Core Features

| Feature                | Description |
|------------------------|-------------|
| **Speed**              | Up to 100x faster than Hadoop MapReduce due to in-memory computing |
| **Ease of Use**        | APIs in Python, Java, Scala, and R |
| **Unified Engine**     | One engine for SQL, streaming, ML, and graph data |
| **Distributed Computing** | Automatically handles parallelization and fault tolerance |

---

## 🧠 Spark Ecosystem Components

| Module        | Purpose |
|---------------|---------|
| **Spark Core**       | Base engine for scheduling, memory management, fault recovery |
| **Spark SQL**        | SQL queries on structured data |
| **Spark Streaming**  | Real-time data processing |
| **MLlib**            | Machine Learning at scale |
| **GraphX**           | Graph processing |

---

## 🔄 Key Concepts

### 1. **RDD (Resilient Distributed Dataset)**  
Low-level distributed data structure with fault tolerance and parallel computation.

### 2. **DataFrame**  
High-level abstraction (like a table or pandas DataFrame) with schema support and optimizations via Catalyst engine.

### 3. **SparkSession**  
Entry point for all Spark functionality (since Spark 2.x).

---

## ✍️ Simple Example in Python (PySpark)

```python
from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder.appName("Example").getOrCreate()

# Create DataFrame
data = [("Alice", 28), ("Bob", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show data
df.show()
```

---

## 🛠 Where Spark Shines

✅ Processing **big data**  
✅ **ETL** pipelines  
✅ **Real-time analytics**  
✅ **Machine learning** workflows  
✅ Scalable **data lakes**

---

## 📦 Spark vs Hadoop

| Feature     | Spark                  | Hadoop (MapReduce)        |
|-------------|-------------------------|----------------------------|
| Processing  | In-memory               | Disk-based                |
| Speed       | Fast                    | Slower                    |
| Use cases   | Batch, Streaming, ML    | Mostly batch              |
| APIs        | Rich (SQL, ML, etc.)    | Low-level (Java-heavy)    |

---

## 📚 Learn More

- [Apache Spark Official Docs](https://spark.apache.org/)
- [Databricks Free Community Cloud](https://community.cloud.databricks.com/)
- Books:  
  - *Learning Spark* (O’Reilly)  
  - *Spark: The Definitive Guide*

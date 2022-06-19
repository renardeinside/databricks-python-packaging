# Databricks notebook source
# MAGIC %pip install databricks-python-packaging

# COMMAND ----------

from databricks_python_packaging.utils.common import vertical_append

# COMMAND ----------

tables = [
    spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/region")
    for _ in range(5)
]

appended = vertical_append(tables)

print(f"Single table size: {tables[0].count()}")
print(f"Multiplied (appended) size: {appended.count()}")

# COMMAND ----------

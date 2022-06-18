# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Sample notebook

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Aux steps for auto reloading of dependent files

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Example usage of existing code

# COMMAND ----------

from databricks_python_packaging.workloads.sample_ml_job import SampleMLJob

pipeline = SampleMLJob._get_pipeline()
print(pipeline)

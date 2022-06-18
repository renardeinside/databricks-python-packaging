import logging

from pyspark.sql import SparkSession
from databricks_python_packaging.utils.common import vertical_append


def test_append(spark: SparkSession):
    logging.info("Testing the vertical append function")
    frames = [
        spark.range(100).toDF("id"),
        spark.range(100, 1000).toDF("id"),
        spark.range(1000, 2000).toDF("id"),
    ]
    _count = sum(f.count() for f in frames)
    appended = vertical_append(frames)
    assert appended.count() == _count

"""
This conftest.py contains handy components that prepare SparkSession and other relevant objects.
"""

import logging
import shutil
import tempfile
from pathlib import Path

import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """
    This fixture provides preconfigured SparkSession with Hive and Delta support.
    After the test session, temporary warehouse directory is deleted.
    :return: SparkSession
    """
    logging.info("Configuring Spark session for testing environment")
    warehouse_dir = tempfile.TemporaryDirectory().name
    _builder = SparkSession.builder.master("local[1]").config(
        "spark.hive.metastore.warehouse.dir", Path(warehouse_dir).as_uri()
    )
    spark: SparkSession = _builder.getOrCreate()
    logging.info("Spark session configured")
    yield spark
    logging.info("Shutting down Spark session")
    spark.stop()
    if Path(warehouse_dir).exists():
        shutil.rmtree(warehouse_dir)

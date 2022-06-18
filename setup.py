"""
This file configures the Python package with entrypoints used for future runs on Databricks.

Please follow the `entry_points` documentation for more details on how to configure the entrypoint:
* https://setuptools.pypa.io/en/latest/userguide/entry_point.html
"""

from setuptools import find_packages, setup
from databricks_python_packaging import __version__

setup(
    name="databricks_python_packaging",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    entry_points={
        "console_scripts": [
            "etl = databricks_python_packaging.workloads.sample_etl_job:entrypoint",
            "ml = databricks_python_packaging.workloads.sample_ml_job:entrypoint",
        ]
    },
    version=__version__,
    description="",
    author="",
)

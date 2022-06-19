# databricks-python-packaging

Sample Python project which shows how to package, release and use packages in Databricks.

While using this project, you need Python 3.X and `pip` or `conda` for package management.
Please find the blogpost about this setup [here](https://polarpersonal.medium.com/releasing-and-using-python-packages-with-azure-devops-and-azure-databricks-906ec2ff8e2d).

## Technologies used

* Azure Databricks
* Azure DevOps
* Azure Artifacts

## Local environment setup

1. Instantiate a local Python environment via a tool of your choice. This example is based on `conda`, but you can use any environment management tool:
```bash
conda create -n databricks_python_packaging python=3.9
conda activate databricks_python_packaging
```

2. If you don't have JDK installed on your local machine, install it (in this example we use `conda`-based installation):
```bash
conda install -c conda-forge openjdk
```

3. Install unit requirements for local development and the project package in a developer mode:
```bash
pip install -r unit-requirements.txt
pip install -e .
```

## Running unit tests

For unit testing, please use `pytest`:
```
pytest tests/unit --cov
```

Please check the directory `tests/unit` for more details on how to use unit tests.
In the `tests/unit/conftest.py` you'll also find useful testing primitives.

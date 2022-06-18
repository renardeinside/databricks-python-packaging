from typing import List

from pyspark.sql import DataFrame
from functools import reduce


def vertical_append(frames: List[DataFrame]) -> DataFrame:
    """
    Vertically assembles (appends) a list of Spark Data Frames.
    All frames are expected to have same columns.
    :param frames: list of Spark Data Frames
    :return: Data Frame
    """
    return reduce(DataFrame.unionAll, frames)

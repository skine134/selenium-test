from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.getOrCreate()

def array2df(arr=[]):
    row_arr = map(lambda item:Row(item),arr)
    df = spark.createDataFrame(row_arr)
    return df
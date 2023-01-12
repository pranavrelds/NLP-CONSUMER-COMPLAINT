
from pyspark.sql import SparkSession

spark_session = SparkSession.builder.master('local[*]').appName('consumer_complaint') \
    .config("spark.executor.instances", "2") \
    .config("spark.executor.memory", "8g") \
    .config("spark.driver.memory", "8g") \
    .config("spark.executor.memoryOverhead", "8g") \
    .getOrCreate()
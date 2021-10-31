from pyspark.sql import SparkSession
import sys

spark = SparkSession.builder.appName("A3T1").getOrCreate()

df = spark.read.option("header",True).csv(sys.argv[2])
count=sys.argv[1]

rdd1=df.filter(df.Country.contains(count))

rdd2=rdd1.map(df.City,df.AverageTemperature)

rdd3=rdd1.groupBy('City').mean('AverageTemperature').collect()




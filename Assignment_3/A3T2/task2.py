from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType
from pyspark.sql.functions import countDistinct
from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys

sc = SparkContext()
sqlContext = SQLContext(sc)

spark = SparkSession.builder.appName("A3T2").getOrCreate()

city_df = spark.read.option("header",True).csv(sys.argv[1])
global_df = spark.read.option("header",True).csv(sys.argv[2])

city_df= city_df.withColumn("AverageTemperature", city_df["AverageTemperature"].cast(DoubleType()))
global_df= global_df.withColumn("LandAverageTemperature", global_df["LandAverageTemperature"].cast(DoubleType()))

cond= [city_df["dt"]==global_df["dt"], city_df["AverageTemperature"] > global_df["LandAverageTemperature"]]
res= city_df.join(global_df, cond, "inner").select(city_df.Country, city_df.dt)

res2= res.groupBy("Country").agg(countDistinct("dt")).collect()
res2.sort()
for row in res2:
	print(row[0],"\t",row[1])


from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType
from pyspark.sql.functions import avg
from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys

sc =SparkContext()
sqlContext = SQLContext(sc)

spark = SparkSession.builder.appName("A3T1").getOrCreate()

df = spark.read.option("header",True).csv(sys.argv[2])
countr=sys.argv[1]

rdd1=df.filter(df.Country.contains(countr))
rdd1= rdd1.withColumn("AverageTemperature", df["AverageTemperature"].cast(DoubleType()))

cityList=rdd1.groupBy("City").avg("AverageTemperature")
#cityList.show()
#cityList.sort(key= lambda x: x[0])
rdd1= rdd1.orderBy(rdd1.City)

cond= [rdd1["AverageTemperature"] > cityList["avg(AverageTemperature)"], rdd1["City"] == cityList["City"] ]
res= rdd1.join(cityList, cond , "inner").select(rdd1.City).groupBy("City").count().collect()
res.sort()
for row in res:
	print (row[0],"\t",row[1])


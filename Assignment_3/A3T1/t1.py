from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
#from pyspark.sql import Window
import sys

spark = SparkSession.builder.appName("A3T1").getOrCreate()

df = spark.read.option("header",True).csv(sys.argv[2])
count=sys.argv[1]

rdd1=df.filter(df.Country.contains(count))
rdd1= rdd1.withColumn("AverageTemperature", df["AverageTemperature"].cast(IntegerType()))

cityList=rdd1.groupBy("City").mean("AverageTemperature").collect()

rdd1= rdd1.orderBy(rdd1.City).collect()
cityList.sort(key= lambda x: x[0])
#print(rdd1, "\n\n", cityList)

cc= 0
count=0
prevCity= None 

for row in rdd1:
	if(prevCity == row[3] or prevCity == None ):	
		try:
			if( row[1] > cityList[cc][1]):
				count+=1
			prevCity= row[3]
		except:
			prevCity= row[3]
			continue
		
	else:
		if(count!=0):
			print(prevCity,"\t", count)
			
		cc+=1
		prevCity= row[3]

		try:
			if( row[3] > cityList[cc][1] ):
				count=1
			else:
				count =0

		except:
			count=0
	
if(count!=0):
	print(prevCity,"\t", count)
		
	
	





	


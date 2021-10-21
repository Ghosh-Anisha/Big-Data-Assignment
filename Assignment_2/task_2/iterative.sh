#! /bin/sh

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave 

hdfs dfs -rm -r /Assignment2/Input
hdfs dfs -rm -r /Assignment2/output
hdfs dfs -rm -r /Assignment2
hdfs dfs -mkdir /Assignment2
hdfs dfs -mkdir /Assignment2/Input
hdfs dfs -mkdir /Assignment2/output
hdfs dfs -put /home/pes1ug19cs167/Desktop/A2T1/dataset-sample.txt /Assignment2/Input
chmod +x mapper.py reducer.py
dos2unix mapper.py reducer.py

hadoop jar /home/pes1ug19cs167/hadoop-3.2.2/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes1ug19cs167/Desktop/A2T1/mapper.py'" \
-reducer "'/home/pes1ug19cs167/Desktop/A2T1/reducer.py' '/home/pes1ug19cs167/Desktop/A2T1/v' " \
-input /Assignment2/Input \
-output /Assignment2/output/o1t1

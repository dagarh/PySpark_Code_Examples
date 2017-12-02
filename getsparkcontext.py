import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("Application")
sc = SparkContext(conf=conf)

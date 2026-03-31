from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ADF_ELT").getOrCreate()

df = spark.read.format("parquet").load("/mnt/raw/orders")

customer_sales = df.groupBy("customer_id").sum("order_amount")

customer_sales.write \
.format("delta") \
.mode("overwrite") \
.save("/mnt/gold/customer_sales")

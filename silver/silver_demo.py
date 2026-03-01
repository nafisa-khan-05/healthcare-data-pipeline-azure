from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create spark session
spark = SparkSession.builder.appName("SilverLayer").getOrCreate()

# Read Bronze data
df_bronze = spark.read.parquet("bronze/patient")

# Data Cleaning
df_clean = df_bronze.filter(col("age").isNotNull()) \
                     .filter(col("age") > 0)

# Show cleaned data
df_clean.show()

# Write to Silver Layer
df_clean.write.mode("overwrite").parquet("silver/patient")

print("Silver layer transformation completed.")

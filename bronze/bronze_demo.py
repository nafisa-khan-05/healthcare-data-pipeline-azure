from pyspark.sql import SparkSession

# create spark session
spark = SparkSession.builder.appName("BronzeLayer").getOrCreate()

# Read raw JSON data
df_raw = spark.read.json("data/patient.json")

# Show Raw data (for testing)
df_raw.show()

# Write to Bronze Layer (parquet format)
df_raw.write.mode("overwrite").parquet("bronze/patient")

print("Bronze layer data stored successfully.")

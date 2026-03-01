from pyspark.sql import SparkSession
form pyspark.sql.funtions import count,avg,col

# Create Spark Session
spark = SparkSession.builder.appName("GoldLayer").getOrCreate()

# Read Silver data
df_silver = spark.read.parquet("silver/patient")

# KPI 1: Total Patients
total_patients = df_silver.count()

# KPI 2: Average Age
average_age = df_silver.select(avg("age")).collect()[0][0]

#KPI 3: Disease Distribution
disease_count = df_silver.groupBy("disease").count()

print(f"Total Patients: {total_patients}")
print(f"Average Age: {average_age}")

disease_count.show()

# Write Gold data (optional aggregated table)
df_silver.write.mode("overwrite").parquet("gold/patient_kpi")

print("Gold layer KPI calculation completed.")

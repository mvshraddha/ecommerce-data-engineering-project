import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import col

# Initialize Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read JSON from S3
users_df = spark.read.json("s3://ecommerce-data-shraddha/raw/users/")

# Select required fields
users_clean = users_df.select(
    col("id").alias("user_id"),
    col("email"),
    col("username")
)

# Write to S3 (Parquet)
users_clean.write.mode("overwrite").parquet(
    "s3://ecommerce-data-shraddha/processed/users/"
)

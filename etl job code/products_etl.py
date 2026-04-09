import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import col

# Initialize Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read JSON directly from S3 (NO crawler)
products_df = spark.read.json("s3://ecommerce-data-shraddha/raw/products/")

# Select and clean columns
products_clean = products_df.select(
    col("id").alias("product_id"),
    col("title"),
    col("price"),
    col("category")
)

# Write as Parquet to processed layer
products_clean.write.mode("overwrite").parquet(
    "s3://ecommerce-data-shraddha/processed/products/"
)

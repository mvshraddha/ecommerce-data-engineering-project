import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import col, explode

# Initialize Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read JSON from S3
carts_df = spark.read.json("s3://ecommerce-data-shraddha/raw/carts/")

# Explode products array
carts_exploded = carts_df.select(
    col("id").alias("cart_id"),
    col("userId").alias("user_id"),
    explode(col("products")).alias("product")
)

# Flatten structure
carts_clean = carts_exploded.select(
    col("cart_id"),
    col("user_id"),
    col("product.productId").alias("product_id"),
    col("product.quantity")
)

# Write to S3
carts_clean.write.mode("overwrite").parquet(
    "s3://ecommerce-data-shraddha/processed/carts/"
)

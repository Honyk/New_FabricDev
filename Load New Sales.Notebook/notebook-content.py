# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "3a065bff-8960-4af3-a1b9-956a623d8e72",
# META       "default_lakehouse_name": "LH",
# META       "default_lakehouse_workspace_id": "c17c1f7b-110a-4909-92d6-dfd520dd52a7",
# META       "known_lakehouses": [
# META         {
# META           "id": "2a8239b4-01fa-4b70-96c6-ee25dbdcbba9"
# META         },
# META         {
# META           "id": "3a065bff-8960-4af3-a1b9-956a623d8e72"
# META         }
# META       ]
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

table_name = "new_sales"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import *

# Read the new sales data
df = spark.read.format("csv").option("header","true").load("Files/new_data/*.csv")

## Add month and year columns
df = df.withColumn("Year", year(col("OrderDate"))).withColumn("Month", month(col("OrderDate")))

# Derive FirstName and LastName columns
df = df.withColumn("FirstName", split(col("CustomerName"), " ").getItem(0)).withColumn("LastName", split(col("CustomerName"), " ").getItem(1))

# Filter and reorder columns
df = df["SalesOrderNumber", "SalesOrderLineNumber", "OrderDate", "Year", "Month", "FirstName", "LastName", "EmailAddress", "Item", "Quantity", "UnitPrice", "TaxAmount"]

# Load the data into a table
df.write.format("delta").mode("append").saveAsTable(table_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

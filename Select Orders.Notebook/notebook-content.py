# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2a8239b4-01fa-4b70-96c6-ee25dbdcbba9",
# META       "default_lakehouse_name": "first_lakehouse",
# META       "default_lakehouse_workspace_id": "c17c1f7b-110a-4909-92d6-dfd520dd52a7",
# META       "known_lakehouses": [
# META         {
# META           "id": "2a8239b4-01fa-4b70-96c6-ee25dbdcbba9"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC select count(*) from orders

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

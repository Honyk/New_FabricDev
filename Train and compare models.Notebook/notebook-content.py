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

# MARKDOWN ********************

# # Train a machine learning model and track with MLflow
# 
# Use the code in this notebook to train and track models.


# CELL ********************



import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/" + "Files/churn.csv"
df = pd.read_csv("/lakehouse/default/" + "Files/churn.csv")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from sklearn.model_selection import train_test_split

print("Splitting data...")
X, y = df[['years_with_company','total_day_calls','total_eve_calls','total_night_calls','total_intl_calls','average_call_minutes','total_customer_service_calls','age']].values, df['churn'].values
   
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import mlflow
experiment_name = "experiment-churn"
mlflow.set_experiment(experiment_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from sklearn.linear_model import LogisticRegression
   
with mlflow.start_run():
    mlflow.autolog()

    model = LogisticRegression(C=1/0.1, solver="liblinear").fit(X_train, y_train)

    mlflow.log_param("estimator", "LogisticRegression")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from sklearn.tree import DecisionTreeClassifier
   
with mlflow.start_run():
    mlflow.autolog()

    model = DecisionTreeClassifier().fit(X_train, y_train)
   
    mlflow.log_param("estimator", "DecisionTreeClassifier")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import mlflow
experiments = mlflow.search_experiments()
for exp in experiments:
    print(exp.name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

experiment_name = "experiment-churn"
exp = mlflow.get_experiment_by_name(experiment_name)
print(exp)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

mlflow.search_runs(exp.experiment_id)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

mlflow.search_runs(exp.experiment_id, order_by=["start_time DESC"], max_results=2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import matplotlib.pyplot as plt
   
df_results = mlflow.search_runs(exp.experiment_id, order_by=["start_time DESC"], max_results=2)[["metrics.training_accuracy_score", "params.estimator"]]
   
fig, ax = plt.subplots()
ax.bar(df_results["params.estimator"], df_results["metrics.training_accuracy_score"])
ax.set_xlabel("Estimator")
ax.set_ylabel("Accuracy")
ax.set_title("Accuracy by Estimator")
for i, v in enumerate(df_results["metrics.training_accuracy_score"]):
    ax.text(i, v, str(round(v, 2)), ha='center', va='bottom', fontweight='bold')
plt.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# Azure Data Factory ELT Pipeline

SQL Database → Azure Data Factory → ADLS Gen2 → Databricks → Delta Lake

## Overview

This project demonstrates an end-to-end **ELT data pipeline on Azure**.
Data is extracted from a SQL database, loaded into **Azure Data Lake Storage Gen2** using **Azure Data Factory**, and transformed in **Azure Databricks** using PySpark. The final aggregated data is stored in **Delta Lake** for analytics and reporting.

## Architecture

SQL Database
→ Azure Data Factory Pipeline
→ Azure Data Lake Storage Gen2 (Raw Data)
→ Azure Databricks (PySpark Transformations)
→ Delta Lake (Gold Layer)

## Tech Stack

* Azure Data Factory
* Azure Data Lake Storage Gen2
* Azure Databricks
* PySpark
* Delta Lake
* SQL

## Repository Structure

```
azure-adf-databricks-elt-pipeline
│
├── adf_pipeline
│   └── pipeline.json
├── databricks_notebooks
│   └── transform_data.py
├── sql_scripts
│   └── source_tables.sql
├── datasets
│   └── orders_sample.csv
├── delta_tables
│   └── gold_tables.sql
└── README.md
```

## Dataset

The project uses a sample **e-commerce orders dataset** containing:

* order_id
* customer_id
* product
* order_amount
* order_date

Only a small sample dataset is included in the repository.

## Transformation Logic

The Databricks job reads raw order data from the data lake and calculates **total sales per customer**.

Example transformation:

```python
customer_sales = df.groupBy("customer_id").sum("order_amount")
```

The result is stored in a **Delta Lake table** for downstream analytics.

## Example Output

| customer_id | total_sales |
| ----------- | ----------- |
| 501         | 1500        |
| 502         | 170         |
| 503         | 25          |

## Use Cases

This architecture is commonly used for:

* building cloud data lakes
* ELT pipelines in Azure
* enterprise analytics platforms
* BI and reporting pipelines

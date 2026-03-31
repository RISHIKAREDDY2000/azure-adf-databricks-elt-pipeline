# Azure Data Factory ELT Pipeline

SQL Database → ADLS → Databricks → Delta Lake

## Overview

This project demonstrates a cloud-based ELT pipeline built using Azure services. Data is extracted from a SQL database, loaded into Azure Data Lake Storage using Azure Data Factory, and transformed in Azure Databricks using PySpark.

The processed data is stored in Delta Lake tables for analytics and reporting.

## Architecture

SQL Database
→ Azure Data Factory Pipeline
→ Azure Data Lake Storage Gen2
→ Azure Databricks
→ Delta Lake

## Tech Stack

Azure Data Factory
Azure Data Lake Storage Gen2
Azure Databricks
PySpark
Delta Lake
SQL

## Pipeline Workflow

1. Orders data is stored in a SQL database.
2. Azure Data Factory copies data into Azure Data Lake Storage.
3. Databricks reads raw data from the data lake.
4. PySpark transformations aggregate customer sales.
5. Results are stored in Delta Lake tables.

## Use Cases

Cloud data lake ingestion pipelines
Retail analytics platforms
Azure-based ELT architectures

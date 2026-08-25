RetailWorks Data Warehouse and Analytics Project (Databricks + PySpark Edition)

Welcome to the RetailWorks Data Warehouse and Analytics Project! 🚀 This project demonstrates a comprehensive data warehousing and analytics solution, from building a data warehouse to generating actionable insights — built entirely on Databricks Free Edition using PySpark and Delta Lake, so no cloud account is required. Designed as a portfolio project, it highlights industry best practices in data engineering and analytics, going a step further than the classic SQL Server version by including SCD Type 2 history tracking.

🏗️ Data Architecture

This project follows the Medallion Architecture — Bronze, Silver, and Gold layers:
Source Systems (CRM, ERP, Orders)
        │
        ▼
   BRONZE LAYER    — raw data ingested as-is from CSV source files via Autoloader (incremental)
        │
        ▼
   SILVER LAYER    — cleansed, standardized, deduplicated data
        │
        ▼
   GOLD LAYER      — business-ready Star Schema (Fact + Dimension tables) for reporting

--Bronze Layer: Stores raw data as-is from source systems. Data is ingested from CSV files (simulating CRM, ERP, and Orders systems) into Unity Catalog Delta tables using Autoloader.
--Silver Layer: Includes data cleansing, standardization, validation, and deduplication to prepare data for analysis.
--Gold Layer: Houses business-ready data modeled into a Star Schema, including SCD Type 2 history tracking on the Customer dimension.

📖 Project Overview
This project involves:
Data Architecture: Designing a modern data warehouse using Medallion Architecture (Bronze, Silver, Gold) on Databricks.
ETL Pipelines: Extracting, transforming, and incrementally loading data from simulated source systems using PySpark and Autoloader.
Data Modeling: Developing fact and dimension tables optimized for analytical queries, including SCD Type 1 and Type 2 dimensions.
Analytics & Reporting: Writing Spark SQL–based business queries against the Star Schema for actionable insights.

🎯 This repository is a resource for showcasing expertise in:

PySpark & Spark SQL Development
Data Engineering (Databricks, Delta Lake, Unity Catalog)
ETL Pipeline Development (Autoloader, incremental loading)
Dimensional Data Modeling (Star Schema, SCD)
Data Analytics & Reporting

🛠️ Important Links & Tools (All Free)
--Databricks Free Edition: databricks.com/learn/free-edition — no cloud account or credit card needed
--Unity Catalog: Pre-configured automatically in Free Edition for governance
--Git Repository: GitHub account + repo for version control and portfolio visibility
--Draw.io: For designing the architecture, star schema, and data flow diagrams

🚀 Project Requirements
Building the Data Warehouse (Data Engineering)

Objective: Develop a modern data warehouse using Databricks and PySpark to consolidate sales data, enabling analytical reporting and informed decision-making.

Specifications:

Data Sources: Import data from two simulated source systems (CRM and ERP) plus a transactional Orders source, provided as CSV files.
Data Quality: Cleanse and resolve data quality issues prior to analysis (nulls, duplicates, invalid values).
Integration: Combine all sources into a single, user-friendly dimensional model designed for analytical queries.
Scope: Unlike the base SQL Server version, this project does implement historization — DimCustomer uses SCD Type 2 to track change history; DimProduct uses SCD Type 1.
Documentation: Clear documentation of the data model (this file + a data catalog) to support both business stakeholders and analytics teams.
BI: Analytics & Reporting (Data Analysis)

Objective: Develop Spark SQL–based analytics delivering insights into:

Customer Behavior (by segment, by city)
Product Performance (by category, by revenue)
Sales Trends (by month, by quarter)

📂 Repository Structure
retailworks-dwh-project/
│
├── datasets/                           # Simulated raw datasets (CRM, ERP, Orders CSVs)
│
├── docs/                                # Project documentation and architecture details
│   ├── data_architecture.drawio         # Diagram of the Bronze/Silver/Gold architecture
│   ├── data_flow.drawio                 # Diagram of the end-to-end data flow
│   ├── data_models.drawio               # Star schema diagram (Fact + Dimension tables)
│   ├── data_catalog.md                  # Catalog of tables, fields, and descriptions
│   ├── naming_conventions.md            # Naming guidelines for tables, columns, and files
│
├── notebooks/                           # PySpark notebooks for ETL and transformations
│   ├── 01_generate_sample_data.py       # Creates simulated CRM/ERP/Orders source files
│   ├── 02_bronze_ingestion.py           # Autoloader incremental ingestion into Bronze
│   ├── 03_silver_transform.py           # Cleansing and standardization into Silver
│   ├── 04_gold_dim_customer_scd2.py     # DimCustomer build with SCD Type 2
│   ├── 05_gold_dim_product.py           # DimProduct build with SCD Type 1
│   ├── 06_gold_dim_date.py              # DimDate build
│   ├── 07_gold_fact_sales.py            # FactSales build (Star Schema grain: one row per order line)
│
├── tests/                                # Data quality and validation scripts
│   └── data_quality_checks.py           # Referential integrity & completeness checks
│
├── README.md                             # Project overview and instructions (this file)
├── LICENSE                               # License information for the repository
└── .gitignore                            # Files and directories excluded from Git




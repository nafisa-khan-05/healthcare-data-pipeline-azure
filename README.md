# Healthcare Data Analytics Pipeline (Azure)

## Project Overview
This project demonstrates an end-to-end healthcare data pipeline built using Azure Data Factory and Azure Databricks following Medallion Architecture (Bronze, Silver, Gold).

This pipeline processes patient data to generate business KPIs for clinical, operational and financial reporting.

## Architecture Flow
REST API / JSON Data  
        ↓  
Azure Data Factory (Orchestration)  
        ↓  
ADLS Gen2 (Bronze Layer - Raw Data)  
        ↓  
Azure Databricks (PySpark Transformation)  
        ↓  
Silver Layer (Cleaned & Structured Data)  
        ↓  
Gold Layer (KPI Tables & Reporting)

## Technologies Used
- Azure Data Factory
- Azure Databricks
- PySpark
- ADLS Gen2
- Unity Catalog
- Medallion Architecture

## Sample KPIs Generated
- Total Patients
- Average Patient Age
- Disease Distribution
- Claim Approval Rate
- Revenue by Insurance Provider

# 🛒 RetailPulse — Retail Analytics & Inventory Risk Management

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811.svg)](https://powerbi.microsoft.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Chunked_Processing-150458.svg)](https://pandas.pydata.org/)
[![Scale](https://img.shields.io/badge/Dataset_Scale-~10M_Records-brightgreen.svg)]()

> **Zidio Internship Project**  
> **Developed By:** Hemant Kakde  
> **Tech Stack:** Python (Pandas, NumPy, Matplotlib) & Power BI (DAX, Star Schema Modeling)

---

## 📌 Project Overview

**RetailPulse** is an enterprise-scale retail business intelligence and inventory analytics solution designed to extract actionable insights from multi-source retail datasets. The project bridges large-scale data engineering with executive business intelligence:
- **Python Pipeline:** Ingests nearly **10 million transaction rows**, performs data quality audits, missing value/duplicate handling, feature engineering, and exploratory data analysis (EDA).
- **Power BI Data Engine:** Implements a normalized **Star Schema**, separates transaction and inventory grains, computes business KPIs using custom **DAX measures**, and delivers **10 interactive analytical dashboard pages**.

---

## 🔗 External Assets & Large Files (Google Drive)

Because the raw transactional dataset (~2.4 GB uncompressed) and the compiled Power BI analytical model (`.pbix` ~245 MB) exceed standard GitHub file size limits, they are hosted securely on Google Drive[cite: 1]:

* 📁 **[Access All Project Assets on Google Drive](https://drive.google.com/drive/u/0/folders/1dL3_TOwIdR4jTgGJxcnTY94iWh1zFQXY)**
  * **Power BI Production File (`.pbix`):** Pre-built star schema model containing all 10 dashboard views and DAX metrics.
  * **Source Data Archive:** Full source files including transactions, product master, customer master, store master, and inventory logs.
  * **Demonstration Videos:** Full project walkthrough demo and evaluation feedback recordings.

---

## 🏗️ Architecture & Analytical Workflow

```text
SOURCE DATA (CSV Files)
  ├── sales_transactions.csv (~9.97M rows)
  ├── sku_master.csv (5,000 SKUs)
  ├── customer_master.csv (10,000 Customers)
  ├── store_master.csv (30 Stores)
  ├── promotions.csv (100 Campaigns)
  └── inventory_snapshot.csv & sku_inventory_flags.csv
       │
       ▼
PYTHON ENGINE (Pandas / NumPy)
  ├── Inspection (shape, head(), info(), describe())
  ├── Validation (zero-quantity audits, duplicate detection, promo handling)
  ├── Datetime Feature Preparation (Year, Month, Quarter, Day Name)
  └── Exploratory Data Analysis (EDA Charts)
       │
       ▼
POWER BI DATA MODEL (Star Schema)
  ├── Fact: SalesF
  ├── Separate Grain: Inventory_snapshot_F & Inventory_flags
  └── Dimensions: ProductD, CustomerD, StoreD, DateD, PromotionD
       │
       ▼
DAX BUSINESS LOGIC & KPI ENGINE
  ├── Core Metrics: Revenue, Orders, Units, Customers, AOV
  └── Profitability Metrics: Total Cost, Gross Profit, Profit Margin %
       │
       ▼
10 INTERACTIVE EXECUTIVE DASHBOARDS

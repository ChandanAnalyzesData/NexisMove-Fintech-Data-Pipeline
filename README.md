# NexisMove-Fintech-Data-Pipeline
An end-to-end data analytics pipeline tracking peer-to-peer transaction risks, data degradation, and financial metrics for a mock Fintech platform using Google Sheets, SQL, Python, and Power BI.

# NexisMove: Fintech Data Analytics & Risk Pipeline

## 📌 Project Overview
NexisMove is a mock peer-to-peer (P2P) digital wallet application. This portfolio project simulates the real-world workflow of a Fintech Data Analyst. The objective is to ingest chaotic, real-world operational transactional data, build a structural cleaning pipeline, query the data for risk metrics, and serve an interactive financial dashboard.

## 🛠️ Tech Stack & Architecture
* **Data Sourcing & Prototyping:** Google Sheets (Handling data schema discovery)
* **Database Ingestion:** SQL / SQLite (Relational modeling, Joins, and filtering)
* **Data Sanitization & Engineering:** Python & Pandas (Data types, deduplication, handling missing records)
* **Business Intelligence:** Power BI (Building executive dashboards and TPV metrics)

## 📁 Repository Structure
* `/data/raw/`: Original transactional datasets with operational anomalies.
* `/data/processed/`: Clean, production-ready outputs.
* `/scripts/`: Python automation and cleaning scripts.
* `/queries/`: SQL scripts for risk analysis.
* `/dashboards/`: Power BI visual configurations.

## 📈 Daily Progress Log
* **Day 1:** Established relational schemas and created raw spreadsheet tracking anomalies.

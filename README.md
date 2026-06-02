# Healthcare Claims Analytics

## Project Overview
This project analyzes healthcare claims data to identify data quality issues, missing provider IDs, billing anomalies, and claim approval trends.

## Business Problem
Healthcare organizations process thousands of claims daily. Missing provider IDs, duplicate records, and unusual billing amounts can delay audits, increase financial risk, and reduce reporting accuracy.

## Tools Used
- Python
- Pandas
- SQL logic
- Data validation
- Anomaly detection
- KPI reporting

## Key Features
- Detects missing provider IDs
- Flags high-value billing anomalies
- Calculates claim approval and rejection rates
- Generates provider-level KPI summaries
- Exports cleaned claims data and anomaly reports

## Project Structure
```text
healthcare-claims-analytics/
│── data/
│   └── sample_claims.csv
│── src/
│   └── claims_analysis.py
│── README.md
│── requirements.txt
```

## How to Run
```bash
pip install -r requirements.txt
python src/claims_analysis.py
```

## Outputs
The script creates:
- cleaned_claims.csv
- anomaly_claims.csv
- provider_kpi_summary.csv

## Skills Demonstrated
- Data cleaning
- Healthcare data analysis
- KPI reporting
- Python analytics
- Business problem solving

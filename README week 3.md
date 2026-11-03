# Week 3: Advanced Data Analysis and Visualization in Logistics

## Project overview
This project uses a **hypothetical, simulated logistics dataset** of 600 shipments to demonstrate exploratory data analysis (EDA), statistical summaries, and visual analytics.

## Files
- `logistics_dataset.csv` – simulated shipment records.
- `week3_exploratory_data_analysis.py` – Python script to perform EDA and regenerate charts.
- `Week3_Logistics_Analysis_Report.docx` – detailed internship report.
- `visualizations/` – six generated charts.
- `requirements.txt` – Python dependencies.

## Dataset variables
Shipment ID, shipment date, warehouse, distance, shipment volume, delivery time, fuel cost, transportation cost, and delivery status.

## Setup and run
```bash
pip install -r requirements.txt
python week3_exploratory_data_analysis.py
```

The script expects `logistics_dataset.csv` in the same folder and saves charts under `visualizations/`.

## Main sample findings
- Records analysed: 600
- Delayed shipments: 15.5%
- Mean delivery time: 2.41 days
- Mean transportation cost: INR 1,606.09
- Distance / transportation-cost correlation: 0.98

# COGITO-FORECAST 📊

**Automated Financial Intelligence & Forecasting Dashboard for SMBs**

## 📖 Project Overview
COGITO-FORECAST is a lightweight, open-source web application designed to democratize financial intelligence for Small and Medium-sized Businesses. It functions as a "Virtual Financial Analyst," bridging the gap between raw accounting data and strategic foresight.

The system allows users to:
1.  **Upload** raw financial CSV data.
2.  **Visualize** historical performance and future trajectories.
3.  **Generate** AI-driven strategic insights and action plans.
4.  **Export** comprehensive PDF reports for offline decision-making.

---

## ⚠️ Assessment Configuration (Simulation Mode)
**NOTE TO ASSESSOR:** This repository contains the **"Simulation Build" (v1.0-academic)** submitted for the Final Project assessment.

To ensure **100% reproducibility**, **offline stability**, and **security** on any assessment machine, this version implements a "Service Mocking" architecture:
* **Forecasting Engine:** Utilizes a linear projection algorithm to mimic the *Facebook Prophet* workflow without requiring complex C++ compiler dependencies (PyStan) on Windows.
* **Intelligence Layer:** Utilizes a deterministic mock response pattern to simulate the *Google Gemini API*. This prevents API key leakage and ensures the demo runs successfully even without an internet connection.

---

## 🚀 Installation & Setup

### Prerequisites
* Python 3.8 or higher

### Step 1: Clone the Repository
```bash
git clone [https://github.com/amalmathewcodes/COGITO-FORECAST.git](https://github.com/amalmathewcodes/COGITO-FORECAST.git)
cd COGITO-FORECAST

Step 2: Install Dependencies
Bash
pip install -r requirements.txt
Step 3: Run the Application
Bash
streamlit run app.py
```
🧪 How to Test (Demo Data)
To facilitate immediate testing, a sample dataset has been provided in this repository.

Download the file sample_financials.csv from the file list above.

Launch the app using the command above.

In the Sidebar, click "Browse files" and select sample_financials.csv.

Click the "🚀 Run Forecast Model" button to see the trajectory.

Click "📈 AI Analysis" to generate the strategic report.

Click "📄 Download PDF" to export the final document.

🛠️ Technology Stack
Frontend: Streamlit

Data Processing: Pandas

Visualization: Plotly Interactive Charts

Reporting: FPDF (PDF Generation Engine)

Architecture: Modular "Input-Process-Export" Pipeline

Student: Amal Mathew | Course: Computer Science Project

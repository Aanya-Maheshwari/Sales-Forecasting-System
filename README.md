# Sales Forecasting & Demand Intelligence System

A full-stack data pipeline and interactive utility designed for weekly supply chain planning and inventory optimization. This system combines time-series forecasting, anomaly detection, and cluster-based stocking strategies into a unified, user-friendly **Streamlit** dashboard.

---

## 🚀 Key Features

* **Interactive Forecast Explorer**: Predicts 3-month future sales trends across diverse product categories and regions using **Facebook Prophet**.
* **Supply Chain Anomaly Tracking**: Implements an **Isolation Forest** pipeline to dynamically flag historical weekly sales outliers (spikes or drops) to prevent stockouts or overstocking.
* **Product Inventory Strategy Matrix**: Uses **K-Means Clustering** to automatically segment inventory into distinct demand profiles (e.g., High Volume/High Volatility vs. Low Volume/Stable) and provides automated stocking recommendations (like *Buffer Stock* or *Just-In-Time* allocation).

---

## 🛠️ Tech Stack & Architecture

* **Frontend Dashboard**: Streamlit
* **Time-Series Forecasting**: Facebook Prophet
* **Anomaly Detection & Clustering**: Scikit-Learn (Isolation Forest, K-Means)
* **Data Manipulation**: Pandas, NumPy
* **Data Visualization**: Matplotlib, Seaborn

---

## 📊 Dataset Reference

The predictive models in this project were trained on the classic retail sales dataset hosted on Kaggle. 
* **Source Dataset**: [Kaggle Sales Forecasting Dataset](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)

---

## ⚙️ How to Run Locally

### Prerequisites
Make sure you have Python installed on your system.

### Installation Steps

```bash
# 1. Clone this repository
git clone [https://github.com/Aanya-Maheshwari/Sales-Forecasting-System-Demand-Intelligence.git](https://github.com/Aanya-Maheshwari/Sales-Forecasting-System-Demand-Intelligence.git)

# 2. Navigate to the project directory
cd Sales-Forecasting-System-Demand-Intelligence

# 3. Install the required dependencies
pip install -r requirements.txt

# 4. Run the Streamlit application
streamlit run app.py

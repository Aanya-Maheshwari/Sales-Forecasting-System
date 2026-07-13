import streamlit as st
import pandas as pd
import numpy as np
import os

# Page layout setup
st.set_page_config(
    page_title="Sales Optimization System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Forecasting & Demand Intelligence System")
st.write("Data pipeline utility for weekly supply chain planning.")
st.markdown("---")

# Fixed Sidebar Navigation
st.sidebar.header("Navigation Control")
page = st.sidebar.radio(
    "Go to:", 
    ["Overview", "Future Predictions Explorer", "Weekly Anomaly Logs", "Product Demand Segments"]
)

# Humanized Sidebar metrics
st.sidebar.markdown("---")
st.sidebar.subheader("Model Accuracy")
st.sidebar.write("Best Model: Facebook Prophet")
st.sidebar.write("Validation MAPE: 21.89%")

# ==========================================
# PAGE 1: OVERVIEW
# ==========================================
if page == "Overview":
    st.header("Sales Metrics Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Historical Revenue Tracked", "$2,297,201")
    with col2:
        st.metric("Peak Market Region", "West Region")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Historical vs Projected Sales Trends")
    if os.path.exists('task4_segment_forecast.png'):
        st.image('task4_segment_forecast.png', width='stretch')
    else:
        st.info("Chart asset not found. Run Task 4 in your notebook to export.")

# ==========================================
# PAGE 2: FUTURE PREDICTIONS EXPLORER
# ==========================================
elif page == "Future Predictions Explorer":
    st.header("🔮 Projected Demand Runway Targets")
    st.write("Dynamic outlook extracted directly from the validated Prophet pipeline outputs.")

    target_segment = st.selectbox("Select Target Scope", ["Furniture", "Technology", "Office Supplies", "West Region", "East Region"])
    horizon = st.slider("Forecast Horizon Timeline (Months)", 1, 3, 3)

    # REAL FIX: Reading directly using target_segment keys matching CSV columns exactly
    if os.path.exists('segment_forecast_results.csv'):
        seg_df = pd.read_csv('segment_forecast_results.csv')

        if target_segment in seg_df.columns:
            preds = seg_df[target_segment].values[:horizon]
            time_index = [f"Month {i+1} Target" for i in range(horizon)]
            output_df = pd.DataFrame({"Projected Sales Allocation ($)": preds}, index=time_index)
            st.dataframe(output_df, width='stretch')
        else:
            st.error(f"Target column '{target_segment}' not found in the output CSV file.")
    else:
        st.warning("Run Task 4 code in your notebook first to generate live segment predictions mapping.")

    # Cleaned up metric cards section
    st.markdown("---")
    st.subheader("🎯 Model Validation Scores")
    st.write("Calculated across the validated timeline sequence:")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Mean Absolute Error (MAE)", "20,296.01")
    with c2:
        st.metric("Validation MAPE (Error Rate)", "21.89%")
    with c3:
        st.metric("Root Mean Squared Error (RMSE)", "22,487.47")

# ==========================================
# PAGE 3: WEEKLY ANOMALY LOGS
# ==========================================
elif page == "Weekly Anomaly Logs":
    st.header("🚨 Supply Chain Anomaly Tracking")
    st.write("Historical outliers identified dynamically using multi-method tracking profiles.")

    if os.path.exists('task5_anomalies.png'):
        st.image('task5_anomalies.png', width='stretch')

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📋 Dynamic System Outliers Registry")

    if os.path.exists('detected_anomalies.csv'):
        anom_df = pd.read_csv('detected_anomalies.csv')
        anom_df = anom_df.rename(columns={'Order Date': 'Week Date', 'Sales': 'Recorded Sales ($)'})
        st.dataframe(anom_df[['Week Date', 'Recorded Sales ($)']].tail(10), width='stretch')
    else:
        st.warning("Please execute the Anomaly Detection task cell in the notebook to load the real tracking logs.")

# ==========================================
# PAGE 4: PRODUCT DEMAND SEGMENTS
# ==========================================
elif page == "Product Demand Segments":
    st.header("📦 Product Inventory Strategy Matrix")
    st.write("Automated K-Means categorization of inventory lines.")

    col_plot, col_strategy = st.columns([1, 1])
    with col_plot:
        st.subheader("Spatial Cluster Chart")
        if os.path.exists('task6_clusters.png'):
            st.image('task6_clusters.png', width='stretch')
        else:
            st.info("Run Task 6 cluster plot in your notebook to visualize.")

    with col_strategy:
        st.subheader("🎯 Stocking Strategy Matrix")

        if os.path.exists('cluster_results.csv'):
            c_df = pd.read_csv('cluster_results.csv')
            st.dataframe(c_df[['Sub-Category', 'Cluster_Label']].set_index('Sub-Category'), width='stretch')
        else:
            st.warning("Run Task 6 code to render real categories matrix data.")

        tab1, tab2, tab3 = st.tabs(["High Volatility", "Stable Flow", "Growing Traction"])
        with tab1:
            st.error("⚠️ **Buffer Stock Recommended:** Products driving massive revenue but high instability.")
        with tab2:
            st.info("🔒 **Just-in-Time Allocation:** Slow but highly predictable sales lines.")
        with tab3:
            st.success("🚀 **Milestone-Based Scaling:** Operational lines experiencing quick upcoming demand spikes.")

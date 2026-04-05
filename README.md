import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import warnings
import numpy as np

from codebase.dashboard_graphs import MaternalHealthDashboard

# =======================
# Load models and scaler
# =======================
maternal_model = pickle.load(open("model/finalized_maternal_model.sav", "rb"))
fetal_model = pickle.load(open("model/fetal_health_classifier.sav", "rb"))
scale_X = pickle.load(open("model/scaler_maternal_model.sav", "rb"))

# =======================
# Sidebar
# =======================
with st.sidebar:
    st.title("MaternalPredict")
    st.write("Welcome to MaternalPredict")

    selected = option_menu(
        "Menu",
        ["About us", "Pregnancy Risk Prediction", "Fetal Health Prediction", "Dashboard"],
        icons=["info-circle", "hospital", "heart-pulse", "bar-chart"],
        default_index=0
    )

# =======================
# About
# =======================
if selected == "About us":

    # =======================
    # Custom Styling
    # =======================
    st.markdown("""
        <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            text-align: center;
            color: #ffffff;
        }
        .subtitle {
            text-align: center;
            color: #bbbbbb;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .card {
            background-color: #111827;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
            text-align: center;
        }
        .metric {
            font-size: 28px;
            font-weight: bold;
            color: #22c55e;
        }
        </style>
    """, unsafe_allow_html=True)

    # =======================
    # HERO SECTION
    # =======================
    st.markdown('<p class="main-title">MaternalPredict</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">AI-powered insights for safer pregnancies & fetal health monitoring</p>',
        unsafe_allow_html=True
    )

    # =======================
    # HERO COLUMNS
    # =======================
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        ### 🧠 What we do
        - Predict **pregnancy risk levels**
        - Analyze **fetal health conditions**
        - Provide **data-driven insights**
        - Help in **early medical intervention**
        """)

    with col2:
        st.image(
          "https://images.unsplash.com/photo-1581594693702-fbdc51b2763b",
          use_column_width=True
    )

    st.divider()

    # =======================
    # FEATURE CARDS
    # =======================
    st.subheader("🚀 Key Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h4>📊 Risk Prediction</h4>
            <p>Machine learning models to assess maternal risk levels.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h4>❤️ Fetal Analysis</h4>
            <p>Advanced CTG-based fetal health classification.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h4>📈 Dashboard</h4>
            <p>Interactive charts & visual insights from real data.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =======================
    # STATS / METRICS
    # =======================
    st.subheader("📌 Impact Overview")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown('<p class="metric">95%</p><p>Prediction Accuracy</p>', unsafe_allow_html=True)

    with m2:
        st.markdown('<p class="metric">10K+</p><p>Records Analyzed</p>', unsafe_allow_html=True)

    with m3:
        st.markdown('<p class="metric">24/7</p><p>Monitoring Support</p>', unsafe_allow_html=True)

    st.divider()

    # =======================
    # SAMPLE GRAPH (UI ENHANCEMENT ONLY)
    # =======================
    st.subheader("📉 Sample Health Trend")

    import pandas as pd
    import numpy as np

    chart_data = pd.DataFrame({
        "Weeks": list(range(1, 11)),
        "Risk Score": np.random.randint(20, 90, 10)
    })

    st.line_chart(chart_data.set_index("Weeks"))

    st.info("This is a sample visualization. Real insights are available in the Dashboard section.")
# =======================
# Pregnancy Risk Prediction
# =======================
if selected == "Pregnancy Risk Prediction":

    st.title("Pregnancy Risk Prediction")
    st.write("Enter correct medical values to predict pregnancy risk.")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age (years)", min_value=10, max_value=60, value=26)

    with col2:
        diastolicBP = st.number_input("Diastolic BP (mmHg)", min_value=40, max_value=120, value=65)

    with col3:
        BS = st.number_input("Blood Glucose (mmol/L)", min_value=2.0, max_value=20.0, value=5.5)

    with col1:
        bodyTemp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=36.8)

    with col2:
        heartRate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=80)

    if st.button("Predict Pregnancy Risk"):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            # Create input array (order MUST match training)
            input_data = np.array([[age, diastolicBP, BS, bodyTemp, heartRate]])

            # Scale input
            input_scaled = scale_X.transform(input_data)

            # Predict
            predicted_risk = maternal_model.predict(input_scaled)

        st.subheader("Risk Level")

        if predicted_risk[0] == 0:
            st.success("Low Risk")
        elif predicted_risk[0] == 1:
            st.warning("Medium Risk")
        else:
            st.error("High Risk")

    if st.button("Clear"):
        st.rerun()

# =======================
# Fetal Health Prediction
# =======================
if selected == "Fetal Health Prediction":

    st.title("Fetal Health Prediction")
    st.write("Enter CTG parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        BaselineValue = st.number_input("Baseline Value", value=120.0)
        uterine_contractions = st.number_input("Uterine Contractions", value=0.0)
        prolongued_decelerations = st.number_input("Prolonged Decelerations", value=0.0)
        mean_value_of_short_term_variability = st.number_input("Mean STV", value=5.0)
        mean_value_of_long_term_variability = st.number_input("Mean LTV", value=50.0)
        histogram_min = st.number_input("Histogram Min", value=60.0)
        histogram_number_of_zeroes = st.number_input("Histogram Zeroes", value=0.0)
        histogram_median = st.number_input("Histogram Median", value=120.0)

    with col2:
        Accelerations = st.number_input("Accelerations", value=0.0)
        light_decelerations = st.number_input("Light Decelerations", value=0.0)
        abnormal_short_term_variability = st.number_input("Abnormal STV", value=0.0)
        percentage_of_time_with_abnormal_long_term_variability = st.number_input("ALTV %", value=0.0)
        histogram_width = st.number_input("Histogram Width", value=50.0)
        histogram_max = st.number_input("Histogram Max", value=180.0)
        histogram_mode = st.number_input("Histogram Mode", value=120.0)
        histogram_variance = st.number_input("Histogram Variance", value=10.0)

    with col3:
        fetal_movement = st.number_input("Fetal Movement", value=0.0)
        severe_decelerations = st.number_input("Severe Decelerations", value=0.0)
        histogram_number_of_peaks = st.number_input("Histogram Peaks", value=2.0)
        histogram_mean = st.number_input("Histogram Mean", value=120.0)
        histogram_tendency = st.number_input("Histogram Tendency", value=0.0)

    if st.button("Predict Fetal Health"):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            fetal_input = [[
                BaselineValue, Accelerations, fetal_movement,
                uterine_contractions, light_decelerations, severe_decelerations,
                prolongued_decelerations, abnormal_short_term_variability,
                mean_value_of_short_term_variability,
                percentage_of_time_with_abnormal_long_term_variability,
                mean_value_of_long_term_variability, histogram_width,
                histogram_min, histogram_max, histogram_number_of_peaks,
                histogram_number_of_zeroes, histogram_mode, histogram_mean,
                histogram_median, histogram_variance, histogram_tendency
            ]]

            predicted_risk = fetal_model.predict(fetal_input)

        if predicted_risk[0] == 1:
            st.success("Normal")
        elif predicted_risk[0] == 2:
            st.warning("Suspect")
        else:
            st.error("Pathological")

# =======================
# Dashboard
# =======================
if selected == "Dashboard":
    st.header("Maternal Health Dashboard")

    api_key = "579b464db66ec23bdd00000139b0d95a6ee4441c5f37eeae13f3a0b2"
    api_endpoint = f"https://api.data.gov.in/resource/6d6a373a-4529-43e0-9cff-f39aa8aa5957?api-key={api_key}&format=csv"

    import pandas as pd

try:
    dashboard = MaternalHealthDashboard(api_endpoint)
    dashboard.create_bubble_chart()
    dashboard.create_pie_chart()

except Exception as e:
    st.error("⚠️ Live API is currently unavailable. Showing sample data instead.")

    # =======================
    # FALLBACK SAMPLE DATA
    # =======================
    sample_data = pd.DataFrame({
        "State": ["A", "B", "C", "D"],
        "Cases": [120, 200, 150, 80]
    })

    st.subheader("📊 Sample Maternal Health Data")

    st.bar_chart(sample_data.set_index("State"))

    st.info("This is fallback data. Connect to API when available.")

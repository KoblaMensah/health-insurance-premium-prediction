import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("xgb_model.pkl")

st.title("🏥 Health Insurance Premium Predictor")

# --- BMI Calculator Section ---
with st.expander("Don't know your BMI? Calculate here!"):
    weight = st.number_input("Enter your weight (in kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    height = st.number_input("Enter your height (in meters)", min_value=1.0, max_value=2.5, value=1.70, step=0.01)
    
    if st.button("Calculate BMI"):
        bmi_value = weight / (height ** 2)
        st.success(f"Your calculated BMI is: {bmi_value:.2f}")

# --- Premium Prediction Section ---
with st.form("input_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age", min_value=18, max_value=64, value=39, help="Range matches training data (18-64 years)")
        bmi = st.slider("BMI", min_value=16.0, max_value=53.1, value=30.4, step=0.1, help="Healthy range: 18.5-24.9")
    
    with col2:
        children = st.slider("Number of Children", min_value=0, max_value=5, value=1, help="Max 5 children in training data")
        sex = st.selectbox("Sex", ["Female", "Male"])
        smoker = st.selectbox("Smoker", ["No", "Yes"])
        region = st.selectbox("Region", ["Southeast", "Northwest", "Southwest", "Northeast"])
    
    submitted = st.form_submit_button("Predict Premium")

if submitted:
    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex_male": [1 if sex == "Male" else 0],
        "smoker_yes": [1 if smoker == "Yes" else 0],
        "region_northwest": [1 if region == "Northwest" else 0],
        "region_southeast": [1 if region == "Southeast" else 0],
        "region_southwest": [1 if region == "Southwest" else 0]
    })
    
    premium = model.predict(input_data)[0]
    
    st.success(f"**Predicted Premium:** ${premium:.2f}")

    # Create report as a DataFrame
    report_df = pd.DataFrame({
        "Age": [age],
        "BMI": [bmi],
        "Children": [children],
        "Sex": [sex],
        "Smoker": [smoker],
        "Region": [region],
        "Predicted Premium ($)": [f"{premium:.2f}"]
    })

    # Convert report to CSV
    csv = report_df.to_csv(index=False).encode('utf-8')

    # Download button
    st.download_button(
        label="📄 Download Prediction Report",
        data=csv,
        file_name='insurance_premium_report.csv',
        mime='text/csv'
    )


import streamlit as st
import pandas as pd
import joblib

# Page setup
st.title("🔮 Animal Extinction Risk Prediction")

st.markdown("""
Input the traits of a species to see if it's at risk of extinction.  
The prediction is based on a trained Decision Tree model using animal and climate features.
""")

# Load model
model = joblib.load("Model/predicting_model.pkl")

# Define form inputs
with st.form("prediction_form"):
    st.subheader("🧬 Species Traits")
    height = st.slider("Height (cm)", 1, 500, 100)
    weight = st.slider("Weight (kg)", 1, 5000, 100)
    lifespan = st.slider("Lifespan (years)", 1, 150, 20)
    speed = st.slider("Average Speed (km/h)", 1, 120, 20)
    gestation = st.slider("Gestation Period (days)", 10, 1000, 100)
    offspring = st.slider("Offspring per Birth", 1, 20, 1)
    temp_change = st.slider("Avg Temp Change in Habitat (°C)", 0.0, 4.0, 1.5)

    submitted = st.form_submit_button("Predict")

# Prediction logic
if submitted:
    input_data = pd.DataFrame([{
        "Height (cm)": height,
        "Weight (kg)": weight,
        "Lifespan (years)": lifespan,
        "Average Speed (km/h)": speed,
        "Gestation Period (days)": gestation,
        "Offspring per Birth": offspring,
        "temp_change": temp_change
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ This species is predicted to be AT RISK of extinction.")
    else:
        st.success("✅ This species is predicted to be NOT at risk.")

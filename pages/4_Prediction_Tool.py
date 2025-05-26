import streamlit as st
import pandas as pd
import joblib

# Load your trained Logistic Regression model
# scaler = joblib.load("Model/scaler.pkl")
# selector = joblib.load("Model/selector.pkl")
model = joblib.load("Model/predicting_model.pkl")

# --- Region to temp values
region_to_temp = {
    "Africa": {"temp_change": 0.19, "avg_temp_recent": 21.703},
    "Asia": {"temp_change": 1.12, "avg_temp_recent": 21.2},
    "Europe": {"temp_change": 1.51, "avg_temp_recent": 10.6},
    "Americas": {"temp_change": 0.96, "avg_temp_recent": 15.3},
    "Oceania": {"temp_change": 1.18, "avg_temp_recent": 22.5},
    "Arctic": {"temp_change": 2.78, "avg_temp_recent": -5.0}
}

# --- Social structure encoding
social_map = {
    "Colony-based": 0,
    "Eusocial": 1,
    "Flocks": 2,
    "Group-based": 3,
    "Herd-based": 4,
    "Pack-based": 5,
    "Social groups": 6,
    "Social pods": 7,
    "Solitary": 8,
    "Varies": 9
}

# --- Habitat encoding (now just one value!)
habitat_map = {
    "Wetlands": 0,
    "Forests": 1,
    "Grasslands": 2,
    "Mountains": 3,
    "Oceans": 4,
    "Other": 5,
    "Freshwater": 6,
    "Tundra": 7,
    "Deserts": 8  # optional: only include if in training set
}

# --- Streamlit interface
st.title("🦓 Predict Extinction Risk (Logistic Regression)")

st.markdown("""
Enter species traits below.  
Climate values are auto-filled from region 🌍.  
Habitat & social structure are encoded internally.
""")

# --- Form Inputs
with st.form("prediction_form"):
    st.subheader("🧬 Physical Traits")
    height = st.slider("Height (cm)", 1, 500, 100)
    weight = st.slider("Weight (kg)", 1, 5000, 100)
    lifespan = st.slider("Lifespan (years)", 1, 150, 20)
    speed = st.slider("Average Speed (km/h)", 1, 120, 20)
    gestation = st.slider("Gestation Period (days)", 10, 1000, 100)
    offspring = st.slider("Offspring per Birth", 1, 20, 1)

    st.subheader("👥 Social Structure")
    social_label = st.selectbox("Choose type", list(social_map.keys()))
    social_encoded = social_map[social_label]

    st.subheader("🌍 Region")
    region = st.selectbox("Region", list(region_to_temp.keys()))
    temp_change = region_to_temp[region]["temp_change"]
    avg_temp = region_to_temp[region]["avg_temp_recent"]

    st.subheader("🏞️ Habitat")
    habitat_label = st.selectbox("Habitat Type", list(habitat_map.keys()))
    habitat_encoded = habitat_map[habitat_label]

    submitted = st.form_submit_button("Predict")

# --- On Submit
if submitted:
    input_data = pd.DataFrame([{
        "Height (cm)": height,
        "Weight (kg)": weight,
        "Lifespan (years)": lifespan,
        "Average Speed (km/h)": speed,
        "Gestation Period (days)": gestation,
        "Offspring per Birth": offspring,
        "Social Encoded": social_encoded,
        "temp_change": temp_change,
        "avg_temp_recent": avg_temp,
        "Habitat Encoded": habitat_encoded
    }])

    # # 1. Scale input
    # X_scaled = scaler.transform(input_data.values)

    # # 2. Select best features
    # X_selected = selector.transform(X_scaled)

    # # 3. Predict
    # prediction = model.predict(X_selected)[0]
    # probability = model.predict_proba(X_selected)[0][1]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ This species is predicted to be **AT RISK**.\nProbability: **{probability:.2f}**")
    else:
        st.success(f"✅ This species is predicted to be **NOT at risk**.\nProbability: **{probability:.2f}**")

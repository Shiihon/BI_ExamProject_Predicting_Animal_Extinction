import streamlit as st

# 💚 Page title
st.set_page_config(page_title="Animal Extinction Risk", layout="wide")
st.title("BI Exam: Animal Extinction Risk Prediction Project")

# 🔎 Project intro
st.markdown("""
Welcome to the **Animal Extinction Risk Predictor** app!

This tool uses animal biological data and climate indicators to help predict the **risk of extinction** for different species.
It is based on a machine learning model trained on real datasets.

### 👈 Use the menu on the left to:
- Explore data visualizations
- Input animal traits and **get a prediction**
""")

# 📷 Optional image (make sure the path is correct)
# st.image("images/extinction.jpg", use_column_width=True)

# Sidebar (shows on all pages)
st.sidebar.title("📘 About")
st.sidebar.markdown("""
Built by Nanna using data from:
- Kaggle Animal Dataset
- World Bank Climate Indicators

Model used: **Decision Tree Classifier**

Enjoy exploring the data and trying out predictions!
""")

import streamlit as st

# Set page config (only once)
st.set_page_config(
    page_title="Welcome | Animal Extinction Risk",
    layout="wide"
)

# Title section
st.markdown("""
<h1 style='text-align: center;'>
    🌍 <span style="font-size: 2.5rem;">WildTrack: Species Risk & Survival</span>
</h1>
<p style='text-align: center; font-size: 1.1rem;'>
    Welcome to my <strong>BI Exam Project Dashboard</strong>!
</p>
<p style='text-align: center;'>This interactive app explores:</p>
<blockquote style='text-align: center; font-style: italic; color: #555;'>
    Which animals are most at risk of extinction — and why?
</blockquote>
<p style='text-align: center; max-width: 850px; margin: auto;'>
    By combining <strong>biological traits</strong> with <strong>climate data</strong>,
    this project uses machine learning to help predict species vulnerability.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# Use central space for content: left buffer, center (offers + works), right buffer
col_spacer1, col_main1, col_main2, col_spacer2 = st.columns([3, 4, 4, 1])


with col_main1:
    st.markdown("### What this app offers:")
    st.markdown("""
    - Interactive **data visualizations**  
    - Custom input to get a **risk prediction**  
    - Insights into which traits matter most — and why  
    """)

with col_main2:
    st.markdown("### How it works:")
    st.markdown("""
    - **Model used:** Logistic Regression  
    - **Data sources:**  
        - Kaggle Animal Dataset  
        - World Bank Climate Indicators  
    """)

# 📎 GitHub link
st.markdown("""
<br>
<p style='text-align: center; font-size: 1.05rem;'>
    If you’d like to explore the code or methodology:<br>
    👉 <a href="https://github.com/Shiihon/BI_ExamProject_Predicting_Animal_Extinction/tree/main" target="_blank"><strong>View full GitHub repo</strong></a>
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 0.95rem; color: #555;'>
    Interested in the research questions and hypothesis results?<br>
    You can find them in the full <strong>project report</strong> inside the GitHub repo.
</p>
""", unsafe_allow_html=True)

# 🧾 Sidebar still clean
st.sidebar.title("📘 About This App")
st.sidebar.markdown("""
Created by **Nadia Hamza**  
BI Exam Project (Semester 4)
(CphBusiness Lyngby)

- Combines climate + species data  
- Predicts extinction risk  
- Explains model logic  

Enjoy exploring 🌱
""")

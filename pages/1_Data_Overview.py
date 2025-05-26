import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged dataset
@st.cache_data
def load_data():
    return pd.read_csv("Data/Cleaned_Data/final_combined_data.csv")

df = load_data()
st.write(df.columns.tolist())

# Page title and introduction
st.title("Data Overview: Animal + Climate Features")
st.markdown("""
This dashboard provides an interactive overview of a merged dataset combining animal traits and regional climate trends.  
It was developed to explore how biological and environmental factors relate to extinction risk.

Below you'll see a preview of the cleaned dataset, and 3 focused tabs.
""")

# Preview
st.subheader("Preview of Merged Dataset")
st.dataframe(df.head())

st.markdown("""
- **Tab 1: Traits & Climate**  
  Explores how biological traits (like weight, speed, lifespan) may correlate with climate indicators.

- **Tab 2: Risk Factors**  
  Compares species classified as at-risk vs. not-at-risk to highlight possible predictors of extinction vulnerability.

- **Tab 3: Climate Impact by Region**  
  Analyzes temperature change across habitats and regions to uncover geographic patterns tied to climate pressure.
""")

st.markdown("""
Each chart is designed to offer:
- 📊 A descriptive comparison (e.g. boxplots)
- 🔍 A relationship insight (e.g. scatter or correlation)
- 🌍 A contextual summary (e.g. distribution by region)
""")

tab1, tab2, tab3 = st.tabs(["🌡️ Climate & Traits", "🔥 Climate & Risk", "🧭 Regional Climate Impact"])

with tab1:
    st.subheader("1️⃣ Correlation Heatmap: Climate & Traits")

    # Filter DataFrame to selected numeric columns
    selected_cols = [
        "Height (cm)",
        "Weight (kg)",
        "Lifespan (years)",
        "Social Encoded",
        "Gestation Period (days)",
        "Offspring per Birth",
        "temp_change",
        "avg_temp_recent",
        "At_Risk"
    ]

    filtered_df = df[selected_cols].copy()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Between Traits and Climate Variables")
    st.pyplot(fig)

    st.subheader("2️⃣ Scatterplot: Lifespan vs Temperature Change")
    if "temp_change" in df.columns and "Lifespan (years)" in df.columns:
        fig2, ax2 = plt.subplots()
        sns.scatterplot(x="temp_change", y="Lifespan (years)", hue="At_Risk", data=df, ax=ax2)
        ax2.set_title("Lifespan vs. Climate Change (colored by At_Risk)")
        st.pyplot(fig2)

    st.subheader("3️⃣ Boxplot: Weight by Diet Type")
    if "Diet" in df.columns and "Weight (kg)" in df.columns:
        # Group rare diets
        diet_counts = df["Diet"].value_counts()
        rare_diets = diet_counts[diet_counts < 5].index
        df["Diet_Cleaned"] = df["Diet"].replace(rare_diets, "Other")

        # Plot
        fig, ax = plt.subplots()
        sns.boxplot(x="Diet_Cleaned", y="Weight (kg)", data=df, ax=ax)
        ax.set_title("Weight Distribution by Diet Type (Grouped)")
        ax.set_ylabel("Weight (kg)")
        ax.set_xlabel("Dietary Type")
        ax.set_ylim(0, 1000)
        plt.xticks(rotation=65, ha='right')
        st.pyplot(fig)


with tab2:
    # Map keywords to simplified habitat categories
    habitat_map = {
    "forest": "Forests",
    "rainforest": "Forests",
    "mountain": "Mountains",
    "desert": "Deserts",
    "tundra": "Tundra",
    "wetland": "Wetlands",
    "ocean": "Oceans",
    "marine": "Oceans",
    "freshwater": "Freshwater",
    "river": "Freshwater",
    "lake": "Freshwater",
    "grassland": "Grasslands",
    "savanna": "Grasslands",
    "plain": "Grasslands"
}
    # Function to simplify the original habitat strings
    def simplify_habitat(habitat_str):
        for keyword, category in habitat_map.items():
            if keyword.lower() in str(habitat_str).lower():
                return category
        return "Other"

    st.subheader("1️⃣ Bar Chart: At-Risk Species per Habitat")
    if "Habitat Category" in df.columns and "At_Risk" in df.columns:
        simplified_counts = df.groupby("Habitat Category")["At_Risk"].sum().sort_values(ascending=False)

        fig, ax = plt.subplots()
        simplified_counts.plot(kind="bar", color="firebrick", ax=ax)
        ax.set_ylabel("Number of At-Risk Species")
        ax.set_title("At-Risk Species by Simplified Habitat")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)

    st.subheader("2️⃣ Bar Chart: Climate Change Levels for At-Risk vs Not")
    if "At_Risk" in df.columns and "temp_change" in df.columns:
        fig5, ax5 = plt.subplots()
        sns.boxplot(x="At_Risk", y="temp_change", data=df, ax=ax5)
        ax5.set_xticklabels(["Not at Risk", "At Risk"])
        ax5.set_title("Temperature Change in Habitats of At-Risk vs Non-Risk Species")
        st.pyplot(fig5)

    st.subheader("3️⃣ Boxplot: Lifespan by At-Risk Status")
    if "At_Risk" in df.columns and "Lifespan (years)" in df.columns:
        fig6, ax6 = plt.subplots()
        sns.boxplot(x="At_Risk", y="Lifespan (years)", data=df, ax=ax6)
        ax6.set_xticklabels(["Not at Risk", "At Risk"])
        ax6.set_title("Lifespan by Extinction Risk")
        st.pyplot(fig6)

with tab3:
    st.subheader("1️⃣ Histogram: All Temperature Change Values")
    fig7, ax7 = plt.subplots()
    sns.histplot(df["temp_change"], bins=20, kde=True, ax=ax7)
    ax7.set_title("Distribution of Temperature Changes Across Species")
    st.pyplot(fig7)

    st.subheader("🌡️ Avg Temperature Change by Region")
    avg_temp_by_region = df.groupby("Region")["temp_change"].mean().dropna()

    fig, ax = plt.subplots()
    avg_temp_by_region.sort_values().plot(kind="bar", ax=ax, color="skyblue")
    ax.set_ylabel("Avg Temperature Change (°C)")
    ax.set_title("Average Regional Temperature Change")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

    st.subheader("3️⃣ Temperature Change by Habitat Category")
    if "Habitat Category" in df.columns and "temp_change" in df.columns:
        # 🧼 Step 1: Filter out categories with fewer than 3 entries
        habitat_counts = df["Habitat Category"].value_counts()
        valid_categories = habitat_counts[habitat_counts >= 3].index
        filtered_df = df[df["Habitat Category"].isin(valid_categories)]

        # 📈 Step 2: Make the plot using the filtered data
        fig, ax = plt.subplots()
        sns.boxplot(x="Habitat Category", y="temp_change", data=filtered_df, ax=ax)
        ax.set_title("Temperature Change (1901–2023) by Habitat Type")
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

        # ℹ️ Optional info note for the user
        st.markdown("ℹ️ Habitat types with fewer than 3 species were excluded for clarity.")



   



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged dataset
@st.cache_data
def load_data():
    return pd.read_csv("Data/Cleaned_Data/cleaned_animal_data.csv")

df = load_data()
#st.write(df.columns.tolist())

# Page title and introduction
st.title("Data Overview: Animal Data")
st.markdown("""
The animal dataset includes key biological and ecological features such as lifespan, reproductive habits, social structure, and diet.
Species are categorized by whether they are "at risk" or not, enabling supervised learning and trait-based insights.
Some animals appear multiple times due to their presence in several regions, which was addressed during data cleaning.
""")

# Preview
st.subheader("Preview of Merged Dataset")
st.dataframe(df.head())
st.markdown("---")

st.subheader("Analyzing Animal Data")

# Create a responsive but fixed-width centered column
container = st.container()
with container:
    fig, ax = plt.subplots(figsize=(14, 8))  # Balanced size
    sns.countplot(data=df, x="Conservation Status", order=df["Conservation Status"].value_counts().index, ax=ax)
    ax.set_title("Distribution of Conservation Status", fontsize=18, loc="center")
    ax.set_ylabel("Count", fontsize=16)
    ax.set_xlabel("Conservation Status", fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()

    st.pyplot(fig, use_container_width=True)

    st.markdown("""

### **What we can observe from the chart:**
This bar chart shows how many species fall under each conservation status — from “Least Concern” to “Extinct.” It gives us a clear picture of how widespread extinction risk is in our dataset.

 - **Most species** are listed as ***"Least Concern"*** meaning they're currently safe.
 - However, a large number are ***""Vulnerable"***, ***"Endangered"***, or even ***"Critically Endangered"***, which means they already face serious threats.
 - A few are marked as ***"Extinct"***, including some that dissappeared thousands of years ago.                                              
Even though most species aren’t at risk <em>yet</em>, the amount already in danger is significant. This highlights why early prediction of extinction risk matters — so we can take action before it’s too late.

""")
st.markdown("")

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df, x="At_Risk", y="Offspring per Birth", ax=ax)
ax.set_title("Offspring per Birth vs. Extinction Risk", fontsize=18, loc="center")
ax.set_xlabel("At Risk (0 = Not at Risk, 1 = At Risk)", fontsize=14)
ax.set_ylabel("Offspring per Birth", fontsize=14)
ax.set_ylim(0, 40)
plt.tight_layout()
st.pyplot(fig, use_container_width=True)

st.markdown("""
### **What we can observe from the chart:**
This bar chart shows how many species fall under each conservation status — from “Least Concern” to “Extinct.” It gives us a clear picture of how widespread extinction risk is in our dataset.
            
This boxplot compares the number of offspring per birth between animals that are **at risk** of extinction and those that are **not at risk**. We've limited the y-axis to 40 to focus on the most relevant range (excluding extreme outliers).

- **Not-at-risk species (0)** tend to have **more offspring** on average and show a slightly wider range.
- **At-risk species (1)** mostly have **fewer offspring per birth**, with very limited variation.
- This suggests that species producing more offspring may have a **higher chance of long-term survival**, but it’s **not a guarantee**.

Even if many animals reproduce often, extinction can still threaten them due to other factors like **habitat loss** or **climate change**. That’s why we need to look at multiple traits — not just reproduction — to predict extinction risk accurately.
""")
st.markdown("---")

fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, x="Diet", hue="At_Risk", ax=ax)
ax.set_title("Diet Type by Extinction Risk", fontsize=17, loc="center")
ax.set_xlabel("Diet", fontsize=16)
ax.set_ylabel("Count", fontsize=16)
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()

st.pyplot(fig, use_container_width=True)

st.markdown("""
### What we can observe from the chart:
This chart shows how different diet types are associated with extinction risk. Here's what stands out:

- **Carnivores** and **Herbivores** are the most common diet types in the dataset.
- A noticeable number of **Herbivores** and **Omnivores** are marked as at-risk, suggesting vulnerability despite diet diversity.
- **Insectivores** and mixed-diet species (like "Herbivore, Insectivore") appear less frequently but still show some risk presence.
- The variety of diets among both safe and at-risk species highlights that diet alone doesn’t guarantee survival.

It gives us insight that while diet plays a role in a species’ life strategy, it’s not a clear-cut predictor of extinction risk by itself.
""")
st.markdown("---")

# Only select numeric columns
numeric_cols = df.select_dtypes(include=["float64", "int64", "bool"])

# Drop region indicator columns
region_cols = ['Africa', 'Asia', 'Europe', 'Americas', 'Oceania', 'Arctic']
numeric_cols = numeric_cols.drop(columns=region_cols, errors="ignore")

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Correlation Heatmap (Numerical Features)", fontsize=17)
plt.tight_layout()

st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This heatmap helps us understand how different numerical traits are related to each other in the dataset.  
Correlation values range from **-1 (negative)** to **+1 (positive)** — the closer to 1 or -1, the stronger the relationship.

- **Height, Weight, and Lifespan** have a noticeable positive correlation.  
  ↳ This means that generally, larger animals tend to live longer.

- **Gestation Period** is moderately correlated with **Weight** and **Lifespan**,  
  suggesting that bigger, longer-living species also have longer pregnancies.

- **At_Risk** has weak correlations with most traits, but some stand out:
  - A **positive correlation with Lifespan**, meaning longer-living animals may be more likely to be at risk — possibly because they reproduce more slowly.
  - A slight positive link with **Weight**, indicating heavier animals might also be more vulnerable.

- **Offspring per Birth** shows **no strong correlation** with risk, but slightly more offspring is loosely connected to reduced risk.

- **Average Speed** and **Social Encoded** don’t appear to be strongly tied to risk or other traits in this dataset.

Overall: There’s no single "magic" trait that explains extinction risk.  
Instead, it’s likely a **combination of factors** — like lifespan, weight, and reproductive patterns — that together influence survival chances.
""")


st.markdown("---")


# Count of at-risk animals per region
region_risk_counts = df[df["At_Risk"] == True][region_cols].sum()

fig, ax = plt.subplots(figsize=(8, 5))
region_risk_counts.sort_values().plot(kind="barh", color="tomato", ax=ax)
ax.set_xlabel("Count of At-Risk Animals")
ax.set_title("Number of At-Risk Animals per Region", fontsize=17)
st.pyplot(fig, use_container_width=True)

st.markdown("""
### **What we can observe from the chart:**

This horizontal bar chart shows the number of animals at risk of extinction in each major region of the world.

- **Asia** stands out with the **highest number** of at-risk species in this dataset.
- **Africa** follows, also showing a large amount of species facing danger.
- **Oceania** and the **Americas** show moderate levels of risk, while
- **Europe** and the **Arctic** have the **fewest at-risk animals** recorded.

This may reflect both biodiversity and data coverage — some regions simply have more species or more thorough assessments.
""")

st.markdown("""
---  
### **Final Thoughts on Animal Data Insights**

Through this analysis, we've explored the biological and ecological traits of various species and how they relate to extinction risk.  
The findings give us several important takeaways:

- Species classified as **"at risk"** often differ in key traits such as **lifespan**, **reproduction**, and **habitat type**.
- Some diets and social structures appear more common among threatened species.
- **Asia and Africa** hold the **highest number of vulnerable species**, possibly due to high biodiversity, environmental pressure, or human activity.

These insights reinforce the importance of monitoring not just environmental changes but **biological patterns** as well.  
By understanding what makes a species vulnerable, we’re one step closer to **predicting and preventing extinction** — before it’s too late.  
""")


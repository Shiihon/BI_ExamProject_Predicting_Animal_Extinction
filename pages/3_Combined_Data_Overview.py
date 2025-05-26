import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Load merged dataset
@st.cache_data
def load_data():
    return pd.read_csv("Data/Cleaned_Data/final_combined_data.csv")

df = load_data()
#st.write(df.columns.tolist())

# Page title and introduction
st.title("Data Overview: Climate Data")
st.markdown("""
This section explores a merged dataset that integrates animal biological traits with climate trends across global regions.
It serves as the foundation for predictive modeling, linking species’ ecological profiles to recent environmental changes.
The goal is to understand how traits and temperature shifts together may contribute to extinction risk
""")
# Preview
st.subheader("Preview of Merged Dataset")
st.dataframe(df.head())
st.markdown("---")

st.subheader("Analyzing Combined Data")
# Boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Diet', y='avg_temp_recent', palette='coolwarm', ax=ax)
ax.set_title("Average Regional Temperature by Diet Type", fontsize=17)
ax.set_xlabel("Diet", fontsize=16)
ax.set_ylabel("Average Temperature (°C, 2014–2023)", fontsize=16)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**
            
This boxplot shows the **average regional temperatures** (from 2014–2023) where animals with different diet types are found.  
Each box represents the **temperature range** experienced by animals of that specific diet type.

- **Common diet types** like *Insectivore*, *Herbivore*, *Carnivore*, and *Omnivore* show a **wide range of temperatures**, suggesting that these animals are spread across diverse climates.
- Some diet labels appear **long or combined** (e.g., *Carnivore, Scavenger*, *Herbivore, Insectivore*). These represent animals with **multiple diet classifications**.
- Diet types that are shown as **thin horizontal lines without a box** only have **one or very few animals** in the dataset.  
  That means there isn’t enough data to show variation — just a single temperature value.

Keep in mind that categories with few entries are less reliable for drawing broad conclusions.
""")

# Group and sort data
diet_temp_change = df.groupby('Diet')['temp_change'].mean().sort_values().reset_index()

# Title and intro
st.markdown("""
---
### **Average Temperature Change by Diet Type**
This table shows the **mean temperature change (2014–2023)** experienced by animals with different diet types.  
It helps identify which dietary groups are most exposed to climate shifts.
""")

# Show as a styled dataframe
st.dataframe(diet_temp_change.style.format({'temp_change': '{:.2f}'}).background_gradient(cmap='coolwarm', subset='temp_change'))

# Optional note for missing data
st.markdown("""
⚠️ *Note: Some diet types are missing (`NaN`) because they had no valid temperature change data after merging.*  
These may represent very rare diets or data gaps and were excluded from the table above.
""")
st.markdown("""
### **What we can observe from the table:**

This table ranks **diet types** by the **average temperature change** in the regions where those animals live (from 2014–2023).

- Diet combinations like *Herbivore, Insectivore* and *Omnivore, Insectivore* are linked to **the smallest climate changes**, suggesting those species may live in more stable environments.
- On the other hand, diets such as *Omnivore, Herbivore* and *Carnivore, Piscivore* are found in regions with the **highest temperature shifts**, possibly indicating greater environmental pressure.
- **Composite diet types** (those with multiple labels) appear throughout the list and may reflect species with broader ecological niches.
- Diet types with **no data** (not shown in this table) were excluded due to missing or insufficient climate records.

These patterns may help identify which dietary groups are most vulnerable to future environmental change.
""")

st.markdown("---")
# Bar plot
fig, ax = plt.subplots(figsize=(14, 8))
sns.countplot(data=df, x='Diet', hue='Conservation Status', ax=ax)
ax.set_title("Conservation Status Distribution by Diet Type", fontsize=17)
ax.set_xlabel("Diet", fontsize=18)
ax.set_ylabel("Count", fontsize=16)
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This bar chart shows how animals with different **diet types** are distributed across various **conservation statuses**.

- Diet types like **Insectivore**, **Herbivore**, **Carnivore**, and **Omnivore** have the **highest number of entries**, and also show the **broadest range of conservation categories** — from *Least Concern* to *Critically Endangered*.
- **"Least Concern"** remains the most common status across nearly all diet groups, but **vulnerable and endangered species** are still visibly present in nearly every category.
- **Composite diets** (e.g., *Omnivore, Insectivore* or *Carnivore, Piscivore*) appear less frequently and mostly contain species in **threatened or endangered statuses**, possibly due to smaller sample sizes.
- The right side of the chart contains **rare diet combinations**, each with only a few species. These tend to have lower overall counts and limited conservation categories.
- Some extinct or prehistoric statuses (e.g., *Extinct ~58 million years ago*) appear in **very small numbers**, highlighting data that may come from fossils or long-lost lineages.

Overall, this chart helps link **feeding behavior** with species survival, showing which diet groups might be more ecologically vulnerable or under-studied.
""")

st.markdown("---")

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='At_Risk', y='temp_change', ax=ax)
ax.set_title("Temperature Change (1901–2023) for At-Risk vs. Non-At-Risk Species", fontsize=17)
ax.set_xlabel("At Risk (1 = Yes, 0 = No)", fontsize=16)
ax.set_ylabel("Temperature Change (°C)", fontsize=16)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This boxplot compares the **regional temperature change (1901–2023)** experienced by species that are marked as *at risk* versus those that are not.

- **At-risk species** (1/True) appear to be living in regions with **greater temperature fluctuations**. Their data shows a **larger spread** and higher upper range in temperature change.
- In contrast, **non-at-risk species** (0/False) tend to be in **more stable climates**, with a **narrower distribution** and a slightly lower median.
- This difference in variation suggests that **exposure to climate change** may be one of several contributing factors to extinction risk.
- However, overlap exists between the two groups, indicating that **temperature alone isn’t a guaranteed predictor**, but it may still be a relevant risk indicator.

This visualization strengthens the idea that climate instability can correlate with species vulnerability, though additional ecological and biological factors must also be considered.
""")

st.markdown("---")

# Calculate average temperature change by risk status
avg_temp_by_risk = df.groupby('At_Risk')['temp_change'].mean()

# Streamlit display in a summary box format
st.markdown("### **Average Temperature Change by Risk Status (1901–2023)**")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Not At-Risk Species (False)", value=f"{avg_temp_by_risk[False]:.2f} °C")

with col2:
    st.metric(label="At-Risk Species (True)", value=f"{avg_temp_by_risk[True]:.2f} °C")

st.markdown("""
### **What we can observe from the values above:**

- On average, species classified as **at risk** have experienced a **slightly higher regional temperature change** (1.17 °C) compared to those that are **not at risk** (1.11 °C).
- While the difference may seem small, it suggests that even **modest increases in environmental stress** could be linked to species vulnerability.
- These results support the idea that **climate change may be a contributing factor** in extinction risk, although further analysis is needed to isolate its exact role.

A small difference in average temperature can have major effects on ecosystems — especially for sensitive species.
""")

st.markdown("---")

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x='Offspring per Birth', y='temp_change', hue='At_Risk', ax=ax)
ax.set_title("Offspring per Birth vs. Temperature Change (Colored by At-Risk Status)", fontsize=17)
ax.set_xlabel("Offspring per Birth", fontsize=16)
ax.set_ylabel("Temperature Change (°C)", fontsize=16)
ax.set_xlim(0, 40)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This scatterplot visualizes how the number of **offspring per birth** relates to the **temperature change** species have experienced,  
with points colored based on whether the species is **at risk** (*orange*) or **not at risk** (*blue*).

- Most animals cluster around **low offspring counts (1–10)**, regardless of risk status — indicating that smaller litters are common.
- Both at-risk and non-at-risk species are spread throughout similar **temperature change ranges**, especially between **0.5 °C and 2.0 °C**.
- There are **no clear visual patterns** suggesting that higher offspring numbers consistently protect against climate change impact.
- A few species with very high offspring counts (15–35) still fall into both risk categories, hinting that **reproductive rate alone does not determine extinction vulnerability**.

In summary: while reproductive output varies, it does **not appear to strongly correlate** with whether a species is considered at risk due to climate change.
""")

st.markdown("---")

# Calculate correlation
corr = df[['Offspring per Birth', 'temp_change']].corr().iloc[0, 1]

# Calculate groupwise offspring average
avg_offspring_by_risk = df.groupby('At_Risk')['Offspring per Birth'].mean()

# Header
st.markdown("""
### **Does Reproduction Buffer Against Climate Change Risk?**
This section explores how **offspring count** relates to **temperature change** and **extinction risk**.
""")

# Correlation result box
st.info(f"**Correlation between Offspring per Birth and Temperature Change:** {corr:.4f}")

# Side-by-side average offspring counts
col1, col2 = st.columns(2)

with col1:
    st.metric("Avg. Offspring (Not At-Risk)", f"{avg_offspring_by_risk[False]:.2f}")

with col2:
    st.metric("Avg. Offspring (At-Risk)", f"{avg_offspring_by_risk[True]:.2f}")

st.markdown("""
### **What we can observe from the results above:**

- The **correlation** between *offspring per birth* and *temperature change* is **very weak and negative** (-0.0782), suggesting that species living in areas with more climate change **do not necessarily produce more or fewer offspring**.
- However, there is a **clear difference in average reproductive output** between groups:
  - Species that are **not at risk** produce significantly more offspring on average (**15.89**),
  - While **at-risk species** produce far fewer (**6.06**).
- This may suggest that **lower reproductive rates** could be a **risk factor**, potentially making it harder for these species to recover from population declines or adapt to environmental stress.

While climate change alone doesn’t explain this pattern, the combination of **low reproduction** and **environmental pressure** may increase extinction vulnerability.
""")

st.markdown("---")

# Header and intro
st.markdown("""
### **How Temperature Change Varies Across Habitats**
To make this analysis readable, the many habitat types were **grouped into simplified categories** (e.g., "Rainforest" → "Forests").  
This plot compares how much **temperature has changed (1901–2023)** in different habitat environments.
""")

# Boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Habitat Category', y='temp_change', ax=ax)
ax.set_title("Temperature Change (1901–2023) by Simplified Habitat Type, fotnsize=17")
ax.set_xlabel("Habitat Category", fontsize=16)
ax.set_ylabel("Temperature Change (°C)", fontsize=16)
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This boxplot shows how **temperature change (1901–2023)** varies across different types of habitats, after grouping them into simplified categories.

- **Mountains** and **Freshwater** habitats show the **highest median temperature change**, indicating that species in these environments may be especially exposed to recent climate shifts.
- **Tundra** also shows a consistently high temperature change, though it contains fewer entries, reflected in the narrow box width.
- **Grasslands**, **Wetlands**, and **Deserts** generally show **lower and more stable temperature changes**, with tighter distributions and lower medians.
- The **Forests** category has a wide range, suggesting variation depending on forest type and location (e.g., tropical vs. temperate).
- The **“Other”** category captures undefined or less common habitats (like caves, cities, or unknown types), and also shows moderate variability.

This comparison highlights that **climate impact is not evenly distributed** — habitat type plays a key role in the environmental conditions species face.
""")

st.markdown("---")

# Calculate mean temperature change per habitat category
habitat_temp_change = df.groupby('Habitat Category')['temp_change'].mean().sort_values().reset_index()

# Header
st.markdown("""
---
### **Average Temperature Change by Habitat Type (1901–2023)**
The chart above showed variability within each habitat — this table summarizes the **mean temperature change** for each category.
""")

# Display table with color gradient
st.dataframe(
    habitat_temp_change.style.format({'temp_change': '{:.2f} °C'}).background_gradient(cmap='coolwarm', subset='temp_change'),
    use_container_width=True
)

st.markdown("""
### **What we can observe from the table above:**

- **Mountains** have experienced the **highest average temperature change** (2.04 °C), making them the most affected habitat in the dataset.
- **Tundra** also shows a high level of warming (1.52 °C), which aligns with broader global research highlighting its vulnerability to climate shifts.
- Habitats like **Oceans**, **Freshwater**, and **Forests** fall in the **mid-range**, showing notable but less extreme temperature increases.
- **Deserts**, **Grasslands**, and especially **Wetlands** have seen the **lowest average changes**, suggesting relatively more stable thermal conditions over the past century.

These results help pinpoint **which ecosystems may be under the most pressure** from climate change — and where conservation efforts might be most urgently needed.
""")

st.markdown("---")

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x='Habitat Category', y='At_Risk', ax=ax)
ax.set_title("Proportion of At-Risk Species by Habitat Category", fontsize=17)
ax.set_ylabel("Proportion at Risk (0–1)", fontsize=17)
ax.set_xlabel("Habitat Category", fontsize=17)
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This barplot presents the **proportion of species labeled as "at risk"** (vulnerable, endangered, etc.) across each habitat type.

- **Freshwater habitats** have the **highest share of at-risk species**, with more than **60%** of species affected — highlighting them as a major conservation concern.
- **Tundra**, **Forests**, and **Oceans** also show elevated proportions, indicating that these ecosystems face considerable pressure.
- **Deserts**, **Mountains**, and **Grasslands** show relatively **lower risk levels**, though they still include a substantial number of vulnerable species.
- The error bars suggest that some categories — like **Wetlands** and **Tundra** — have **greater variability or uncertainty** in their risk proportions, which may reflect fewer data points or mixed habitat types.

This chart reinforces the need to **prioritize habitat-specific strategies** when addressing extinction risk and environmental policy.
""")

st.markdown("---")

# Title and intro
st.markdown("""
### **Impact of Social Structure on Extinction Risk and Climate Exposure**
This visual compares how different **social structures** are associated with:
- The **proportion of species that are at risk**, and  
- The **average temperature change** they experience.
""")

# Combined plot
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))

# Proportion at risk
sns.barplot(data=df, x='Social Structure', y='At_Risk', ax=axes[0])
axes[0].set_title('Proportion of At-Risk Species by Social Structure', fontsize=17)
axes[0].set_ylabel('At Risk (0–1)', fontsize=16)

# Average temperature change
sns.barplot(data=df, x='Social Structure', y='temp_change', ax=axes[1])
axes[1].set_title('Average Temperature Change by Social Structure', fontsize=17)
axes[1].set_ylabel('Temp Change (°C)', fontsize=16)

plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the charts above:**

These two barplots explore how different **social structures** among species relate to:

- **Extinction risk** (top plot), and  
- **Exposure to temperature change** (bottom plot).

#### **Proportion of At-Risk Species:**
- Species in **herd-based** and **social group** structures show **the highest proportion at risk**, often well above 60%.
- **Solitary** and **pack-based** animals fall in the mid-range, while **group-based** and **eusocial** species show the **lowest risk** — though some categories have high uncertainty (as seen in error bars).
- The high vulnerability among **herd-based animals** may reflect their reliance on stable group behavior, coordinated migration, or large territory needs.

####  **Average Temperature Change:**
- **Pack-based** and **colony-based** species have experienced the **highest average temperature increases**, nearing or exceeding **1.6 °C**.
- **Social pods** and **group-based** animals appear to inhabit more stable climates, with lower average temperature shifts.
- Interestingly, **eusocial** species (e.g., some insects) show **low risk and low climate exposure**, though this may be due to data limitations.

Overall, this suggests that **social behavior can influence both extinction vulnerability and environmental sensitivity**, with more complex or cooperative systems potentially being more fragile under pressure.
""")

# Assuming Social Structure has already been encoded as 'Social Encoded'
correlation_value = df[['Social Encoded', 'At_Risk']].corr().iloc[0, 1]

# Add under your previous charts
st.markdown("""
---
### **Is Social Structure Correlated with Extinction Risk?**
To further quantify the relationship, each social structure type was encoded as a numeric value and compared to extinction risk using a correlation analysis.
""")

# Show the correlation in a highlight box
st.info(f"**Correlation between Social Structure (Encoded) and At-Risk Status:** {correlation_value:.3f}")

# Interpretation
st.markdown("""
### **What we can observe from this result:**

- The correlation is **positive but weak** (**r = 0.11**), indicating a **slight tendency** for some social structures to be associated with higher extinction risk.
- While not a strong predictor on its own, it supports the pattern seen in the barplot: **certain social behaviors may influence species' vulnerability**, especially in changing environments.
- This also reflects the **complexity of social traits** — they're not linear, and some types (e.g. eusocial vs. pack-based) may face very different ecological pressures.

Overall, social structure contributes **some predictive signal**, but should be analyzed in combination with other biological and environmental factors.
""")

# Header
st.markdown("""
---
### **Temperature Change by Social Structure and At-Risk Status**
This boxplot explores how **climate exposure** varies across different **social structures**, while also separating animals that are **at risk** from those that are not.
""")

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Social Structure', y='temp_change', hue='At_Risk', ax=ax)
ax.set_title('Temp Change by Social Structure and At-Risk Status', fontsize=17)
ax.set_xlabel("Social Structure", fontsize=16)
ax.set_ylabel("Temperature Change (°C)", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This boxplot compares **temperature change (°C)** across different **social structures**, separated by whether species are **at risk** (orange) or not (blue).

- For **solitary** and **herd-based** species, those classified as *at risk* tend to experience **higher temperature changes**, suggesting a possible link between isolation/vulnerability and climate stress.
- In contrast, **group-based** and **social group** species show the **opposite pattern**, where *non-risk species* face more climate change — possibly reflecting broader geographic ranges or better adaptability.
- Some structures, like **colony-based** or **pack-based**, have **small sample sizes**, which may explain the narrow or missing boxplots.
- **Eusocial** and **varies** show little to no data, indicating either few species or inconsistent categorization in those groups.

Overall, this plot highlights how **climate exposure varies by social structure**, but the relationship is **not uniform** — extinction risk likely results from **a mix of social, ecological, and environmental pressures**.
""")

st.markdown("---")
# Plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x='Social Structure', hue='At_Risk', ax=ax)
ax.set_title("At-Risk vs Not At-Risk per Social Structure", fontsize=17)
ax.set_xlabel("Social Structure", fontsize=16)
ax.set_ylabel("Count", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
### **What we can observe from the chart:**

This countplot displays the **number of species** in each social structure category, divided by whether they are **at risk** (*orange*) or **not at risk** (*blue*).

- **Solitary animals** make up the largest portion of the dataset overall — and they also contribute heavily to both **at-risk and non-at-risk categories**.
- In **herd-based** and **group-based** species, we see fewer total observations, but still a **notable share of at-risk individuals**.
- **Social groups** are particularly interesting: despite a lower total count, they show a **nearly equal distribution** between risk categories.
- Other social structures such as **flocks**, **pack-based**, and **colony-based** show **smaller sample sizes**, but still include both at-risk and stable species.
- Categories like **eusocial**, **varies**, and **social pods** are **minimally represented**, possibly due to their rarity or underreporting in the dataset.

This plot provides important **context for previous proportions** by grounding them in actual **species counts**, helping us understand both **prevalence** and **risk distribution** across social systems.
""")

st.markdown("---")

st.markdown("""
### **Final Thoughts on Combined Animal & Climate Data Insights**

This project brought together two distinct datasets — one on **biological traits** and one on **regional climate change** — to investigate how various factors relate to species extinction risk.

The combined analysis reveals several key takeaways:

- Species marked as **"at risk"** often show differences in **reproduction rate**, **social structure**, and **habitat use** compared to non-threatened species.
- Certain **social systems** (e.g., *herd-based*, *social groups*) appear more vulnerable, potentially due to ecological dependence or group-based behaviors.
- While **temperature change** alone is not a perfect predictor, species living in **Tundra**, **Freshwater**, and **Mountain habitats** — areas with higher average warming — also show higher proportions of at-risk classification.
- **Solitary species** are by far the most represented in the dataset and make up a large portion of those facing extinction risk.
- The relationship between **diet** and **climate exposure** was complex, but species with specialized or combined diets (e.g. *carnivore + scavenger*) tended to show higher temperature variability.

⚠️ It's important to note that the dataset had **missing regional coverage** — especially underrepresented areas like **Oceania and parts of the Arctic**.  
This means some biodiversity hotspots may not be fully captured, which could underestimate extinction risks in those zones.

Overall, this analysis emphasizes the value of combining **biological and environmental data** to better understand extinction patterns.  
The more we identify which species are vulnerable — and why — the closer we get to taking **targeted conservation action before it's too late**.
""")

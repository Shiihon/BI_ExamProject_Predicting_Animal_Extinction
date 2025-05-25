# **Predicting animal extinction**

## In the face of accelerating biodiversity loss and climate change, this project aims to predict which animal species are at greatest risk of extinction by analyzing patterns in their biological traits and environmental conditions. It combines comprehensive datasets of species-specific characteristics (e.g., lifespan, reproductive rate, habitat type, diet, conservation status) with historical climate data (such as country-level temperature trends) to incorporate both intrinsic biological factors and external environmental pressures into the analysis. Using this integrated data, the project employs a suite of analytical techniques—including classification algorithms (such as Decision Tree models), clustering analysis, and data visualization tools—to identify key patterns and build a predictive model for extinction risk. By highlighting vulnerable species before they become critically endangered, this data-driven approach provides early warning insights and underscores the importance of predictive modeling in guiding biodiversity conservation efforts.

### **Research questions**
* Can we build a model that predicts which animals are likely to become endangered next?
* Which traits (biological or environmental) are the strongest indicators of future extinction risk?
* Is there a measurable link between rising climate pressure (e.g. temperature increase) and species vulnerability?
* How does the combination of climate data and species-specific features improve prediction compared to using only one data type?

### **Hypothesis**
* Animals with low reproductive output (few offspring, long gestation) are more likely to face extinction.
* Species located in countries with sharply rising temperatures are at higher risk.
* Carnivorous species are more vulnerable due to higher food chain dependence and niche sensitivity.
* Habitat type and social structure will improve extinction prediction accuracy when modeled alongside climate data.
* A model combining both biological and climate indicators will outperform single-source models.

### **Data Sources**
* [Animal Dataset(Kaggle)](https://www.kaggle.com/datasets/iamsouravbanerjee/animal-information-dataset?resource=download)

* [Climate Dataset (World Bank Climate Change Data Portal)](https://climateknowledgeportal.worldbank.org/download-data)

### **Description of both datasets**
#### ***Animal Dataset***
* The animal dataset contains biological and ecological information about a wide range of animal species. Each record includes features such as conservation status, body mass, lifespan, diet, reproductive traits, and geographical distribution. One of the key columns, Country Found, includes a mix of specific countries (e.g., Kenya, India) and broad regions (e.g., Africa, Asia), which presented a challenge for direct geographical alignment with climate data.

Data Sources
Description of both datasets

Cleaning + Region Mapping

Exploration Summary
Visuals + insights (from Sprint 2)

Model Building
Methods used

Feature engineering

Performance comparison

Results & Insights
Which traits mattered most?

Did climate really add predictive power?

Any surprises?

Conclusion
Answer research questions

Evaluate hypothesis

Suggest real-world implications
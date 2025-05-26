# **Predicting animal extinction**

## In a time where biodiversity is declining and climate change is speeding up, this project set out to figure out which animal species might be next in line for extinction. To do that, it brings together two types of information:

- Biological traits of animals — like how long they live, how many babies they have, what they eat, and where they live

- And climate data — especially how temperatures have been changing over time in different parts of the world

## By combining these two datasets, the project looks at both the internal traits of species and the external pressures they’re facing. Using a mix of tools like decision tree models, clustering, and visualizations, it identifies patterns and builds models that can help predict which species are at risk.

## The goal? To spot warning signs early — ideally before a species becomes critically endangered.
This kind of data-driven approach can give conservation efforts a head start, helping focus attention where it’s needed most, and showing the value of using prediction to protect biodiversity.

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

#### ***Climate Dataset***
* The climate dataset includes climate indicators (e.g., temperature change, CO₂ levels, precipitation) associated with specific countries. Unlike the animal dataset, this dataset uses only standardized country names without any regional aggregates.

### **Regional Mapping and Merging Strategy**
#### To connect the two datasets for analysis, a unified geographical structure was necessary. Since the animal dataset included both countries and regions while the climate dataset only referenced countries, a preprocessing step was performed:
* Five geographical regions were defined: Africa, Asia, Europe, Americas, and Oceania.

* All countries in the climate dataset were assigned to one of these five regions.

* Animals were also mapped to these regions based on the countries or regions listed in the Country Found column.

* Each animal was duplicated for every region it was found in. For example, if an animal existed in both Africa and Asia, it appeared in the dataset twice, once for each region.

* These duplicates were later removed to ensure a clean dataset, resulting in a one-to-one mapping per region per animal.

---

### **Considerations and Limitations**
#### This regional mapping allowed for the datasets to be merged effectively on a shared geographical level (region). However, this approach introduces certain limitations:

* By generalizing location data from specific countries to broader regions, some granularity is lost. Localized climate effects might not align perfectly with region-wide averages.

* The presence of duplicates due to multi-region presence of animals introduced redundancy, which had to be addressed during preprocessing.

* A more precise solution would have involved mapping each animal to every country it exists in and then joining with exact country-level climate data. Due to time constraints, this was not feasible in the current project scope, but it is a clear direction for future work to improve the precision and reliability of the analysis.

---

## Endangered Species Prediction – Summary of Findings

This project explored whether it's possible to predict species extinction risk using a combination of **biological traits** and **climate data**.  
By merging an animal dataset with global temperature trends, we investigated how climate pressure interacts with species-specific traits like diet, habitat, social structure, and reproduction.

---

### Research Questions

**1. Can we build a model that predicts which animals are likely to become endangered next?**  
 - Yes – the combined dataset enabled the creation of predictive models with measurable accuracy.  
 Models using biological traits alone performed reasonably well, and performance improved further when climate features were added. This shows it is **feasible to predict extinction risk**, although results vary depending on available features.

**2. Which traits (biological or environmental) are the strongest indicators of future extinction risk?**  
 - **Reproductive rate** (e.g., offspring per birth) showed a strong signal: species with fewer offspring tended to be more at risk.  
 - **Social structure** also mattered — herd-based and group-dependent animals had higher risk proportions.  
 - **Habitat type** helped differentiate risk levels, especially in areas like Freshwater and Tundra regions.  
 - While **temperature change** was not the strongest single predictor, it was consistently higher in some of the most vulnerable habitats.

**3. Is there a measurable link between rising climate pressure (e.g. temperature increase) and species vulnerability?**  
 - Partially.  
 On average, at-risk species were found in slightly warmer and more climate-affected regions (e.g., Mountains, Tundra, Freshwater). However, temperature change alone was not a strong predictor — its value was clearer when combined with biological traits.

**4. How does the combination of climate data and species-specific features improve prediction compared to using only one data type?**  
 - Models using both data types **outperformed single-source models**.  
 Biological-only models captured species-specific risk factors, while climate-only models were too broad. The combined model showed better feature diversity and more balanced performance, especially in edge cases.

---

### Hypothesis Review

| Hypothesis                                                                                         | Outcome      |
|----------------------------------------------------------------------------------------------------|--------------|
| Animals with low reproductive output are more likely to face extinction.                           | ✅ Supported  |
| Species in regions with sharply rising temperatures are at higher risk.                            | ⚠️ Partially supported |
| Carnivorous species are more vulnerable due to food chain and niche dependence.                    | ⚠️ Mixed – some evidence, but not strong alone |
| Habitat type and social structure improve extinction prediction when modeled with climate data.    | ✅ Supported  |
| A combined model of biological + climate traits outperforms single-source models.                  | ✅ Strongly supported  |

---

### ⚠️ Data Limitations

- Some regions — especially **Oceania**, **Arctic zones**, and **island habitats** — were underrepresented in the dataset.
- Many species had **missing or incomplete trait data**, particularly for social structure and reproductive rate.
- Climate data was regionalized and averaged, which may have **blurred local effects**.

---

### Conclusion

This analysis confirms that extinction risk is a **multifactorial issue**, influenced by a mix of biological traits and climate dynamics.  
The best predictive power comes from **combining both domains**, which helps account for individual species behavior **and** external environmental pressure.

With better data coverage and refinement, this kind of modeling could meaningfully support **early warning systems for conservation**.

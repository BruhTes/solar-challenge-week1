# Solar Challenge Week 1

This repository contains the code, analysis, and environment setup for Week 1 of the Solar Challenge project. The goal of this challenge is to perform exploratory data analysis (EDA) on solar farm data from Benin, Sierra Leone, and Togo to support MoonLight Energy Solutions in identifying high-potential regions for solar energy installations.
This repository contains setup and configuration for Week-1 of the Solar Challenge project.

## Project Overview

MoonLight Energy Solutions aims to enhance operational efficiency and sustainability through data-driven solar investments. This week’s challenge focuses on cleaning, profiling, and exploring solar radiation data collected from different regions. The analysis includes:

- Data cleaning and missing value imputation
- Outlier detection and handling
- Time series and statistical analysis of solar irradiance, temperature, wind, and humidity
- Assessing the impact of cleaning events on sensor performance
- Visualizations such as correlation heatmaps, scatter plots, and wind rose charts
- Delivering actionable insights and strategic recommendations for solar farm deployment

## Project Contributions

This repository includes:

### Environment setup and CI pipeline:
- Virtual environment configuration
- `.gitignore` to exclude sensitive and bulky files
- GitHub Actions workflow to automate dependency installation and testing

### Exploratory Data Analysis (EDA):
- Summary statistics and missing value reports for each country dataset
- Outlier detection using Z-scores and subsequent cleaning/imputation
- Time series visualizations to analyze solar irradiance and temperature trends
- Analysis of the effect of cleaning events on sensor readings
- Correlation and scatter plots to reveal relationships between weather parameters
- Wind speed and direction visualizations (wind rose plots)
- Bubble charts combining multiple environmental factors to highlight insights

### Documentation:
- Clear instructions to reproduce environment and run analysis
- Well-organized project structure for scalability and collaboration


## 📊 Interactive Dashboard
An interactive dashboard has been developed using Streamlit to visualize and compare key insights across Benin, Sierra Leone, and Togo, based on the exploratory data analysis.

### 🔗 Access the Dashboard
[🔗 Launch the Dashboard]()

### 💻 Run Locally
To run the dashboard on your local machine:

- Ensure all dependencies in requirements.txt are installed.
- Confirm the cleaned datasets are placed inside the data/ directory.

Run the following command from the root of the project:

```bash
streamlit run app/main.py
```
### 🧩 Dashboard Features

- ✅ Country Selection: Select one or more countries for comparison.

- 📊 Interactive Visualizations:
     -- Boxplots for GHI, DNI, temperature, and humidity.
     -- Time series trends for solar irradiance and weather variables.

- 🏆 Performance Ranking:

- Summary table ranking regions based on KPIs (e.g., GHI, DNI).

- 📈 Metric Comparison Viewer: Time series explorer with dynamic filters.

### 🖼️ Dashboard Screenshots
Screenshots from the deployed app are available below:
![screencapture-localhost-8502-2025-05-21-21_36_28](https://github.com/user-attachments/assets/a05f90f7-83e1-442b-8d39-658a7259fc1e)

---

## How to Run

- Activate the virtual environment and install dependencies as described below.
- Navigate to the `notebooks/` folder and open any `<country>_eda.ipynb` notebook with Jupyter or VSCode.
- Run the cells sequentially to explore the data, visualizations, and analyses.
- Cleaned data is exported to the `data/` folder but is excluded from Git tracking.


## Reproducing the Development Environment

Follow the steps below to set up the project environment on your local machine:

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1
```

### **2. Create a Virtual Environment**

``` bash
python -m venv .venv
```
#### If python does not work, try using py:

```bash
py -m venv .venv
```

### **3. Activate the Virtual Environment**

```bash
.venv\Scripts\activate
```
   #### You should now see a (.venv) at the start of your terminal prompt

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
``` 

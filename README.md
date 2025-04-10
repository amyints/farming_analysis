# Farming and Agriculture Analysis

**GitHub Repository** -
https://github.com/amyints/farming_analysis/tree/main#

**Farming and Agricultural Practices Dashboard (Tableau)**
https://public.tableau.com/app/profile/alayah.shaw/viz/FarmingandAgriculturePractices/ApplicationEfficiencyDashboard?publish=yes

**Agriculture and Farming Dataset (Kaggle)**
https://www.kaggle.com/datasets/bhadramohit/agriculture-and-farming-dataset/code

## Raw Data file (agriculture_dataset.csv) located in data folder

# Run this Project
To run this project:
* clone the Git Repository
* connect to WSL: Ubuntu
* run a new WSL terminal and run `python main.py`

## Cleaning.py
* load raw dataset
* drop duplicates
* identify missing values
* identify outliers
* create new columns:
    * fertilizer_to_yield_ratio
    * pesticide_to_yield_ratio
    * water_to_yield_ratio
    * fertilizer_to_acre_ratio
    * pesticide_to_acre_ratio
    * water_to_acre_ratio
* select the top 3 crops
* return cleaned dataset and top 3 crops

##  Analysis.py
* Create 5 analysis functions to find the correlation and statistical significance for the top 3 crops
    * fertilizer to yield correlation
    * pesticide to yield correlation
    * water to yield correlation
    * irrigation type to yield correlation
    * soil type to yield correlation
* return the correlation and p-value for each input factor

# Modeling.py
* Train the data modeling using the features:
    * Fertilizer_Used(tons)
    * Pesticide_Used(kg)
    * Water_Usage(cubic meters)
    * fertilizer_to_yield_ratio
    * pesticide_to_yield_ratio
    * water_to_yield_ratio
    * fertilizer_to_acre_ratio
    * pesticide_to_acre_ratio
    * water_to_acre_ratio

* Initialize and train model using a StackingRegressor with the following regression models:
    * RandomForestRegressor
    * GradientBoostingRegressor
    * ExtraTreesRegressor
    * StandardScaler
    * KNeighborsRegressor
    * XGBRegressor
* Hyperparameters are fine-tuned achieve the following criteria:
    * R-squared value >= 0.80
    * Low MAE
    * Low RMSE
* Return the following:
    * trained model
    * predictions
    * X_train
    * X_test
    * y_train
    * y_test

## Simulating.py
* Generate a range of possible values for input factors
* Create a grid of all combinations to display scenarios
* Compute ratio features to simulate changes in factors
* Create a column for the predicted yield based on ratio features
* return scenarios

## Main.py
* Calls functions to clean, analyze, model, and simulate data.
* Function to remove data is called but commented out until user decides to delete raw and cleaned data

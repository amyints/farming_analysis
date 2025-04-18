import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
from scipy import stats
from scipy.stats import pearsonr



def data_cleaning(df_path):

    # Load the dataset
    df = pd.read_csv(df_path)
    clean_df = df.copy()

    # Drop missing values
    clean_df.dropna(inplace=True)
    print(f"Missing Values: \n{clean_df.isna().sum()}")

    # Drop duplicates
    clean_df.drop_duplicates(inplace=True)

    # Find outliers
    clean_df['z_score'] = np.abs(stats.zscore(clean_df['Yield(tons)']))
    outliers = clean_df[clean_df['z_score'] > 3]
    print(f"Number of outliers detected: {outliers.shape[0]}")

    # Remove Outliers
    clean_df = clean_df[clean_df['z_score'] <= 3]


    # Create a new column for the Fertilizer Usage to Crop Yield ratio
    clean_df['fertilizer_to_yield_ratio'] = clean_df['Yield(tons)'] / clean_df['Fertilizer_Used(tons)']
    clean_df['pesticide_to_yield_ratio'] = clean_df['Yield(tons)'] / clean_df['Pesticide_Used(kg)']
    clean_df['water_to_yield_ratio'] = clean_df['Yield(tons)'] / clean_df['Water_Usage(cubic meters)']
    clean_df['fertilizer_to_acre_ratio'] = clean_df['Fertilizer_Used(tons)'] / clean_df['Farm_Area(acres)']
    clean_df['pesticide_to_acre_ratio'] = clean_df['Pesticide_Used(kg)'] / clean_df['Farm_Area(acres)']
    clean_df['water_to_acre_ratio'] = clean_df['Water_Usage(cubic meters)'] / clean_df['Farm_Area(acres)']



    # Select top 3 crops
    popular_by_yield = clean_df.groupby('Crop_Type')['Yield(tons)'].sum().sort_values(ascending=False)
    top_3_crops = popular_by_yield.head(3).index.tolist()
    print(f"Top 3 crops by yield: {top_3_crops}")

    return clean_df, top_3_crops



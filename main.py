from cleaning import data_cleaning
from analysis import fertilizer_correlation, pesticide_correlation, water_correlation

# clean data using cleaning.py
df_path = "./data/agriculture_dataset.csv"
clean_df, top_5_crops = data_cleaning(df_path)
print(f"These top 5 crop will be referenced to analyze: {top_5_crops}")
clean_df.to_csv("./data/cleaned_agriculture_dataset.csv", index=False )

# Fertilizer Correlation and Statistical Significance
print("---FERTILIZER CORRELATION---\n")
fertilizer_correlation(clean_df, f"{top_5_crops[0]}")
fertilizer_correlation(clean_df, f"{top_5_crops[1]}")
fertilizer_correlation(clean_df, f"{top_5_crops[2]}")


# Pesticide Correlation and Statistical Significance
print("---PESTICIDE CORRELATION---\n")
pesticide_correlation(clean_df, f"{top_5_crops[0]}")
pesticide_correlation(clean_df, f"{top_5_crops[1]}")
pesticide_correlation(clean_df, f"{top_5_crops[2]}")


# Water Usage Correlation and Statistical Significance
print("---WATER CORRELATION---\n")
water_correlation(clean_df, f"{top_5_crops[0]}")
water_correlation(clean_df, f"{top_5_crops[1]}")
water_correlation(clean_df, f"{top_5_crops[2]}")

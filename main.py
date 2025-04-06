from cleaning import data_cleaning
from analysis import fertilizer_correlation, pesticide_correlation, water_correlation, irrigation_correlation, soil_correlation
from model.modeling import data_modeling

# clean data using cleaning.py
df_path = "./data/agriculture_dataset.csv"
clean_df, top_3_crops, encoded_df = data_cleaning(df_path)
print(f"These top 3 crop will be referenced to analyze: {top_3_crops}")
clean_df.to_csv("./data/cleaned_agriculture_dataset.csv", index=False )

# Fertilizer Correlation and Statistical Significance
print("---FERTILIZER CORRELATION---\n")
fertilizer_correlation(clean_df, f"{top_3_crops[0]}")
fertilizer_correlation(clean_df, f"{top_3_crops[1]}")
fertilizer_correlation(clean_df, f"{top_3_crops[2]}")


# Pesticide Correlation and Statistical Significance
print("---PESTICIDE CORRELATION---\n")
pesticide_correlation(clean_df, f"{top_3_crops[0]}")
pesticide_correlation(clean_df, f"{top_3_crops[1]}")
pesticide_correlation(clean_df, f"{top_3_crops[2]}")


# Water Usage Correlation and Statistical Significance
print("---WATER CORRELATION---\n")
water_correlation(clean_df, f"{top_3_crops[0]}")
water_correlation(clean_df, f"{top_3_crops[1]}")
water_correlation(clean_df, f"{top_3_crops[2]}")

#print(clean_df.columns.to_list())


# Irrigation Type Correlation and Statistical Significance
irrigation_correlation(clean_df, top_3_crops[0])
irrigation_correlation(clean_df, top_3_crops[1])
irrigation_correlation(clean_df, top_3_crops[2])

# Soil Type Correlation and Statistical Significance
soil_correlation(clean_df, top_3_crops[0])
soil_correlation(clean_df, top_3_crops[1])
soil_correlation(clean_df, top_3_crops[2])

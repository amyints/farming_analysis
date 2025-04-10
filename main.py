from cleaning import data_cleaning
from analysis import fertilizer_correlation, pesticide_correlation, water_correlation, irrigation_correlation, soil_correlation
from model.modeling import data_modeling
from model.simulating import simulate
from data.deleting import remove_data

# clean data using cleaning.py
df_path = "./data/agriculture_dataset.csv"
clean_df, top_3_crops = data_cleaning(df_path)
print(f"These top 3 crop will be referenced to analyze: {top_3_crops}")
clean_df.to_csv("./data/cleaned_agriculture_dataset.csv", index=False)

# Fertilizer Correlation and Statistical Significance
print("---FERTILIZER CORRELATION---")
fert_stat_sig = []
fert_not_stat_sig = []
fert_stat_sig1, fert_not_stat_sig1, fcorr1, fpval1 = fertilizer_correlation(clean_df, f"{top_3_crops[0]}")
fert_stat_sig.append(fert_stat_sig1)
fert_not_stat_sig.append(fert_not_stat_sig1)

fert_stat_sig2, fert_not_stat_sig2, fcorr2, fpval2 = fertilizer_correlation(clean_df, f"{top_3_crops[1]}")
fert_stat_sig.append(fert_stat_sig2)
fert_not_stat_sig.append(fert_not_stat_sig2)

fert_stat_sig3, fert_not_stat_sig3, fcorr3, fpval3 = fertilizer_correlation(clean_df, f"{top_3_crops[2]}")
fert_stat_sig.append(fert_stat_sig3)
fert_not_stat_sig.append(fert_not_stat_sig3)
print(f"Crops with a statistically significant correlation with fertilizer usage: {fert_stat_sig}")
print(f"Crops with no statistically significant correlation with fertilizer usage: {fert_not_stat_sig}\n")
print('')

# Pesticide Correlation and Statistical Significance
print("---PESTICIDE CORRELATION---")
pest_stat_sig = []
pest_not_stat_sig = []
pest_stat_sig1, pest_not_stat_sig1, pcorr1, ppval1 = pesticide_correlation(clean_df, f"{top_3_crops[0]}")
pest_stat_sig.append(pest_stat_sig1)
pest_not_stat_sig.append(pest_not_stat_sig1)

pest_stat_sig2, pest_not_stat_sig2, pcorr2, ppval2 = pesticide_correlation(clean_df, f"{top_3_crops[1]}")
pest_stat_sig.append(pest_stat_sig2)
pest_not_stat_sig.append(pest_not_stat_sig2)

pest_stat_sig3, pest_not_stat_sig3, pcorr3, ppval3 = pesticide_correlation(clean_df, f"{top_3_crops[2]}")
pest_stat_sig.append(pest_stat_sig3)
pest_not_stat_sig.append(pest_not_stat_sig3)
print(f"Crops with a statistically significant correlation with pesticide usage: {pest_stat_sig}")
print(f"Crops with no statistically significant correlation with pesticide usage: {pest_not_stat_sig}")
print('')

# Water Usage Correlation and Statistical Significance
print("---WATER CORRELATION---")
water_stat_sig = []
water_not_stat_sig = []

water_stat_sig1, water_not_stat_sig1, wcorr1, wpval1 = water_correlation(clean_df, f"{top_3_crops[0]}")
water_stat_sig.append(water_stat_sig1)
water_not_stat_sig.append(water_not_stat_sig1)

water_stat_sig2, water_not_stat_sig2, wcorr2, wpval2 = water_correlation(clean_df, f"{top_3_crops[1]}")
water_stat_sig.append(water_stat_sig2)
water_not_stat_sig.append(water_not_stat_sig2)

water_stat_sig3, water_not_stat_sig3, wcorr2, wpval2 = water_correlation(clean_df, f"{top_3_crops[2]}")
water_stat_sig.append(water_stat_sig3)
water_not_stat_sig.append(water_not_stat_sig3)
print(f"Crops with a statistically significant correlation with water usage: {water_stat_sig}")
print(f"Crops with no statistically significant correlation with water usage: {water_not_stat_sig}")
print('')

#print(clean_df.columns.to_list())

print("---IRRIGATION CORRELATION---")
# Irrigation Type Correlation and Statistical Significance
irri_stat_sig = []
irri_not_stat_sig = []

irri_stat_sig1, irri_not_stat_sig1 = irrigation_correlation(clean_df, top_3_crops[0])
irri_stat_sig.append(irri_stat_sig1)
irri_not_stat_sig.append(irri_not_stat_sig1)

irri_stat_sig2, irri_not_stat_sig2 = irrigation_correlation(clean_df, top_3_crops[1])
irri_stat_sig.append(irri_stat_sig2)
irri_not_stat_sig.append(irri_not_stat_sig2)

irri_stat_sig3, irri_not_stat_sig3 = irrigation_correlation(clean_df, top_3_crops[2])
irri_stat_sig.append(irri_stat_sig3)
irri_not_stat_sig.append(irri_not_stat_sig3)

print(f"Crops with a statistically significant correlation with irrigation type: {irri_stat_sig}")
print(f"Crops with no statistically significant correlation with irrigation type: {irri_not_stat_sig}")
print('')

print("---SOIL CORRELATION---")
# Soil Type Correlation and Statistical Significance
soil_stat_sig = []
soil_not_stat_sig = []

soil_stat_sig1, soil_not_stat_sig1 = soil_correlation(clean_df, top_3_crops[0])
soil_stat_sig.append(soil_stat_sig1)
soil_not_stat_sig.append(soil_not_stat_sig1)

soil_stat_sig2, soil_not_stat_sig2 = soil_correlation(clean_df, top_3_crops[1])
soil_stat_sig.append(soil_stat_sig2)
soil_not_stat_sig.append(soil_not_stat_sig2)

soil_stat_sig3, soil_not_stat_sig3 = soil_correlation(clean_df, top_3_crops[2])
soil_stat_sig.append(soil_stat_sig3)
soil_not_stat_sig.append(soil_not_stat_sig3)

print(f"Crops with a statistically significant correlation with soil type: {soil_stat_sig}")
print(f"Crops with no statistically significant correlation with soil type: {soil_not_stat_sig}")
print('')

model, predictions, X_train, X_test, y_train, y_test = data_modeling(clean_df)

simulator = simulate(clean_df, model)
#remove_data(df_path, "./data/cleaned_agriculture_dataset.csv")
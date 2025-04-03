from cleaning import data_cleaning

df_path = "./data/agriculture_dataset.csv"
clean_df, top_3_crops = data_cleaning(df_path)
print(f"These top 3 crop will be referenced to analyze: {top_3_crops}")
clean_df.to_csv("./data/cleaned_agriculture_dataset.csv", index=False )
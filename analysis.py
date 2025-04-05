from scipy.stats import pearsonr

def fertilizer_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    corr, pval = pearsonr(crop_df['fertilizer_to_yield_ratio'], crop_df['Yield(tons)'])
    print(f"Correlation between fertilizer usage and {crop_name} yield: {corr:.1f}")
    print(f"P-Value: {pval}")
    
    # Identify whether there is a statistically significant correlation
    if pval <= 0.5:
        print(f"There is a statistically significant correlation between fertilizer usage and {crop_name} yield.")
    else:
        print(f"There is not a statistically significant correlation between fertilizer usage and {crop_name} yield.")
    
    # Identify the type of correlation
    if corr == 1:
        print(f"There is a perfect, positive correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr >= 0.7:
        print(f"There is a strong, positive correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr >= 0.4:
        print(f"There is a moderate, positive correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr >= 0.1:
        print(f"There is a weak, positive correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr > -0.1:
        print(f"There is no correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr >= -0.3:
        print(f"There is a weak, negative correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr >= -0.6:
        print(f"There is a moderate, negative correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr >= -0.9:
        print(f"There is a strong, negative correlation between fertilizer usage and {crop_name} yield.\n")
    elif corr == -1:
        print(f"There is a perfect, negative correlation between fertilizer usage and {crop_name} yield.\n")

    return

def pesticide_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    corr, pval = pearsonr(crop_df['pesticide_to_yield_ratio'], crop_df['Yield(tons)'])
    print(f"Correlation between pesticide usage and {crop_name} yield: {corr:.1f}")
    print(f"P-Value: {pval:.2f}")

    # Identify whether there is a statistically significant correlation
    if pval <= 0.5:
        print(f"There is a statistically significant correlation between pesticide usage and {crop_name} yield.")
    else:
        print(f"There is not a statistically significant correlation between pesticide usage and {crop_name} yield.")
    
    # Identify the type of correlation
    if corr == 1:
        print(f"There is a perfect, positive correlation between pesticide usage and {crop_name} yield.\n")
    elif corr >= 0.7:
        print(f"There is a strong, positive correlation between pesticide usage and {crop_name} yield.\n")
    elif corr >= 0.4:
        print(f"There is a moderate, positive correlation between pesticide usage and {crop_name} yield.\n")
    elif corr >= 0.1:
        print(f"There is a weak, positive correlation between pesticide usage and {crop_name} yield.\n")
    elif corr > -0.1:
        print(f"There is no correlation between pesticide usage and {crop_name} yield.\n")
    elif corr >= -0.3:
        print(f"There is a weak, negative correlation between pesticide usage and {crop_name} yield.\n")
    elif corr >= -0.6:
        print(f"There is a moderate, negative correlation between pesticide usage and {crop_name} yield.\n")
    elif corr >= -0.9:
        print(f"There is a strong, negative correlation between pesticide usage and {crop_name} yield.\n")
    elif corr == -1:
        print(f"There is a perfect, negative correlation between pesticide usage and {crop_name} yield.\n")

    return
    
def water_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    corr, pval = pearsonr(crop_df['water_to_yield_ratio'], crop_df['Yield(tons)'])
    print(f"Correlation between water usage and {crop_name} yield: {corr:.1f}")
    print(f"P-Value: {pval:.2f}")

    # Identify whether there is a statistically significant correlation
    if pval <= 0.5:
        print(f"There is a statistically significant correlation between water usage and {crop_name} yield.")
    else:
        print(f"There is not a statistically significant correlation between water usage and {crop_name} yield.")
    
    # Identify the type of correlation
    if corr == 1:
        print(f"There is a perfect, positive correlation between water usage and {crop_name} yield.\n")
    elif corr >= 0.7:
        print(f"There is a strong, positive correlation between water usage and {crop_name} yield.\n")
    elif corr >= 0.4:
        print(f"There is a moderate, positive correlation between water usage and {crop_name} yield.\n")
    elif corr >= 0.1:
        print(f"There is a weak, positive correlation between water usage and {crop_name} yield.\n")
    elif corr > -0.1:
        print(f"There is no correlation between water usage and {crop_name} yield.\n")
    elif corr >= -0.3:
        print(f"There is a weak, negative correlation between water usage and {crop_name} yield.\n")
    elif corr >= -0.6:
        print(f"There is a moderate, negative correlation between water usage and {crop_name} yield.\n")
    elif corr >= -0.9:
        print(f"There is a strong, negative correlation between water usage and {crop_name} yield.\n")
    elif corr == -1:
        print(f"There is a perfect, negative correlation between water usage and {crop_name} yield.\n")

    return
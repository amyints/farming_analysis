from scipy.stats import pearsonr, f_oneway

# FERTILIZER CORRELATION
def fertilizer_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    corr, pval = pearsonr(crop_df['fertilizer_to_yield_ratio'], crop_df['Yield(tons)'])
    print(f"Correlation between fertilizer usage and {crop_name} yield: {corr:.1f}")
    print(f"P-Value: {pval}")
    
    stat_sig = None
    not_stat_sig = None

    # Identify whether there is a statistically significant correlation
    if pval <= 0.5:
        stat_sig = crop_name
        #print(f"There is a statistically significant correlation between fertilizer usage and {crop_name} yield.")
    else:
        not_stat_sig = crop_name
        #print(f"There is not a statistically significant correlation between fertilizer usage and {crop_name} yield.")
    
    # Identify the type of correlation
    if corr == 1:
        print(f"There is a perfect, positive correlation between fertilizer usage and {crop_name} yield.")
    elif corr >= 0.7:
        print(f"There is a strong, positive correlation between fertilizer usage and {crop_name} yield.")
    elif corr >= 0.4:
        print(f"There is a moderate, positive correlation between fertilizer usage and {crop_name} yield.")
    elif corr >= 0.1:
        print(f"There is a weak, positive correlation between fertilizer usage and {crop_name} yield.")
    elif corr > -0.1:
        print(f"There is no correlation between fertilizer usage and {crop_name} yield.")
    elif corr >= -0.3:
        print(f"There is a weak, negative correlation between fertilizer usage and {crop_name} yield.")
    elif corr >= -0.6:
        print(f"There is a moderate, negative correlation between fertilizer usage and {crop_name} yield.")
    elif corr >= -0.9:
        print(f"There is a strong, negative correlation between fertilizer usage and {crop_name} yield.")
    elif corr == -1:
        print(f"There is a perfect, negative correlation between fertilizer usage and {crop_name} yield.")

    print('')
    return stat_sig, not_stat_sig, corr, pval

# PESTICIDE CORRELATION
def pesticide_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    corr, pval = pearsonr(crop_df['pesticide_to_yield_ratio'], crop_df['Yield(tons)'])
    print(f"Correlation between pesticide usage and {crop_name} yield: {corr:.1f}")
    print(f"P-Value: {pval:.2f}")

    stat_sig = None
    not_stat_sig = None

    # Identify whether there is a statistically significant correlation
    if pval <= 0.5:
        stat_sig = crop_name
        #print(f"There is a statistically significant correlation between pesticide usage and {crop_name} yield.")
    else:
        not_stat_sig = crop_name
        #print(f"There is not a statistically significant correlation between pesticide usage and {crop_name} yield.")
    
    # Identify the type of correlation
    if corr == 1:
        print(f"There is a perfect, positive correlation between pesticide usage and {crop_name} yield.")
    elif corr >= 0.7:
        print(f"There is a strong, positive correlation between pesticide usage and {crop_name} yield.")
    elif corr >= 0.4:
        print(f"There is a moderate, positive correlation between pesticide usage and {crop_name} yield.")
    elif corr >= 0.1:
        print(f"There is a weak, positive correlation between pesticide usage and {crop_name} yield.")
    elif corr > -0.1:
        print(f"There is no correlation between pesticide usage and {crop_name} yield.")
    elif corr >= -0.3:
        print(f"There is a weak, negative correlation between pesticide usage and {crop_name} yield.")
    elif corr >= -0.6:
        print(f"There is a moderate, negative correlation between pesticide usage and {crop_name} yield.")
    elif corr >= -0.9:
        print(f"There is a strong, negative correlation between pesticide usage and {crop_name} yield.")
    elif corr == -1:
        print(f"There is a perfect, negative correlation between pesticide usage and {crop_name} yield.")

    print('')
    return stat_sig, not_stat_sig, corr, pval
    
# WATER CORRELATION
def water_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    corr, pval = pearsonr(crop_df['water_to_yield_ratio'], crop_df['Yield(tons)'])
    print(f"Correlation between water usage and {crop_name} yield: {corr:.1f}")
    print(f"P-Value: {pval:.2f}")

    stat_sig = None
    not_stat_sig = None

    # Identify whether there is a statistically significant correlation
    if pval <= 0.5:
        stat_sig = crop_name
        #print(f"There is a statistically significant correlation between water usage and {crop_name} yield.")
    else:
        not_stat_sig = crop_name
        #print(f"There is not a statistically significant correlation between water usage and {crop_name} yield.")
    
    # Identify the type of correlation
    if corr == 1:
        print(f"There is a perfect, positive correlation between water usage and {crop_name} yield.")
    elif corr >= 0.7:
        print(f"There is a strong, positive correlation between water usage and {crop_name} yield.")
    elif corr >= 0.4:
        print(f"There is a moderate, positive correlation between water usage and {crop_name} yield.")
    elif corr >= 0.1:
        print(f"There is a weak, positive correlation between water usage and {crop_name} yield.")
    elif corr > -0.1:
        print(f"There is no correlation between water usage and {crop_name} yield.")
    elif corr >= -0.3:
        print(f"There is a weak, negative correlation between water usage and {crop_name} yield.")
    elif corr >= -0.6:
        print(f"There is a moderate, negative correlation between water usage and {crop_name} yield.")
    elif corr >= -0.9:
        print(f"There is a strong, negative correlation between water usage and {crop_name} yield.")
    elif corr == -1:
        print(f"There is a perfect, negative correlation between water usage and {crop_name} yield.")

    print('')
    return stat_sig, not_stat_sig, corr, pval

# IRRIGATION TYPE CORRELATION
def irrigation_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    groups = [group['Yield(tons)'].values for name, group in crop_df.groupby('Irrigation_Type')]
    fstat, pval = f_oneway(*groups)
    print(f"ANOVA for Irrigation Type ({crop_name}): F = {fstat:.2f}, p = {pval:.2f}")

    stat_sig = []
    not_stat_sig = []

    if pval > 0.05:
        stat_sig.append(crop_name)
        #print(f"The P-Value suggests that the differences in {crop_name} yield between irrigation types is not statistically significant.\n")
    else:
        not_stat_sig.append(crop_name)
        #print(f"The P-Value suggests that the differences in {crop_name} yield between irrigation types is statistically significant.\n")

    return stat_sig, not_stat_sig

# SOIL TYPE CORRELATION
def soil_correlation(df, crop_name):
    crop_df = df[df['Crop_Type'] == crop_name]
    groups = [group['Yield(tons)'].values for name, group in crop_df.groupby('Soil_Type')]
    fstat, pval = f_oneway(*groups)
    print(f"ANOVA for Soil Type ({crop_name}): F = {fstat:.2f}, p = {pval:.2f}")

    stat_sig = []
    not_stat_sig = []

    if pval > 0.05:
        stat_sig.append(crop_name)
        #print(f"The P-Value suggests that the differences in {crop_name} yield between soil types is not statistically significant.\n")
    else:
        not_stat_sig.append(crop_name)
        #print(f"The P-Value suggests that the differences in {crop_name} yield between soil types is statistically significant.\n")
    
    return stat_sig, not_stat_sig
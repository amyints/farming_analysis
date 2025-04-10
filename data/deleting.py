import os

def remove_data(raw_df, clean_df):
    # Remove raw dataset
    if os.path.exists(raw_df):
        os.remove(raw_df)
        print(f'Raw dataset ({raw_df}) deleted successfully.')
    else:
        print(f"File '{raw_df}' not found.")

    # Remove cleaned dataset
    if os.path.exists(clean_df):
        os.remove(clean_df)
        print(f'Cleaned dataset ({clean_df}) deleted successfully.')
    else:
        print(f"File '{clean_df}' not found.")
    
    return
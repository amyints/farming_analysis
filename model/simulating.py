import pandas as pd
import numpy as np
from model.modeling import data_modeling

def simulate(df, model):

    # Generate a range of possible values
    pesticide_range = np.linspace(0.1, 1.0, 10)
    fertilizer_range = np.linspace(0.1, 1.0, 10)
    water_range = np.linspace(0.1, 1.0, 10)
    acre_range = np.linspace(0.1, 1.0, 10)

    # Create a grid of all combinations
    scenarios = pd.DataFrame(
        [(f, p, w, a) for f in fertilizer_range for p in pesticide_range for w in water_range for a in acre_range],
        columns=[ 'Fertilizer_Used(tons)', 'Pesticide_Used(kg)', 'Water_Usage(cubic meters)', 'Farm_Area(acres)']
    )

    # Compute ratio features
    epsilon = 1e-6
    scenarios['pesticide_to_yield_ratio'] = scenarios['Pesticide_Used(kg)'] / (scenarios['Fertilizer_Used(tons)'] + epsilon)
    scenarios['fertilizer_to_yield_ratio'] = scenarios['Fertilizer_Used(tons)'] / (scenarios['Water_Usage(cubic meters)'] + epsilon)
    scenarios['water_to_yield_ratio'] = scenarios['Water_Usage(cubic meters)'] / (scenarios['Pesticide_Used(kg)'] + epsilon)
    scenarios['fertilizer_to_acre_ratio'] = scenarios['Fertilizer_Used(tons)'] / (scenarios['Farm_Area(acres)'])
    scenarios['pesticide_to_acre_ratio'] = scenarios['Pesticide_Used(kg)'] / (scenarios['Farm_Area(acres)'])
    scenarios['water_to_acre_ratio'] = scenarios['Water_Usage(cubic meters)'] / (scenarios['Farm_Area(acres)'])

    # Order columns to match training
    scenarios = scenarios[
        ['Fertilizer_Used(tons)',
        'Pesticide_Used(kg)',
        'Water_Usage(cubic meters)',
        'fertilizer_to_yield_ratio',
        'pesticide_to_yield_ratio',
        'water_to_yield_ratio',
        'fertilizer_to_acre_ratio',
        'pesticide_to_acre_ratio',
        'water_to_acre_ratio'
        ]
    ]
    # Predict yield for each scenario
    scenarios['predicted_yield'] = model.predict(scenarios)

    return scenarios
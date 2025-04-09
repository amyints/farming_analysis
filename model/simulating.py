import pandas as pd
import numpy as np
from model.modeling import data_modeling

def simulate(df, model):

    # Generate a range of possible values
    pesticide_range = np.linspace(0.1, 1.0, 10)
    fertilizer_range = np.linspace(0.1, 1.0, 10)
    water_range = np.linspace(0.1, 1.0, 10)

    # Create a grid of all combinations
    scenarios = pd.DataFrame(
        [(p, f, w) for p in pesticide_range for f in fertilizer_range for w in water_range],
        columns=['pesticide_to_yield_ratio', 'fertilizer_to_yield_ratio', 'water_to_yield_ratio']
    )

    # Predict yield for each scenario
    scenarios['predicted_yield'] = model.predict(scenarios)

    return scenarios
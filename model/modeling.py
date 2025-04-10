from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, StackingRegressor, ExtraTreesRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def data_modeling(df):

    # Prepare features and target
    X = df[[
        'Fertilizer_Used(tons)',
        'Pesticide_Used(kg)',
        'Water_Usage(cubic meters)',
        'fertilizer_to_yield_ratio',
        'pesticide_to_yield_ratio',
        'water_to_yield_ratio',
        'fertilizer_to_acre_ratio',
        'pesticide_to_acre_ratio',
        'water_to_acre_ratio'
        ]]
    y = df['Yield(tons)']


    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Initialize and train the Random Forest model\
    base_learners = [
        ('rf', RandomForestRegressor(
            n_estimators=200,
            max_depth=5,
            min_samples_split=5,
            max_features='sqrt',
            random_state=42
            )),
        ('gb', GradientBoostingRegressor(
            n_estimators=100,
            learning_rate=0.3,
            max_depth=5,
            max_features='sqrt',
            loss='quantile',
            alpha=0.1,
            random_state=42
            )),
        ('et', ExtraTreesRegressor(
            n_estimators=200,
            random_state=42
            )),
        ('knn', Pipeline([
            ('scaler', StandardScaler(with_std=True)),
            ('knn', KNeighborsRegressor(n_neighbors=4)),
         ]))
    ]

    # Meta learner
    meta_learner = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        gamma=0.1,
        min_child_weight=5,
        tree_method='exact',
        random_state=42
        )
    
    model = StackingRegressor(
        estimators=base_learners,
        final_estimator=meta_learner,
        passthrough=True,
        cv=5,
        n_jobs=-1
        )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    print(f"R-Squared: {r2:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

    return model, predictions, X_train, X_test, y_train, y_test
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, StackingRegressor, ExtraTreesRegressor
import numpy as np

def data_modeling(df):

    # Prepare features and target
    X = df[['pesticide_to_yield_ratio', 'fertilizer_to_yield_ratio', 'water_to_yield_ratio']]
    y = df['Yield(tons)']


    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Random Forest model\
    base_learners = [
        ('rf', RandomForestRegressor(n_estimators=200, max_depth=10, min_samples_split=10, max_features='sqrt', random_state=42)),
        ('gb', GradientBoostingRegressor(n_estimators=200, learning_rate=0.3, random_state=42)),
        ('et', ExtraTreesRegressor(n_estimators=100, random_state=42)),
        ('knn', KNeighborsRegressor(n_neighbors=7)),
    ]

    # Meta learner
    meta_learner = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=20, gamma=0.1, random_state=42)
    model = StackingRegressor(estimators=base_learners, final_estimator=meta_learner, passthrough=True, cv=5)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    """
    # Feature importance
    importances = model.feature_importances_
    feature_names = X.columns
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    importance_df.sort_values(by='Importance', ascending=False, inplace=True)

    print('\n Feature Importance:')
    print(importance_df.to_string(index=False))
    """
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    print(f"R-Squared: {r2:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

    return model
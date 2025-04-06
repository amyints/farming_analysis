from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error

def data_modeling(df):
    X = df.drop(columns=['Yield(tons)'])
    y = df['Yield(tons)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model using Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rsme = root_mean_squared_error(y_test, predictions, squared=False)

    print(f"R-Squared: {r2}")
    print(f"MAE: {mean_absolute_error(y_test, predictions)}")
    print(f"RSME: {rsme}")

    return 
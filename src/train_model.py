import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# 1. Load Data
print("Loading California Housing dataset...")
try:
    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="MedHouseVal")
except Exception as e:
    print(f"Failed to download dataset: {e}")
    print("Generating synthetic data for demonstration...")
    from sklearn.datasets import make_regression
    import numpy as np
    
    X_synthetic, y_synthetic = make_regression(n_samples=1000, n_features=8, noise=0.1, random_state=42)
    feature_names = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
    X = pd.DataFrame(X_synthetic, columns=feature_names)
    # Scale to match typical housing prices (e.g. 0-5)
    y = pd.Series(y_synthetic, name="MedHouseVal")
    y = (y - y.min()) / (y.max() - y.min()) * 5


# 2. Split Data
print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Model
print("Training Random Forest Regressor...")
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# 4. Evaluate
print("Evaluating model...")
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.4f}")
print(f"R2 Score: {r2:.4f}")

# 5. Save Model
model_path = "model.joblib"
print(f"Saving model to {model_path}...")
joblib.dump(model, model_path)
print("Done!")

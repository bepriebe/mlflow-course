# Import the libraries used for training and evaluation.
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Load the course data from the repository's data directory.
data = pd.read_csv("data/fake_data.csv")
X = data.drop(columns=["date", "demand"])
y = data["demand"]
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model with a small, reproducible parameter set.
params = {
    "n_estimators": 10,
    "max_depth": 10,
    "random_state": 42,
}
rf = RandomForestRegressor(**params)
rf.fit(X_train, y_train)

# Evaluate the model on the validation split.
y_pred = rf.predict(X_val)
mae = mean_absolute_error(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_val, y_pred)
metrics = {"mae": mae, "mse": mse, "rmse": rmse, "r2": r2}

print(metrics)

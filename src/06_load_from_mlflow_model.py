import mlflow
import pandas as pd
import numpy as np

# 1. Load data
print("Loading data...")
data = pd.read_csv("data/fake_data.csv")
X = data.drop(columns=["date", "demand"])
X = X.astype('float')

# 2. Point MLflow to the local tracking server and registered model version.
mlflow.set_tracking_uri("http://127.0.0.1:8080")
model_path = "models:/AppleDemandModel/1"

# 3. Load the model
print("Loading model...")
model = mlflow.sklearn.load_model(model_path)

# 4. Make predictions on the entire dataset
print("Calculating predictions...")
predictions = model.predict(X)

# 5. Calculate and display the average of predictions
mean_prediction = np.mean(predictions)

print(f"\nResults:")
print(f"Number of predictions: {len(predictions)}")
print(f"Mean of predictions: {mean_prediction:.2f}")

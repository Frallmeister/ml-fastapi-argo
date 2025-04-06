# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a model (Random Forest for simplicity)
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the model and class names to a file
joblib.dump({"model": model, "target_names": iris.target_names}, "model.joblib")
print("Model trained and saved to model.joblib")

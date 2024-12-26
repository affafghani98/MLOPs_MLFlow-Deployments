import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
data = load_iris()
X, y = data.data, data.target

#different random states for each split to introduce variation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=np.random.randint(1, 100))
# Hyperparameters with more variation
n_estimators = [5, 50, 200]  
max_depth = [2, 5, 10]  
min_samples_split = [2, 5, 10]  
best_model = None
best_accuracy = 0
best_run_id = None
mlflow.set_experiment("Iris_Classification_Experiment")    # Set experiment
# Train and log models
for n in n_estimators:
    for depth in max_depth:
        for min_split in min_samples_split:
            with mlflow.start_run():
                # Create model with more parameters
                model = RandomForestClassifier(
                    n_estimators=n,
                    max_depth=depth,
                    min_samples_split=min_split,
                    random_state=np.random.randint(1, 100)  # Random state for each model
                )
                model.fit(X_train, y_train)#Train the  model
                y_pred = model.predict(X_test) #  predictions
                accuracy = accuracy_score(y_test, y_pred)
                # Log parameters and metrics
                mlflow.log_param("n_estimators", n)
                mlflow.log_param("max_depth", depth)
                mlflow.log_param("min_samples_split", min_split)
                mlflow.log_metric("accuracy", accuracy)

                mlflow.sklearn.log_model(model, "model")
                if accuracy > best_accuracy:      # Track best model
                    best_accuracy = accuracy
                    best_run_id = mlflow.active_run().info.run_id

                print(f"Run completed:")
                print(f"- n_estimators: {n}")
                print(f"- max_depth: {depth}")
                print(f"- min_samples_split: {min_split}")
                print(f"- accuracy: {accuracy:.4f}")
                print("-" * 50)

print(f"\nBest Model Run ID: {best_run_id}")
print(f"Best Model Accuracy: {best_accuracy:.4f}")
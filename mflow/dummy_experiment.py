import mlflow
import random

# local tracking URI
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("DevOps_Intern_Experiment")

with mlflow.start_run():
    # Logging dummy hyperparameters
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)

    # Logging a dummy metric
    dummy_accuracy = random.uniform(0.8, 0.99)
    mlflow.log_metric("accuracy", dummy_accuracy)

    print(f"Logged experiment run with accuracy: {dummy_accuracy:.4f}")
# Task 1: MLFlow Hyperparameter Tuning

This folder contains the code and files for **Task 1** of the MLOps project. It demonstrates the use of MLFlow for hyperparameter tuning, experiment tracking, and serving the best-performing model.

## Features
- **Hyperparameter Tuning**: Uses MLFlow to track 27 combinations of hyperparameters.
- **Experiment Tracking**: Logs metrics, parameters, and artifacts in MLFlow.
- **Model Serving**: Serves the best-performing model locally for predictions.

## File Descriptions
- **`train_model.py`**: Script to train the model, perform hyperparameter tuning, and log experiments in MLFlow.
- **`test_model.py`**: Script to serve the best-performing model and handle prediction requests.
- **`requirements.txt`**: List of dependencies required to run the scripts.
- **`.gitignore`**: Prevents unnecessary files (like logs) from being tracked in Git.

## Prerequisites
- Python 3.8 or higher
- MLFlow installed
- Necessary Python libraries (see `requirements.txt`)

## How to Run
1. Clone the repository and navigate to the Task folder:
   ```bash
   git clone <my-repo-url>
   cd MLFlow_Hyperparameter_Tuning-Task
2. Install the required dependencies:
 ```bash
   pip install -r requirements.txt.
  ```
3. Run command "mlflow ui" in one terminal then
4. Run the training script to perform hyperparameter tuning and log results to MLFlow
 
```bash
python train_model.py
```
5. Serve the best-performing model locally:
```bash
python test_model.py
```
6. Test the served model using curl or Python requests
```bash
#example curl command:
curl -X POST -H "Content-Type: application/json" \
    -d '{"instances": [[5.1, 3.5, 1.4, 0.2]]}' \
    http://127.0.0.1:5000/invocations
```

## Notes
1. Experiment logs and artifacts are stored locally in mlruns (not included in the repository).
2. Use the MLFlow UI to explore experiment results (mlflow ui).






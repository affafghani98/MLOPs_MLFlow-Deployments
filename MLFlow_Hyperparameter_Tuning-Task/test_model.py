
import requests
import json

data = {
    "instances": [
        [5.1, 3.5, 1.4, 0.2] 
    ]
}

url = "http://127.0.0.1:8000/invocations"

try:
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )

    if response.status_code == 200:
        result = response.json()
        predictions = result['predictions']
        print("\nRaw predictions:", predictions)

        # Map predictions to iris types
        iris_types = ['setosa', 'versicolor', 'virginica']
        for i, pred in enumerate(predictions):
            print(f"Sample {i+1}: {iris_types[int(pred)]}")
    else:
        print(f"Error: Status code {response.status_code}")
        print(response.text)

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the model server.")
    
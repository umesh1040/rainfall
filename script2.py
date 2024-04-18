import sys
import json
import pandas as pd
import pickle

# Load the trained XGBoost model from the .pkl file
with open('xgb_model.pkl', 'rb') as f:
    xgb_model = pickle.load(f)

# Assuming sys.argv[1] contains JSON data as a string
json_data = sys.argv[1]

# Parse JSON string into a Python dictionary
data_dict = json.loads(json_data)

# Retrieve values from the dictionary and convert to float
temperature_celsius = float(data_dict["temperature_celsius"])
wind_mph = float(data_dict["wind_mph"])
pressure_in = float(data_dict["pressure_in"])
humidity = float(data_dict["humidity"])
cloud = float(data_dict["cloud"])
visibility_km = float(data_dict["visibility_km"])

new_data = pd.DataFrame({
    'temperature_celsius': [temperature_celsius],
    'wind_mph': [wind_mph],
    'pressure_in': [pressure_in],
    'humidity': [humidity],
    'cloud': [cloud],
    'visibility_km': [visibility_km]
})

# Use the model to predict
xgb_predictions = int(xgb_model.predict(new_data)) # Convert prediction to int

# Prepare the response data
response_data = {"xgb_predictions": xgb_predictions}

# Convert response data to JSON and print it
print(json.dumps(response_data))

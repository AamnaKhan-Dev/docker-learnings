
import json
with open("patients.json", "r") as f:
    data=json.load(f)
    
print(data)
import json

MODEL_FILE = "model.json"

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

with open(MODEL_FILE, "r") as f:
    model = json.load(f)

theta0 = model["theta0"]
theta1 = model["theta1"]

mileage = float(input("Enter mileage (km): "))
price = estimate_price(mileage, theta0, theta1)
print(f"Estimated price: {price:.2f}")

import json

MODEL_FILE = "thetas.txt"

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def main():
    with open(MODEL_FILE, "r") as f:
        model = json.load(f)

    theta0 = model["theta0"]
    theta1 = model["theta1"]

    mileage = float(input("Enter mileage (km): "))
    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price: {price:f}")


if __name__ == "__main__":
    main()
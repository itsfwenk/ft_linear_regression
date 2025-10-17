import json

MODEL_FILE = "thetas.txt"

def estimate_price(mileage, theta0, theta1):
    '''
    Estimates the price of a car given its mileage and the model parameters.
    '''
    return theta0 + theta1 * mileage


def main():
    '''
    Loads the model parameters from thetas.txt and prompts the user for mileage to estimate the car price.'''
    with open(MODEL_FILE, "r") as f:
        model = json.load(f)

    theta0 = model["theta0"]
    theta1 = model["theta1"]

    mileage = float(input("Enter mileage (km): "))
    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price: {price:f}")


if __name__ == "__main__":
    main()
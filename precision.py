import json
import utils
import sys
import pandas as pd
import numpy as np

MODEL_FILE = "thetas.txt"


def evaluate_regression(y_true, y_pred):
    """
    Calculates regression metrics:
    - MAE (Mean Absolute Error)
    - RMSE (Root Mean Square Error)
    - R² Score (Coefficient of Determination)
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    m = len(y_true)

    mae = np.mean(np.abs(y_pred - y_true))

    rmse = np.sqrt(np.sum((y_pred - y_true) ** 2) / m)

    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_pred) ** 2)
    r2 = 1 - (ss_residual / ss_total)

    print(f"MAE = {mae}")
    print(f"RMSE = {rmse}")
    print(f"R2 = {r2}")

def main():
    '''
    Loads the model parameters from thetas.txt and evaluates the model on data.csv file.
    '''
    with open(MODEL_FILE, "r") as f:
        model = json.load(f)

    theta0 = model["theta0"]
    theta1 = model["theta1"]

    datafilename = 'data.csv'
    df = utils.load_csv(datafilename)

    if df is None:
        sys.exit(1)
    km = df.loc[:,'km'].values.flatten().astype(float)
    price = df.loc[:,'price'].values.flatten().astype(float)

    df = pd.DataFrame({
        "km": km,
        "price": price
    })
    y_hat = theta0 + theta1 * np.array(km)
    evaluate_regression(price, y_hat)


if __name__ == "__main__":
    main()
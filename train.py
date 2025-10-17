import pandas as pd
import os
import sys
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import utils


def plot_lr(x, y, theta0, theta1):
    '''
    Plots the linear regression line along with the data points.'''
    df = pd.DataFrame({
        "km": x,
        "price": y
    })
    y_hat = theta0 + theta1 * np.array(x)
    # evaluate_regression(y, y_hat)
    sns.scatterplot(data=df, x="km", y="price")
    plt.plot(x, y_hat, color="magenta", label="Regression Line")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price (EUR)")
    plt.legend()
    plt.tight_layout()
    plt.show()



def minmax_norm(x: np.ndarray) -> np.ndarray:
    '''
    Performs min-max normalization on data array
    '''
    xmin = np.min(x)
    xmax = np.max(x)
    normalized_data = (x - xmin) / (xmax - xmin)
    return normalized_data


def denormalize_thetas(theta0, theta1, x: np.ndarray) :
    '''
    Denormalize thetas values.
    '''
    real_theta1 = theta1 / (np.max(x) - np.min(x))
    real_theta0 = theta0 - real_theta1 * np.min(x)
    return real_theta0, real_theta1


# def evaluate_regression(y_true, y_pred):
#     """
#     Calculates regression metrics:
#     - MAE (Mean Absolute Error)
#     - RMSE (Root Mean Square Error)
#     - R² Score (Coefficient of Determination)
#     """
#     y_true = np.array(y_true)
#     y_pred = np.array(y_pred)

#     m = len(y_true)

#     mae = np.mean(np.abs(y_pred - y_true))

#     rmse = np.sqrt(np.sum((y_pred - y_true) ** 2) / m)

#     ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
#     ss_residual = np.sum((y_true - y_pred) ** 2)
#     r2 = 1 - (ss_residual / ss_total)

#     print(f"MAE = {mae}")
#     print(f"RMSE = {rmse}")
#     print(f"R2 = {r2}")




def main():
    '''
    Trains a linear regression model using gradient descent on the data from data.csv file.
    Saves the learned parameters (theta0 and theta1) to thetas.txt file.
    '''
    datafilename = 'data.csv'
    df = utils.load_csv(datafilename)

    if df is None:
        sys.exit(1)
    km = df.loc[:,'km'].values.flatten().astype(float)
    price = df.loc[:,'price'].values.flatten().astype(float)

    theta0 = 0
    theta1 = 0
    learningRate = 0.01
    iterations = 1000

    km_norm = minmax_norm(km)

    for i in range(iterations):
        m = len(km_norm)
        for i in range(iterations):
            estimatePrice = theta0 + theta1 * km_norm
            error = estimatePrice - price

            tmpTheta0 = (learningRate / m) * error.sum()
            tmpTheta1 = (learningRate / m) * (error * km_norm).sum()

            theta0 -= tmpTheta0
            theta1 -= tmpTheta1

    real_theta0, real_theta1 = denormalize_thetas(theta0,theta1, km)

    data = {"theta0": real_theta0, "theta1": real_theta1}
    print(data)

    # print(f"For a car of 240000km, price is : {real_theta0 + real_theta1 * 240000}")
    with open('thetas.txt', 'w') as f:
        json.dump(data, f)

    plot_lr(km, price, real_theta0, real_theta1)






if __name__ == "__main__":
    main()

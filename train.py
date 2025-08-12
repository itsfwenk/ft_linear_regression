import pandas as pd
import os
import sys
import json
import matplotlib.pyplot as plt
import seaborn as sns

def load(path: str) -> pd.DataFrame:
    """
    Takes a path as argument and returns it.

    Args:
        arg1 (str): The path of the data set to load.

    Returns:
        A pandas dataframe of the data set.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: File '{path}' not found.")
        if not os.path.isfile(path):
            raise ValueError(f"Error: '{path}' is not a valid file.")
        if not path.lower().endswith(".csv"):
            raise AssertionError("file must be .csv.")

        df = pd.read_csv(path)
        # print(f"Loading dataset of dimensions {df.shape}")
        return df

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The CSV file '{path}' is empty.")
        return None
    except pd.errors.ParserError as e:
        print(
            f"Error: Could not parse '{path}': {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading '{path}': {e}")
        return None


# def load_predict_param(path: str) -> dict:
#     try:
#         if not os.path.exists(path):
#             raise FileNotFoundError(f"Error: File '{path}' not found.")
#         if not os.path.isfile(path):
#             raise ValueError(f"Error: '{path}' is not a valid file.")

#         with open(path, 'r') as f:
#             json_data = json.load(f)

#         required_keys = ["theta0", "theta1"]
#         for key in required_keys:
#             if key not in json_data:
#                 raise KeyError(f"Missing required key: {key}")

#         theta0 = json_data["theta0"]
#         theta1 = json_data["theta1"]
#         if not isinstance(theta0, (int, float)):
#             raise TypeError(f"theta0 must be a number, got {type(theta0).__name__}")
#         if not isinstance(theta1, (int, float)):
#             raise TypeError(f"theta1 must be a number, got {type(theta1).__name__}")

#         return json_data

#     except (FileNotFoundError, ValueError, json.JSONDecodeError, KeyError, TypeError) as e:
#         print(e)
#         sys.exit(1)


def plot_dots(x, y, x_name, y_name):
    df = pd.DataFrame({
        x_name: x,
        y_name: y
    })
    sns.scatterplot(data=df, x=x_name, y=y_name)
    plt.tight_layout()
    plt.show()


def main():
    datafilename = 'data.csv'
    # paramfilename = 'predict_param.txt'
    df = load(datafilename)

    if df is None:
        sys.exit(1)
    km = df.loc[:,'km'].values.flatten()
    price = df.loc[:,'price'].values.flatten()

    plot_dots(km, price, "km", "price")
    # json_data = load_predict_param(paramfilename)
    # theta0 = json_data['theta0']
    # theta1 = json_data['theta1']

    theta0 = 0
    theta1 = 0
    learningRate = 1e-8
    iterations = 1000

    # km_mean = km.mean()
    # km_std = km.std()
    # km_scaled = (km - km_mean) / km_std

    for i in range(iterations):
        m = len(km)
        for i in range(iterations):
            estimatePrice = theta0 + theta1 * km
            error = estimatePrice - price

            tmpTheta0 = (learningRate / m) * error.sum()
            tmpTheta1 = (learningRate / m) * (error * km).sum()

            theta0 -= tmpTheta0
            theta1 -= tmpTheta1

    data = {"theta0": theta0, "theta1": theta1}
    print(data)

    print(f"For a car of 240000km, price is : {theta0 + theta1 * 240000}")
    with open('predict_param.txt', 'w') as f:
        json.dump(data, f)






if __name__ == "__main__":
    main()

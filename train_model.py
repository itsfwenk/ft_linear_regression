import pandas as pd
import os
import sys

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


def main():
    df = load("data.csv")
    if df is None:
        sys.exit(1)
    km = df.loc[:,'km'].values.flatten()
    price = df.loc[:,'price'].values.flatten()
    theta0 = 0
    theta1 = 0
    learningRate = 0.01
    iterations = 1000

    estimatePrice = theta0 + theta1 * km

    sum_error = sum(x - y for x, y in zip(estimatePrice, price))
    tmpTheta0 = learningRate * (1 / len(km)) * sum_error

    sum_scaled_error = sum((x - y) * z for x, y, z in zip(estimatePrice, price, km))
    tmpTheta1 = learningRate * (1 / len(km)) * sum_scaled_error


if __name__ == "__main__":
    main()

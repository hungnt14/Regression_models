import pandas as pd


def preprocess_data(df):
    """return the preprocessed dataframe"""
    """ currently not implemented any preprocess method"""
    return df


def load_data(data_path):
    """return Pandas dataframes of X, y from the original data"""
    df = pd.read_csv(data_path)
    df = preprocess_data(df)
    feature_columns = [
        "Relative_Humidity",
        "Specific_Humidity",
        "Precipitation",
        "Pressure",
        "Wind_Speed",
        "Wind_Direction",
    ]
    X_train = df[df["YEAR"] < 2021][feature_columns].values
    y_train = df[df["YEAR"] < 2021]["Temperature"].values
    X_test = df[df["YEAR"] == 2021][feature_columns].values
    y_test = df[df["YEAR"] == 2021]["Temperature"].values
    return X_train, y_train, X_test, y_test

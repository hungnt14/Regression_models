import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(df):
    """return the preprocessed dataframe"""
    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df))
    return df


def load_data(data_path, preprocess=False):
    """return Pandas dataframes of X, y from the original data"""
    df = pd.read_csv(data_path)
    feature_columns = [
        "Relative_Humidity",
        "Specific_Humidity",
        "Precipitation",
        "Pressure",
        "Wind_Speed",
        "Wind_Direction",
    ]
    if preprocess:
        X_train = preprocess_data(df[df["YEAR"] < 2021][feature_columns]).values
        X_test = preprocess_data(df[df["YEAR"] == 2021][feature_columns]).values
    else:
        X_train = df[df["YEAR"] < 2021][feature_columns].values
        X_test = df[df["YEAR"] == 2021][feature_columns].values
    y_train = df[df["YEAR"] < 2021]["Temperature"].values
    y_test = df[df["YEAR"] == 2021]["Temperature"].values
    return X_train, y_train, X_test, y_test

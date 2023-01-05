import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(df):
    """return the preprocessed dataframe"""
    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df))
    return df

def derive_nth_day_feature(df_derive, df, feature, N):
    rows=df.shape[0]
    nth_prior_measurements = [None]*N + [df[feature][i-N] for i in range(N,rows)]
    col_name="{}_{}".format(feature, N)
    df_derive[col_name]=nth_prior_measurements

def prepare_data(df):
    df_derive = df[['YEAR', 'Temperature']]
    for feature in df.columns:
        if feature not in ['YEAR','MO','DY']:
            for N in range(1,4):
                derive_nth_day_feature(df_derive, df, feature, N)
    df_derive.dropna(inplace = True)
    df_derive.reset_index(inplace = True)
    df_derive.drop(['index'], axis = 1, inplace = True)
    return df_derive

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
    df.drop(['Specific_Humidity', 'Wind_Direction', 'Pressure'], axis = 1, inplace = True)
    df_derive = prepare_data(df)
    train = df_derive[df_derive["YEAR"] < 2021].drop('YEAR', axis = 1)
    test = df_derive[df_derive["YEAR"] == 2021].drop('YEAR', axis = 1)
    X_train = train.drop('Temperature', axis = 1).values
    X_test = test.drop('Temperature', axis = 1).values
    if preprocess:
        X_train = preprocess_data(X_train)
        X_test = preprocess_data(X_test)
    y_train = train["Temperature"]
    y_test = test["Temperature"]
    return X_train, y_train, X_test, y_test

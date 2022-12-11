from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


def MAPE(y_true, y_pred):
    return mean_absolute_percentage_error(y_true, y_pred)


def RMSE(y_true, y_pred):
    return mean_squared_error(y_true, y_pred, squared=False)


def MAE(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)


def MAPE_scorer(model, X, y):
    y_pred = model.predict(X)
    return MAPE(y, y_pred)


def RMSE_scorer(model, X, y):
    y_pred = model.predict(X)
    return RMSE(y, y_pred)


def MAE_scorer(model, X, y):
    y_pred = model.predict(X)
    return MAE(y, y_pred)

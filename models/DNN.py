from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
from keras.models import load_model
from scikeras.wrappers import KerasRegressor

from models.base_model import BaseModel
import pickle as pkl


def create_model():
    model = Sequential()

    model.add(Dense(units=256, kernel_initializer='normal', activation="relu"))
    model.add(Dense(units=256, kernel_initializer='normal', activation="relu"))
    model.add(Dense(units=256, kernel_initializer='normal', activation="relu"))

    model.add(Dense(units=1, kernel_initializer='normal', activation="linear"))

    model.compile(loss='mean_absolute_error', optimizer='adam')

    return model

class DNN(BaseModel):
    def __init__(self, opt):
        # self.opt = opt
        self.model = keras.wrappers.scikit_learn.KerasRegressor(build_fn=create_model, **opt)

    def fit(self, X, y):
        self.model.fit(X, y)

    def save_model(self, weight_path):
        self.model.model.save(weight_path)

    def load_model(self, weight_path):
        self.model.model = load_model(weight_path)

    def predict(self, X):
        return self.model.predict(X)

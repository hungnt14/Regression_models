from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
import tensorflow as tf

from models.base_model import BaseModel
import pickle as pkl


class DNN(BaseModel):
    def __init__(self, opt):
        self.opt = opt
        print(opt)

        model = Sequential()

        model.add(Dense(units=256, kernel_initializer='normal', activation="relu"))
        model.add(Dense(units=256, kernel_initializer='normal', activation="relu"))
        model.add(Dense(units=256, kernel_initializer='normal', activation="relu"))

        model.add(Dense(units=1, kernel_initializer='normal', activation="linear"))

        model.compile(loss='mean_absolute_error')

        self.model = model

    def fit(self, X, y):
        self.model.fit(X, y, epochs=100, batch_size=32)

    def save_model(self, weight_path):
        pkl.dump(self.model, open(weight_path, "wb"))

    def load_model(self, weight_path):
        self.model = pkl.load(open(weight_path, "rb"))

    def predict(self, X):
        return self.model.predict(X)

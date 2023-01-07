from sklearn import linear_model
from models.base_model import BaseModel
from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression
import pickle as pkl


class ElasticNet(BaseModel):
    def __init__(self, opt):
        self.model = linear_model.ElasticNet(**opt)

    def fit(self, X, y):
        self.model.fit(X, y)

    def save_model(self, weight_path):
        pkl.dump(self.model, open(weight_path, "wb"))

    def load_model(self, weight_path):
        self.model = pkl.load(open(weight_path, "rb"))

    def predict(self, X):
        return self.model.predict(X)

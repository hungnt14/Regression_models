import sys

sys.path.append(".")

from models.LinearSGD import *
from models.DNN import *
from models.DecisionTree import *
from models.RidgeRegression import *
from models.LassoRegression import *
from models.GradientBoosting import *
from models.LightGBM import *

def get_instance(config, **kwargs):
    assert "name" in config
    config.setdefault("args", {})
    if config["args"] is None:
        config["args"] = {}
    return globals()[config["name"]](config["args"], **kwargs)

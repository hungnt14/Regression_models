import sys

sys.path.append(".")

import argparse
import yaml

from utils.dataloader import load_data
from utils.getter import get_instance
from utils.evaluate import MAE_scorer, MAPE_scorer, RMSE_scorer


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path", default="data/Thu-Duc_Weather_Dataset.csv", help="csv data path"
    )
    parser.add_argument(
        "--config_path", default="configs/LinearSGD.yml", help="config file path"
    )
    parser.add_argument(
        "--weight_path",
        default="weights/LinearSGD.pkl",
        help="weight path to store model",
    )
    parser.add_argument(
        "--test_metric",
        default="MAPE",
        help="test metric",
    )
    return parser.parse_args()


def test(args):
    # load data
    X_train, y_train, X_test, y_test = load_data(args.data_path)
    # load model
    model_configs = yaml.load(open(args.config_path, "r"), Loader=yaml.Loader)
    model = get_instance(model_configs)
    model.load_model(args.weight_path)
    # test
    SCORER_DICT = {"MAE": MAE_scorer, "MAPE": MAPE_scorer, "RMSE": RMSE_scorer}
    print(
        f"Test score ({args.test_metric}) on testset: ",
        SCORER_DICT[args.test_metric](model, X_test, y_test),
    )


if __name__ == "__main__":
    args = get_parser()
    test(args)

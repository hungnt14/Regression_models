python3 -W ignore tools/train.py --config_path configs/DecisionTree.yml --val_metric MAPE --weight_path weights/DecisionTree_MAPE.pkl
python3 -W ignore tools/test.py --config_path configs/DecisionTree.yml --test_metric MAPE --weight_path weights/DecisionTree_MAPE.pkl
python3 -W ignore tools/train.py --config_path configs/DecisionTree.yml --val_metric RMSE --weight_path weights/DecisionTree_RMSE.pkl
python3 -W ignore tools/test.py --config_path configs/DecisionTree.yml --test_metric RMSE --weight_path weights/DecisionTree_RMSE.pkl
python3 -W ignore tools/train.py --config_path configs/DecisionTree.yml --val_metric MAE --weight_path weights/DecisionTree_MAE.pkl
python3 -W ignore tools/test.py --config_path configs/DecisionTree.yml --test_metric MAE --weight_path weights/DecisionTree_MAE.pkl
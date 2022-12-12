python3 -W ignore tools/train.py --config_path configs/DNN.yml --val_metric MAPE --weight_path weights/DNN_MAPE
python3 -W ignore tools/test.py --config_path configs/DNN.yml --test_metric MAPE --weight_path weights/DNN_MAPE
python3 -W ignore tools/train.py --config_path configs/DNN.yml --val_metric RMSE --weight_path weights/DNN_RMSE
python3 -W ignore tools/test.py --config_path configs/DNN.yml --test_metric RMSE --weight_path weights/DNN_RMSE
python3 -W ignore tools/train.py --config_path configs/DNN.yml --val_metric MAE --weight_path weights/DNN_MAE
python3 -W ignore tools/test.py --config_path configs/DNN.yml --test_metric MAE --weight_path weights/DNN_MAE
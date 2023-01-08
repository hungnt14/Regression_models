python3 -W ignore tools/train.py --config_path configs/ElasticNet.yml --val_metric MAPE --weight_path weights/ElasticNet_MAPE
python3 -W ignore tools/test.py --config_path configs/ElasticNet.yml --test_metric MAPE --weight_path weights/ElasticNet_MAPE
python3 -W ignore tools/train.py --config_path configs/ElasticNet.yml --val_metric RMSE --weight_path weights/ElasticNet_RMSE
python3 -W ignore tools/test.py --config_path configs/ElasticNet.yml --test_metric RMSE --weight_path weights/ElasticNet_RMSE
python3 -W ignore tools/train.py --config_path configs/ElasticNet.yml --val_metric MAE --weight_path weights/ElasticNet_MAE
python3 -W ignore tools/test.py --config_path configs/ElasticNet.yml --test_metric MAE --weight_path weights/ElasticNet_MAE
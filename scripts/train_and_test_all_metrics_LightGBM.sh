python -W ignore tools/train.py --config_path configs/LightGBM.yml --val_metric MAPE --weight_path weights/LightGBM_MAPE
python -W ignore tools/test.py --config_path configs/LightGBM.yml --test_metric MAPE --weight_path weights/LightGBM_MAPE
python -W ignore tools/train.py --config_path configs/LightGBM.yml --val_metric RMSE --weight_path weights/LightGBM_RMSE
python -W ignore tools/test.py --config_path configs/LightGBM.yml --test_metric RMSE --weight_path weights/LightGBM_RMSE
python -W ignore tools/train.py --config_path configs/LightGBM.yml --val_metric MAE --weight_path weights/LightGBM_MAE
python -W ignore tools/test.py --config_path configs/LightGBM.yml --test_metric MAE --weight_path weights/LightGBM_MAE
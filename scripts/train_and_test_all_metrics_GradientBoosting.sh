python3 -W ignore tools/train.py --config_path configs/GradientBoosting.yml --val_metric MAPE --weight_path weights/GradientBoosting_MAPE.pkl
python3 -W ignore tools/test.py --config_path configs/GradientBoosting.yml --test_metric MAPE --weight_path weights/GradientBoosting_MAPE.pkl
python3 -W ignore tools/train.py --config_path configs/GradientBoosting.yml --val_metric RMSE --weight_path weights/GradientBoosting_RMSE.pkl
python3 -W ignore tools/test.py --config_path configs/GradientBoosting.yml --test_metric RMSE --weight_path weights/GradientBoosting_RMSE.pkl
python3 -W ignore tools/train.py --config_path configs/GradientBoosting.yml --val_metric MAE --weight_path weights/GradientBoosting_MAE.pkl
python3 -W ignore tools/test.py --config_path configs/GradientBoosting.yml --test_metric MAE --weight_path weights/GradientBoosting_MAE.pkl
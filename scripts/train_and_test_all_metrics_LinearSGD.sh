if [[ "$OSTYPE" =~ ^msys ]]; then
    py -3 tools/train.py --val_metric RMSE
    py -3 tools/test.py --test_metric RMSE
else
    python3 tools/train.py --val_metric RMSE
    python3 tools/test.py --test_metric RMSE
fi
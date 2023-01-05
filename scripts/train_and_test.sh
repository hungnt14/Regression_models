if [[ "$OSTYPE" =~ ^msys ]]; then
  python tools/train.py --val_metric RMSE
  python tools/test.py --test_metric RMSE
else
  python3 tools/train.py --val_metric RMSE
  python3 tools/test.py --test_metric RMSE
fi
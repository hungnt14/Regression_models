# [CS116.N11.KHTN] Regression models 

### 1. Members info and picked models:

| Name | Student ID | Model |
|-|-|-|
| Lê Xuân Tùng | 20520347 | Lasso Regression
| Danh Võ Hồng Phúc | 20520275 | Ridge Regression
| Mai Trung Kiên | 20520066 | Deep Neural Networks
| Cao Văn Hùng | 20520193 | LightGBM
| Lê Phước Vĩnh Linh | 20521531 | Decision Tree
| Nguyễn Tiến Hưng | 20520198 | Linear SGD
| Nguyễn Quốc Huy Hoàng | 20520051 | Bayesian
| Lê Nhật Kha | 20520208 | Gradient Boosting
| Nguyễn Vĩnh Hưng | 20520055 | Elastic-Net Regression
  
### 2. Problem description:
- Weather forecasting is extremely important because it gives information that helps to safeguard human life and property by preventing natural disasters and floods. This is especially crucial for someone like me who is weather-sensitive. Therefore, to better understand how weather forecasting works, and to explore if, based on previous experience observing climate data, can a Machine Learning model that reliably forecasts the weather be built.

- Problem modelling:
  + Input: 3-day continuous weather data for an area (here is
Thu Duc City), including temperature, humidity precipitation, pressure, and other variables.
  + Output: The average temperature of the day that need to be predicted.
  
### 3. Dataset:
- Name: **Thu Duc weather dataset**
- Source: crawled from [NASA](https://power.larc.nasa.gov/data-access-viewer/)
- Time range: 2000 - 2021 (21 years)
- Attributes: Date, Temperature, Relative Humidity, Specific Humidity, Precipitation, Pressure, Wind Speed, Wind Direction

### 4. Evaluation method:
- Metrics: 
  + MAPE (Mean Absolute Percentage Error)
  + RMSE (Root Mean Square Error)
  + MAE (Mean Absolute Error)
- Protocol: Weather data in 2021 will be used as a test set to give comparison between models. Remain data will be used as a train + validation set. For train and validation, we used K-Fold Cross Validation (with k = 5).

### 5. Re-implement instruction:
#### End-to-end run:
```
sh scripts/train_and_test.sh
```

#### Add your model:

First, create your own config file in `configs/` folder, using below structure:

```
name: <Your model name>
args:
  <Your model configuration>
  ...
```
View the example `LinearSGD.yml` for better understanding.

Next, create your model class in `models/` folder. View example to create it.

Note: 
- Your model name must be matched with the class name you created in `models`
- Your class name must not be the same as scikit-learn model name, this can cause unlimited recursion when initializing.
- ...

# load the train and test
# train algo
# save the metrices, params
import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json

#Metric Evaluation
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

#Training and Evaluation
def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"] # this is found in params.yaml
    train_data_path = config["split_data"]["train_path"] # this is found in params.yaml
    raw_data_path = config["load_data"]["raw_dataset_csv"] # this is found in params.yaml
    split_ratio = config["split_data"]["test_size"] # this is found in params.yaml
    random_state = config["base"]["random_state"] # this is found in params.yaml

    model_dir = config["model_dir"]  # this is found in params.yaml
    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"] # this is found in params.yaml
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"] # this is found in params.yaml
    target = [config["base"]["target_col"]] # this is found in params.yaml

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(train_data_path, sep=",")

    train_x = train.drop(target, axis=1)
    test_x = train.drop(target, axis=1)
    train_y = train[target]
    test_y = test[target]

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)
    
    predicted_qualities = lr.predict(test_x)

    #Evaluation
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)
    
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(lr, model_path)




if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
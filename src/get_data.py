import os
import yaml
import argparse
import pandas as pd

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    # print(config) This will return all the parameters and paths in 'params.yaml' file. From there, we can retrieve the data we want
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    # print(df)
    return df


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--config", default="params.yaml")
    parsed_args = arg.parse_args()
    data = get_data(config_path = parsed_args.config)

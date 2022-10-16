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
    print(config)



if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--config", default="params.yaml")
    parsed_args = arg.parse_args()
    data = get_data(config_path = parsed_args.config)

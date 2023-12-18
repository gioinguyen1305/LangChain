import json
import os


def setup_openai_key():
    with open('keys.json', 'r') as file:
        for k, v in json.load(file).items():
            os.environ[k] = v

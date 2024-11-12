import json
import os

# Função para carregar as configurações
def load_config():
    config_path = os.path.join("config", "config.json")
    with open(config_path, "r") as f:
        return json.load(f)
